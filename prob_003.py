#! /usr/bin/python
# -*- coding:utf-8 -*-

def maxPrimeFactor(num):
    i = 2
    while i * i < num:
        while num % i == 0:
             num = num / i
        i = i + 1
    return num

def main():
    print maxPrimeFactor(600851475143)

if __name__ == '__main__':
    main()
