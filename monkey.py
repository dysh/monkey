#!/usr/bin/python

import sys
import random
from random import randint
import string
import matplotlib.pyplot as plt
#import numpy

def chargenerator():
    return random.choice(string.letters)

def joinList(lst):
    res=''
    l=len(lst)
    for i in range(l):
        res = res+str(lst[i])
    return res

def str2List(st):
    res=list()
    l=len(st)
    for i in range(l):
        res.append(st[i])
    return res

def cmpLists(list1,list2):
    l1=len(list1)
    l2=len(list2)
    l=l1
    if l2<l1:
        l=l2
    match=0
    for i in range(l):
        if list1[i] == list2[i]:
            match +=1
    return match
    
def mutate(list1,list2):
    x = random.randint(0,len(list1)-1)
    if list1[x] != list2[x]:
        list2[x]=random.choice(string.letters)
    return list2

def mutate_i(list1,list2):
    x = random.randint(0,len(list1)-1)
    if list1[x] != list2[x]:
        list2[x]=random.choice(string.letters)
    else:
    	if(random.uniform(0,1)<.002):
    		list2[x]=random.choice(string.letters)
    		##print "bum!"
    return list2

def main():
    dlina=len(sys.argv[1])
    target=str2List(sys.argv[1])
    dist=list()
    print "Dtsrting first round:"
    for j in range(10000):
        starter=list()
        if(j % 100 == 0):
        	print str(j)
        for i in range(dlina):
            starter.append('a')
            starter[i]=chargenerator()
        mud=cmpLists(target,starter)
        
    
        step=0;
        mud=0;
        while mud<dlina:
            step +=1
            starter=mutate(target,starter)
            mud=cmpLists(target,starter)
        dist.append(step)
    
    dist1=list()
    for j in range(10000):
        starter=list()
        if(j % 100 == 0):
        	print str(j)
        for i in range(dlina):
            starter.append('a')
            starter[i]=chargenerator()
        mud=cmpLists(target,starter)
        
    
        step=0;
        mud=0;
        while mud<dlina:
            step +=1
            starter=mutate_i(target,starter)
            mud=cmpLists(target,starter)
        
    
    ##print str(step)+' '+joinList(starter)
    plt.hist([dist,dist1],50)
    plt.title("The target word was "+joinList(target))
    plt.grid(True)
    plt.xlabel("mutation steps")
    plt.ylabel("frequency")
    plt.show()
    

if __name__=='__main__':
    main()

