#!/usr/bin/env python

def fib(num):
    if num <= 1:
        print(num)
        return num
    else:
        print(num)
        return fib(num -2) + fib(num - 1)

if __name__ == "__main__":
    print(fib(5))
