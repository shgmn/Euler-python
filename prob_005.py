#! /usr/bin/python
# -*- coding:utf-8 -*-

def lcm(num):
    value = 1
    for x in xrange(1, num):
        pow_num = 1
        if value % x == 0:
            continue
        while pow_num * x <= num:
            pow_num = pow_num * x
        value = value * pow_num
    return value

def main():
    print lcm(20)

if __name__ == '__main__':
    main()