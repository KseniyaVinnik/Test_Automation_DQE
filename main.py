import sys

from FolderCheck import *
from SqliteCon import *
from Fb2File import *
import logging

logging.basicConfig(filename='log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    level=logging.INFO)
logging.info("Analysing FB2 file started")

try:
    directory_name = sys.argv[1]
    check_input = FolderCheck(directory_name)
    # check the folder. If it includes "wrong" files these files are moved to "incorrect_input". The function returns the list of fb2 files
    file_list = check_input.remove_files()
except FileNotFoundError as e:
    logging.error(e)
except IndexError as e:
    logging.error(e)

try:
    my_db = SqliteCon()
except sqlite3.OperationalError as e:
    logging.error(e)

# read and count all the necessary values for each file

for file in file_list:
    get_path = check_input.path + file
    f = Fb2File(get_path)
    title = Fb2File.get_title(f)
    paragraphs = Fb2File.count_paragraphs(f)
    words = Fb2File.count_words(f)
    letters = Fb2File.count_letters(f)
    capital_words = Fb2File.count_cap_words(f)
    lower_words = Fb2File.count_low_words(f)

    try:
        # connect to db and fill in the table "text_info". The table is created with connection to db
        query = 'INSERT INTO text_info(book_name, number_of_paragraph, number_of_words,' \
                ' number_of_letters, words_with_capital_letters, words_in_lowercase) ' \
                'VALUES(\'' + title + '\',' + str(paragraphs) + ',' + str(words) + ',' \
                + str(letters) + ',' + str(capital_words) + ',' + str(lower_words) + ')'
        my_db.exec_query(query)
        my_db.conn.commit()
    except sqlite3.OperationalError as e:
        logging.error(e)

    # create table for each book and fill in it
    try:
        query = 'CREATE TABLE IF NOT EXISTS "' + title + '"(word TEXT,count_words INTEGER,count_uppercase INTEGER)'
        my_db.exec_query(query)
        word_list = Fb2File.word_frequency(f)
        upper_word_list = Fb2File.upper_word_frequency(f)
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

logging.info("Analysing FB2 file finished")
