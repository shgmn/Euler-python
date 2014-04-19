#! /usr/bin/python
# -*- coding:utf-8 -*-
import math


def getTriangleNumber(devs):
    i = 1
    triangleNum = 0
    devisors = 0
    while devisors <= devs:
        triangleNum = triangleNum + i
        i = i + 1
        devisors = 0
        for x in xrange(1, int(math.sqrt(triangleNum))):
            if triangleNum % x == 0:
                if x * x == triangleNum:
                    devisors = devisors + 1
                else:
                    devisors = devisors + 2
    return triangleNum


def main():
    print getTriangleNumber(500)

if __name__ == '__main__':
    main()
