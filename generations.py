#!/usr/bin/env python

from board import Board
import copy
from random import choice, shuffle, randint
import sys

def next_generation(current):
    boards = []

    for board in current:
        for move in board.moves():
            new_board = board.make_move(move)
            boards.append(new_board)

    return boards

def find_best_board(boards):
    best_fields = 9
    best_boards = None

    for b in boards:
        reachables = b.reachables()
        if reachables < best_fields:
            best_boards = [b]
            best_fields = reachables
        if reachables == best_fields:
            best_boards.append(b)

    return choice(best_boards)

def find_ways_greedy(size, start=(0,0)):
    boards = [Board(size=size, current=start)]
   
    while True:
        new_boards = next_generation(boards)
        for b in boards:
            del b.vector
            del b
        boards = new_boards
        if not(boards):
            print "unable to compute"
            break
        example = choice(boards)
        print "step:", example.step, ", boards:", len(boards)
        example.show()
        if example.step == size*size:
            print "reached"
            break

def find_ways_varnsdorf(size, start=(0,0)):
    board = Board(size=size, current=start)

    while True:
        boards = next_generation([board])
        if not(boards):
            print "unable to compute"
            break

        board = find_best_board(boards)
        #print "step:", board.step, ", boards:", len(boards)
        if board.step == size*size:
            if size < 11: board.show()
            board.verify()
            print "reached"
            break


if __name__ == '__main__':
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    else:
        size = 5
    find_ways_varnsdorf(size, start=(randint(0,7), randint(0,7)))
#    find_ways_greedy(size)

