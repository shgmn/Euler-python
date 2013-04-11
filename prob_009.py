#! /usr/bin/python
# -*- coding:utf-8 -*-
import math

def pythagoras(num):
    for a in xrange(1, num / 3):
        for b in xrange(a + 1, num):
            c = num - a - b
            if a * a + b * b == c * c:
                return a * b * c

def main():
    print pythagoras(1000)

if __name__ == '__main__':
    main()