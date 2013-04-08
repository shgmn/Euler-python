#! /usr/bin/python
# -*- coding:utf-8 -*-

def kaibun():
    a = 999
    b = 999
    num = 0
    while a - num > 100:
        max = 0
        for i in xrange(0, num):
            result = (a - i) * (b - num + i)
            if (str(result) == str(result)[::-1]) :
                if max < result:
                    max = result
        if max != 0:
            return max
        num = num + 1

def main():
    print kaibun()

if __name__ == '__main__':
    main()