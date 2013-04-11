#! /usr/bin/python
# -*- coding:utf-8 -*-
import math

def prime(num):
    prime_list = [2]
    value = 3
    while len(prime_list) < num:
        limit = math.sqrt(value)
        for x in prime_list:
            if x > limit:
                prime_list.append(value)
                break
            if value % x == 0:
                break
        value = value + 2
    return prime_list[-1]

def main():
    print prime(10001)

if __name__ == '__main__':
    main()