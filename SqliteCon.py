import sqlite3


class SqliteCon:
    def __init__(self):
        self.conn = sqlite3.connect('fb2_analytics.sqlite')
        self.cursor = self.conn.cursor()
        self.exec_query("CREATE TABLE  IF NOT EXISTS text_info ("
                        "book_name TEXT NOT NULL,"
                        "number_of_paragraph INTEGER,"
                        "number_of_words INTEGER,"
                        "number_of_letters INTEGER,"
                        "words_with_capital_letters INTEGER,"
                        "words_in_lowercase INTEGER);")

    def exec_query(self, query):
        cur = self.cursor.execute(query)
        return cur
