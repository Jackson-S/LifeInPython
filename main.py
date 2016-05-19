#!/usr/bin/env pypy
# coding=UTF-8
from random import randint
from sys import stdout, argv
from threading import Timer
'''Life in Python: An implementation of Conway's Game of Life in Python'''

def disp_fps():
    global ticks, timer
    stdout.write("\x1b]2;{} fps\x07".format(ticks))
    stdout.flush()
    ticks = 0
    timer = Timer(1, disp_fps)
    timer.start()


def main():
    rows = args("rows")
    columns = args("cols")
    old_display = []
    curr_display = [[randint(0, 1) for x in range(columns)] for y in range(rows)]
    global ticks
    while True:
        ticks += 1
        old_display, curr_display = curr_display, new_screen(curr_display)


def new_screen(old):
    result = [[] for x in range(len(old))]
    for x, x_val in enumerate(old):
        for y, y_val in enumerate(x_val):
            try:
                same = True
                c = (old[x-1][y-1] + old[x-1][y] + old[x-1][y+1] +
                     x_val[y-1] + x_val[y+1] +
                     old[x+1][y-1] + old[x+1][y] + old[x+1][y+1])
            except IndexError:
                result[x].append(0)
                continue
            if c == 2:
                result[x].append(y_val)
                same = True
            elif c == 3:
                result[x].append(1)
                if y_val == 1:
                    same = True
            else:
                result[x].append(0)
                if y_val == 0:
                    same = True
            if same is False:
                if y_val == 1:
                    pass
                else:
                    pass
    return result


def usage(case=0):
    ''' Defines usage of program'''
    print("life.py [rows] [columns]")


def args(param):
    '''retrieves arguments from argv and performs error checking
       and conversion on returned values'''
    length = len(argv)
    if param == "cols" and length >= 3:
        return int(argv[2])
    elif param == "cols" and length <= 3:
        return 24
    if param == "rows" and length >= 3:
        return int(argv[1])
    elif param == "rows" and length <= 3:
        return 80


if __name__ == "__main__":
    ticks = timer = 0
    disp_fps()
    try:
        main()
    except KeyboardInterrupt:
        timer.cancel()
        quit()
