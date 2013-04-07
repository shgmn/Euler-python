#! /usr/bin/python
# -*- coding:utf-8 -*-

def fib(a, b, limit):
    if b > limit:
        return a
    if a % 2 == 0:
        return a + fib(b, a + b, limit)
    return fib(b, a + b, limit)

def main():
    print fib(1, 1, 4000000)

if __name__ == '__main__':
    main()