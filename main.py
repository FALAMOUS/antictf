#!/bin/env python3
#there'also an easter egg you can find
from random import randint
flag = 'some string of unique characters'
def roll(d,k,di,s=0):
    if di<0:
        return [s]
    res = []
    for rl in range(d[di]):
        tmps = s + k[di] * rl
        res += roll(d,k,di-1, tmps)
    return res
def mult(cont):
    res = 1
    for el in cont:
        res *=el
    return res
def main():
    n = randint(5,10)
    d = [randint(2,20) for i in range(n)]
    print(*d)
    k = [int(i,10) for i in input().split()]
    ch = input()
    pos = 0
    while pos < len(flag) and flag[pos]!=ch:
        pos+=1
    pos+=1
    if pos>=len(flag):
        print("kek")
        return
    rld = roll(d,k,n-1)
    rng = range(mult(d))
    if set(rld) == set(rng):
        print(flag[pos])
    else:
        print("not so random after all")
try:
    main()
except:
    print("wrong format")
