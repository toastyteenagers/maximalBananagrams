class WordDict:
    FILENAME = "dictionary.txt"
    __wordDict = dict()

    def __init__(self):
        self.populate_dict()

    def populate_dict(self):
        with open(self.FILENAME, 'r') as f:
            for line in f:
                word = line.strip().lower()
                self.__wordDict[word] = len(word)

    def is_word_valid(self, word):
        return ' ' not in word and word in self.__wordDict

    def get_words_of_len(self,word_length):
        return list(set([a for a in self.__wordDict.keys() if len(a) == word_length]))

    def get_words_starting_with(self,starting_letters):
        return [word.startsWith(starting_letters) for word in self.__wordDict.keys()]

