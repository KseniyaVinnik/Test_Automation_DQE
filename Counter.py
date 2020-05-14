
class Counter:
    words = 0
    letters = 0
    cap_words = 0
    lower_words = 0
    counts = dict()
    count_uppers = dict()

    def __init__(self, word_list):
        self.word_list = word_list

    def count_letters(self):
        words = self
        for word in words:
            Counter.letters += len(word)
        return Counter.letters

    def count_words(self):
        words = self
        Counter.words = len(words)
        return Counter.words

    def count_low_words(self):
        words = self
        for word in words:
            if word.islower():
                Counter.lower_words += 1
        return Counter.lower_words

    def count_cap_words(self):
        words = self
        for word in words:
            if word[0].isupper():
                Counter.cap_words += 1
        return Counter.cap_words

    def word_frequency(self):
        words = self
        for word in words:
            if word.lower() in Counter.counts:
                Counter.counts[word.lower()] += 1
            else:
                Counter.counts[word.lower()] = 1
        return Counter.counts

    def upper_word_frequency(self):
        words = self
        for word in words:
            if word[0].isupper():
                if word in Counter.count_uppers:
                    Counter.count_uppers[word] += 1
                else:
                    Counter.count_uppers[word] = 1
        return Counter.count_uppers
