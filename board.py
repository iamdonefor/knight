#!/usr/bin/env python

import copy

KMOVES = [ (-1, 2), (-1, -2),
           (1, 2), (1, -2),
           (-2, 1), (-2, -1),
           (2, 1), (2, -1)]

class Board(object):
    def __init__(self, vector=None, current=(0,0), size=5, step=1):
        self.current = current
        if vector is None:
            self.vector = [0] * pow(size, 2)
        else:
            self.vector = copy.copy(vector)

        self.size = size
        self.step = step

    def __getitem__(self, x):
        if type(x) == int:
            return self.vector[x]
        else:
            assert len(x) == 2
            return self.vector[self.size*x[0] + x[1]]

    def __setitem__(self, x, y):
        if type(x) == int:
            self.vector[x] = y
        else:
            assert len(x) == 2
            self.vector[self.size*x[0] + x[1]] = y

    def reachables(self):
        return sum(1 for i in self.moves())

    def moves(self):
        for dx,dy in KMOVES:
            x,y = self.current

            nx = x+dx
            ny = y+dy

            if (0 <= nx < self.size) and \
               (0 <= ny < self.size) and \
               self[nx, ny] == 0:
                yield (nx, ny)
            else:
                continue

    def make_move(self, move):
        b = Board(self.vector, move, self.size, self.step)

        b[self.current] = self.step
        b.step += 1

        return b

    def distance(self, i1, i2):
        if i1 == pow(self.size, 2):
            p1 = self[self.current]
        else:
            p1 = self.vector.index(i1)
        if i2 == pow(self.size, 2):
            p2 = self[self.current]
        else:
            p2 = self.vector.index(i2)

        x1 = p1 % self.size
        y1 = p1 // self.size

        x2 = p2 % self.size
        y2 = p2 // self.size

        return (x2-x1, y2-y1)

    def verify(self):
        for i in range(2, pow(self.size, 2)):
            assert i in self.vector
            assert self.distance(i-1,i) in KMOVES
        if self.distance(pow(self.size, 2), 1) in KMOVES:
            print "HAMILTON"
        print "verified OK"


    def show(self):
        print '+' + '----+' * self.size
        for i in range(self.size):
            s = "|"
            for j in range(self.size):
                if (i,j) == self.current:
                    value = '**'
                else:
                    value =  "%02d" % self[i,j]

                s += " %s |" % value
            print s
            if i<self.size-1:
                print '+' + '----+' * self.size
        print '+' + '----+' * self.size


if __name__ == '__main__':
    b = Board(size=6)
    b.show()

    b[5] = 34
    b[1,1]= 42
    b.show()

    print b.reachables()

    for move in b.moves():
        print move
        
