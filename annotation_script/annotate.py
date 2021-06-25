#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage: python annotate.py path/file_to_annotate.csv

output: annotated file in same directory with "_annotated" suffix
"""
import sys
from termcolor import colored

input_file = sys.argv[1]
output_file = input_file.split('.')[-2]+"_annotated."+input_file.split('.')[-1]


searchfile = open(input_file, "r")
output_file = open(output_file, 'w')

number = 0
for line in searchfile:
    line_array = line.split(',')
    #number = line_array[1]
    number += 1
    word = colored(line_array[0], 'yellow')
    
    print("{} - {}".format(number, word)) #prints current line number and  word to label 
    label = input("label?: ") or "10" #defaults with label 10 when no input (just hit enter)
    
    output_file.write("{},{}\n".format(line.strip(),label))
    
output_file.close()
searchfile.close()


