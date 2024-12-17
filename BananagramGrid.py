class BananagramGrid:
    BLANK_SPACE = ' '
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__grid = self.__build_grid(width, height)

    def __str__(self):
        ret_string = ''
        for row in self.__grid:
            tmp_string = ''
            for col in row:
                tmp_string += str(col)
            ret_string += tmp_string + '\n'
        return ret_string

    def add_letter(self, letter, row, col):
        if row > self.__height or col > self.__width:
            print(f"bad insert at: {row}, {col}")
            return
        self.__grid[row][col] = letter

    def add_word_row(self, word, row):
        if not (len(word) == self.__width):
            print(f"word of invalid dimension! :grid  width:{self.__width}, word width: {len(word)}")
            return

        if row > self.__width:
            print(f"bad insert: row is greater than height of grid!")
            return

        for index,letter in enumerate(word):
            self.add_letter(letter, row, index)


    def add_word_col(self, word, col):
        if not (len(word) == self.__height):
            print(f"word of invalid dimension! :grid  height:{self.__height}, word height: {len(word)}")
            return

        if col > self.__width:
            print(f"bad insert: col is greater than width of grid!")
            return

        for index, letter in enumerate(word):
            self.add_letter(letter, index, col)


    def get_col_word(self, col_idx):
        word = ''
        for y in range(self.__height):
            word += self.__grid[y][col_idx]
        return word

    def get_row_word(self, row_idx):
        return ''.join(self.__grid[row_idx])

    def __build_grid(self, width, height):
        grid = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(self.BLANK_SPACE)
            grid.append(row)
        return grid