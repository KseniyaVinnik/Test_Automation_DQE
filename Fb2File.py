import re
from xml.dom import minidom

class Fb2File:
    words = 0
    letters = 0
    cap_words = 0
    lower_words = 0
    counts = dict()
    count_uppers = dict()

    def __init__(self, path):
        self.path = path
        self.book = minidom.parse(self.path)
        self.root = self.book.documentElement

    def get_title(self):
        get_booktitle = self.book.getElementsByTagName('book-title')[0]
        title = get_booktitle.firstChild.data
        return title

    def count_paragraphs(self):
        paragraphs = self.book.getElementsByTagName('p')
        number_of_par = (len(paragraphs))
        return number_of_par


    def count_words(self, n=None):
        if n is None:
            for node in self.root.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            Fb2File.words += 1
                self.count_words(node)
        else:
            for node in n.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            Fb2File.words += 1
                self.count_words(node)
        return Fb2File.words


    def count_letters(self, n=None):
        if n is None:
            for node in self.root.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+ ':
                        text = text.replace(char, '')
                    Fb2File.letters += len(text)
                self.count_letters(node)
        else:
            for node in n.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+ ':
                        text = text.replace(char, '')
                    Fb2File.letters += len(text)
                self.count_letters(node)
        return Fb2File.letters

    def count_cap_words(self, n=None):
        if n is None:
            for node in self.root.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            if word[0].isupper():
                                Fb2File.cap_words += 1
                self.count_cap_words(node)
        else:
            for node in n.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            if word[0].isupper():
                                Fb2File.cap_words += 1
                self.count_cap_words(node)
        return Fb2File.cap_words

    def count_low_words(self, n=None):
        if n is None:
            for node in self.root.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            if word.islower():
                                Fb2File.lower_words += 1
                self.count_low_words(node)
        else:
            for node in n.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            if word.islower():
                                Fb2File.lower_words += 1
                self.count_low_words(node)
        return Fb2File.lower_words

    def word_frequency(self, n=None):
        if n is None:
            for node in self.root.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            if word.lower() in Fb2File.counts:
                                Fb2File.counts[word.lower()] += 1
                            else:
                                Fb2File.counts[word.lower()] = 1
                self.word_frequency(node)
        else:
            for node in n.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            if word.lower() in Fb2File.counts:
                                Fb2File.counts[word.lower()] += 1
                            else:
                                Fb2File.counts[word.lower()] = 1
                self.word_frequency(node)
        return Fb2File.counts

    def upper_word_frequency(self, n=None):
        if n is None:
            for node in self.root.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            if word[0].isupper():
                                if word in Fb2File.count_uppers:
                                    Fb2File.count_uppers[word] += 1
                                else:
                                    Fb2File.count_uppers[word] = 1
                self.upper_word_frequency(node)
        else:
            for node in n.childNodes:
                if node.nodeType == node.TEXT_NODE:
                    text = node.data
                    words = text.split()
                    for word in words:
                        for char in '1234567890…№—!@#$%^&*()[]{};:,./<>?\|`~-=_+':
                            word = word.replace(char, '')
                        if re.compile("[А-Яа-я]+").match(word):
                            if word[0].isupper():
                                if word in Fb2File.count_uppers:
                                    Fb2File.count_uppers[word] += 1
                                else:
                                    Fb2File.count_uppers[word] = 1
                self.upper_word_frequency(node)
        return Fb2File.count_uppers
