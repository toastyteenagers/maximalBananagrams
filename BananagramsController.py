import threading
from concurrent.futures import ThreadPoolExecutor

from WordDict import WordDict
from BananagramGrid import BananagramGrid
import random
class BanagramsController:
    def __init__(self,width,height):
        self.__word_dict = WordDict()
        self.__bananagram_grid = BananagramGrid(width,height)
        self.__width = width
        self.__height = height

    def is_board_valid(self):
        col_words = [self.__bananagram_grid.get_col_word(col) for col in range(self.__width)]
        row_words = [self.__bananagram_grid.get_row_word(row) for row in range(self.__height)]
        for col_word in col_words:
            if not self.__word_dict.is_word_valid(col_word):
                #print(f"invalid word: '{col_word}'")
                return False
        for row_word in row_words:
            if not self.__word_dict.is_word_valid(row_word):
                #dprint(f"invalid word: '{row_word}'")
                return False
        return True

    def get_maximal_bananagrams(self):
        maximal_width_words = self.__word_dict.get_words_of_len(self.__width)

        # A lock to ensure thread-safe access to self.__bananagram_grid
        lock = threading.Lock()

        def add_word_to_row(row):
            word = random.choice(maximal_width_words)
            with lock:
                self.__bananagram_grid.add_word_row(word, row)

        # Use ThreadPoolExecutor to run add_word_to_row concurrently
        with ThreadPoolExecutor(max_workers=self.__height) as executor:
            while not self.is_board_valid():
                # Submit tasks to thread pool for each row
                futures = [executor.submit(add_word_to_row, row) for row in range(self.__height)]
                # Wait for all futures to complete
                for future in futures:
                    future.result()

        print(self.__bananagram_grid)
