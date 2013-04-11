#! /usr/bin/python
# -*- coding:utf-8 -*-

def prime(num):
    prime_list = [2]
    value = 3
    while len(prime_list) < num:
        flag = False
        for x in prime_list:
            if value % x == 0:
                flag = True
                break
        if not flag:
            prime_list.append(value)
        value = value + 2
    return prime_list[-1]

def main():
    print prime(10001)

if __name__ == '__main__':
    main()