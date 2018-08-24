# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:09:40 2018

@author: hp
"""

types_of_people=10
x=f"there are {types_of_people} types_of_people"
binary="binary"
do_not="don't"
y=f"those who know {binary} and those who {do_not}"
print(x)
print(y)
print(f"i said {x}")
print(f"i also said that {y}")
hilarious= False
joke_evaluation="isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w="this is a left side of..."
e="a string with a right side"
print(w+e)
