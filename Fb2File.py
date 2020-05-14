import re
from xml.dom import minidom


class Fb2File:

    word_list = []

    def __init__(self, path):
        self.path = path
        self.book = minidom.parse(self.path)
        self.root = self.book.documentElement

    def get_title(self):
        get_book_title = self.book.getElementsByTagName('book-title')[0]
        title = get_book_title.firstChild.data
        return title

    def count_paragraphs(self):
        paragraphs = self.book.getElementsByTagName('p')
        number_of_par = (len(paragraphs))
        return number_of_par

    def get_words(self, n=None):
        if n is None:
            for node in self.root.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            Fb2File.word_list.append(word)
                self.get_words(node)
        else:
            for node in n.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            Fb2File.word_list.append(word)
                self.get_words(node)
        return Fb2File.word_list
