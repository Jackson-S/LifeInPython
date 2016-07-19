from random import randint


class TGOLLogic(object):
    """Logic for Conway's Game Of Life, returns nested lists with 1 and 0 as values"""
    def __init__(self, x_size, y_size):
        self.x_size, self.y_size = x_size, y_size
        self.array = [[1 % randint(1, 3) for _ in range(x_size)] for _ in range(y_size)]
        self.new_array = [[0 for _ in range(x_size)] for _ in range(y_size)]

    def return_new_array(self):
        for x in range(self.y_size):
            for y in range(self.x_size):
                try:
                    value = sum([self.array[x - 1][y - 1],
                                self.array[x - 1][y],
                                self.array[x - 1][y + 1],
                                self.array[x][y - 1],
                                self.array[x][y + 1],
                                self.array[x + 1][y - 1],
                                self.array[x + 1][y],
                                self.array[x + 1][y + 1]])
                except IndexError:
                    value = 0
                if (value == 2 and self.array[x][y]) or value == 3:
                    self.new_array[x][y] = 1
                else:
                    self.new_array[x][y] = 0
        self._completed()
        return self.array

    def _completed(self):
        self.array = self.new_array
        self.new_array = [[0] * self.x_size for _ in range(self.y_size)]
