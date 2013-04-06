#! /usr/bin/python
# -*- coding:utf-8 -*-

def main():
    sum = 0
    for i in xrange(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    print sum

if __name__ == '__main__':
    main()