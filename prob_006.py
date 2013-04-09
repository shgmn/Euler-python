#! /usr/bin/python
# -*- coding:utf-8 -*-

def squareOfSum(num):
    value = 0
    for x in xrange(1, num + 1):
        value = value + x * x
    return value

def sumOfSquare(num):
    value = 0
    for x in xrange(1, num + 1):
        value = value + x
    return value * value

def main():
    print sumOfSquare(100) - squareOfSum(100)

if __name__ == '__main__':
    main()