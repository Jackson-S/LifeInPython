#!/usr/bin/env python3
# coding=UTF-8
from random import randint
from copy import deepcopy
from time import sleep, time
from sys import stdout, argv

def Main():
    '''
    Life in Python: An implementation of Conway's Game of Life in Python 3,
    with compatability for python 2.x (with some strange side effects).
    Created by Jackson Sommerich, with additional credit to external libraries
    I have used.
    '''
    speed = 0.2 # Time between frame updates, 0 for instant (benchmark mode).
    # sizes: x,y Default is 80x24 (OS X standard terminal size).
    columns = 80
    rows = 24
    starttime = time() # get the start time of the program, for calculations later.
    title_text = "Life in Python: Jackson Sommerich 2016" # title text
    desired_generation = generations = 0 # sets default desired gen, and init's gen counter
    if len(argv) > 2 and len(argv) < 5:
        try:
            rows = int(argv[2])
            columns = int(argv[1])
        except:
            usage()
    if len(argv) == 4:
        try:
            desired_generation = int(argv[3])
            from tqdm import tqdm
        except ImportError:
            print("Requires tqdm library, run: python3 -m pip install tqdm")
            quit()
        except: usage()
    old_display = curr_display = [] # initialise display buffers
    # set console size and title text, and flush write cache:
    stdout.write("\x1b[8;{};{}t\x1b]2;{}\x07".format(rows, columns, title_text))
    stdout.flush()
    # creates nested arrays, to use as display buffers, necessitates a deep copy
    # in order to move curr_display to old_display without linking just references
    # also fills current array with random zeroes and ones
    for row in range(rows):
        curr_display.append([])
        for col in range(columns):
            curr_display[row].append(randint(0,1))
    if desired_generation != 0: progress = tqdm(total=desired_generation) # init tqdm if req'd
    while True:
        if desired_generation != 0: progress.update(1) # updates tqdm counter
        generations += 1
        #randomly add a living square
        if randint(0,1) == 1:
            for x in range(0,randint(1,10)):
                curr_display[randint(0, rows - 1)][randint(0, columns - 1)] = 1
        # copies current display buffer to another buffer for updating
        old_display = deepcopy(curr_display)
        for count_y, y in enumerate(curr_display):
            for count_x, x in enumerate(y):
                # adds current cell's neighbours to an array
                if count_x > 1 and count_y > 1 and count_x < columns - 1 and count_y < rows - 1:
                    neigbours = [old_display[count_y - 1][count_x - 1],
                        old_display[count_y - 1][count_x],
                        old_display[count_y - 1][count_x + 1],
                        old_display[count_y][count_x - 1],
                        old_display[count_y][count_x + 1],
                        old_display[count_y + 1][count_x - 1],
                        old_display[count_y + 1][count_x],
                        old_display[count_y + 1][count_x + 1]]
                else:
                    # edge case (heh) for cells lying on the border
                    neigbours = [0,0,0,0,0,0,0,0]
                neigbourcount = sum(neigbours)
                if x == 1:
                    if neigbourcount < 2 or neigbourcount > 3:
                        curr_display[count_y][count_x] = 0
                    if neigbourcount == 2 or neigbourcount == 3:
                        curr_display[count_y][count_x] = 1
                if x == 0:
                    if neigbourcount == 3:
                        curr_display[count_y][count_x] = 1
                    else:
                        curr_display[count_y][count_x] = 0
        # case if not updating to a certain point:
        if desired_generation == 0:
            update(columns, rows, curr_display, title_text, starttime, generations)
            sleep(speed)
        # case if updating to a certain point, however that point hasn't been reached
        elif desired_generation > 0 and generations != desired_generation: continue
        else:
            progress.close()
            update(columns, rows, curr_display, title_text, starttime, generations)
            quit()

def update(columns, rows, curr_display, title_text, starttime, generations):
    ''' Generates borders and outputs to screen, return True if successful'''
    try:
        title = "{}{}{}".format("#" * (columns - (len(title_text) + 5)), title_text, "#" * 5)
        endnote = " Gen {}, {} seconds ".format(generations, round(time() - starttime, 2))
        endnote = ("{}{}{}".format("#" * 3, endnote, "#" * (columns - len(endnote) - 3)))
        for row in range(rows):
            for col in range(columns):
                if col == 0 or col == columns - 1:
                    stdout.write("#")
                elif (row == 0):
                    stdout.write(title[col])
                elif (row == rows - 1):
                    stdout.write(endnote[col])
                elif curr_display[row][col] == 1:
                    stdout.write("█")
                else:
                    stdout.write(" ")
        stdout.flush()
    except:
        return False
    return True

def usage():
    ''' Defines usage of program'''
    print("life.py [columns] [rows] [generation]")
    quit()

if __name__ == "__main__":
    Main()
