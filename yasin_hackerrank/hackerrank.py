# 1 -sWAP cASE: https://www.hackerrank.com/challenges/swap-case/problem
# 
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description
#
def swap_case(s):
   return s.swapcase()
#**********************************************************************************
# 2 -String Split and Join: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# Example:

# a = "this is a string"
# a = a.split(" ") # a is converted to a list of strings. 
# print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:
# 
# a = "-".join(a)
# print a
# this-is-a-string 
# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. 
def split_and_join(line):
    text = line.split(" ")
    return "-".join(text)
#******************************************************************************************
# 3- Mutations: https://www.hackerrank.com/challenges/python-mutations/problem
# Example
# 
# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra
def mutate_string(string, position, character):
    metin = string
    l = list(metin)
    l[position] =character
    return "".join(l)
# *********************************************************************************************
# 4- Text Wrap: https://www.hackerrank.com/challenges/text-wrap/problem    

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    text = textwrap.fill(string, max_width)
    
    return text