#-*-coding:utf-8-*-
"""
Created on Thu Aug 20
@author:victor
"""
count=0
def hanoi(n,A,B,C):
    global count
    if n==1:
        print('Move',n,'from',A,'to',C)
        count+=1
    else:
        hanoi(n-1,A,C,B)
        print('Move',n,'from',A,'to',C)
        count+= 1
        hanoi(n-1,B,A,C)

hanoi(20,'left','Mid','right')
print("step=",count)
