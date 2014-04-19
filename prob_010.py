#! /usr/bin/python
# -*- coding:utf-8 -*-
import math


def eratosthenes(num):
    if num == 1:
        return []
    flag_list = [True] * num
    limit = int(math.sqrt(num))
    primes = eratosthenes(limit)
    for x in primes:
        for i in xrange(x + x, num, x):
            flag_list[i] = False
    prime_list = [2]
    for i in xrange(3, num, 2):
        if flag_list[i]:
            prime_list.insert(-1, i)
    return prime_list


def sumOfPrimes(num):
    sum = 0
    prime_list = eratosthenes(num)
    for x in prime_list:
        sum += x
    return sum


def main():
    print sumOfPrimes(2000000)

if __name__ == '__main__':
    main()
