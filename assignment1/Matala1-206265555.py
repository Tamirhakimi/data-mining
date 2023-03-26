# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:03:39 2023

@author: tamir
"""

## Q1
def my_func(x1,x2,x3):
    if type(x1) == int or type(x2) == int or type(x3) == int:
        return "Error: parameters should be float"
    if type(x1)!= float or type(x2) != float or type(x3) != float:
        return "None"
    if ZeroDivisionError:
        return "Not a number – denominator equals zero"
    else:
        P = ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
        return P
    
##Q2
def revword(word:str) :
    word = word[::-1].lower()
    return word

def countword():
    fn = open(fill)
    word = fn.readlines(1)[0].replace('/n', "")
    count = 1
    for line in fn.readlines()[1:]:
        words = line.split()
        for i in words:
            n=revword(n)
            if n == word:
                count += 1
    print(count) 
           
        