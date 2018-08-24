# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:51:58 2018

@author: hp
"""

formatter=" {} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True,False,True,False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("try your", "own text here", "maybe a poem",
 "or a song about fear"                      ))
#above first four printing part did one thing only and what is that?
#that is print(caller name.format(called name or anything))
