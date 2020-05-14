import os
import sqlite3
import logging
import sys
from pyexpat import ExpatError
from Counter import Counter
from Fb2File import Fb2File
from FolderCheck import FolderCheck
from SqliteCon import SqliteCon


class Conductor:

    def __init__(self, path):
        self.path = path

    def run(self):
        path = self
        try:
            check_input = FolderCheck(path)
            # check the folder. If it includes "wrong" files these files are moved to "incorrect_input". The function
            # returns the list of fb2 files
            file_list = check_input.remove_files()
        except FileNotFoundError as e:
            logging.error(e)

        # read and count all the necessary values for each file
        for file in file_list:
            get_path = check_input.path + file
            try:
                f = Fb2File(get_path)
            except ExpatError as e:
                logging.error(e)
                os.rename(get_path, 'incorrect_input/' + file)
                continue

            title = Fb2File.get_title(f)
            paragraphs = Fb2File.count_paragraphs(f)
            fb2_word_list = Fb2File.get_words(f)
            capital_words = Counter.count_cap_words(fb2_word_list)
            words = Counter.count_words(fb2_word_list)
            lower_words = Counter.count_low_words(fb2_word_list)
            letters = Counter.count_letters(fb2_word_list)
            try:
                my_db = SqliteCon()
            except sqlite3.OperationalError as e:
                logging.error(e)
                # connect to db and fill in the table "text_info". The table is created with connection to db
            try:
                query = 'INSERT INTO text_info(book_name, number_of_paragraph, number_of_words,' \
                        ' number_of_letters, words_with_capital_letters, words_in_lowercase) ' \
                        'VALUES(\'' + title + '\',' + str(paragraphs) + ',' + str(words) + ',' \
                        + str(letters) + ',' + str(capital_words) + ',' + str(lower_words) + ')'
                my_db.exec_query(query)
                my_db.conn.commit()
            except sqlite3.OperationalError as e:
                logging.error(e)
                sys.exit(e)

            # create table for each book and fill in it
            try:
                query = 'CREATE TABLE IF NOT EXISTS "' + title + '"(word TEXT,count_words INTEGER,count_uppercase ' \
                                                                 'INTEGER) '
                my_db.exec_query(query)
                word_list = Counter.word_frequency(fb2_word_list)
                upper_word_list = Counter.upper_word_frequency(fb2_word_list)
                for word in word_list:
                    query = 'INSERT INTO "' + title + '" (word, count_words) ' \
                                                      'VALUES("' + word + '" , ' + str(word_list[word]) + ')'
                    my_db.exec_query(query)
                for upper_word in upper_word_list:
                    query = 'UPDATE "' + title + '" SET count_uppercase = ' + str(upper_word_list[upper_word]) + \
                            ' WHERE upper(word) = "' + upper_word.lower() + '";'
                    my_db.exec_query(query)
                my_db.conn.commit()
            except sqlite3.OperationalError as e:
                logging.error(e)
                sys.exit(e)