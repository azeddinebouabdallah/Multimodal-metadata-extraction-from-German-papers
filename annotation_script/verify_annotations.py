#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage: python verify_annotations.py path/file/to_verify.csv

output: print labels for each word
"""
import sys
from termcolor import colored


def get_label(label_str):
    clase = 'undefined'
    label_int = 20
    
    try:
        label_int = int(label_str)
    except ValueError:
        clase = 'undefined2'
        
    if label_int == 1:
        clase = colored("author", 'green')
    elif label_int == 2:
        clase = colored("title", 'yellow')
    elif label_int == 3:
        clase = colored("affiliation", attrs=['bold'])
    elif label_int == 4:
        clase = "date"
    elif label_int == 5:
        clase = colored("journal", 'cyan')
    elif label_int == 6:
        clase = "address"
    elif label_int == 7:
        clase = colored("abstract", 'magenta')
    elif label_int == 8:
        clase = "doi"
    elif label_int == 9:
        clase = "email"
    elif label_int == 10:
        clase = colored("other", 'red')
    
    return clase


input_file = sys.argv[1]
#output_file = input_file.split('.')[-2]+"_annotated."+input_file.split('.')[-1]


searchfile = open(input_file, "r")
#output_file = open(output_file, 'w')

for line in searchfile:
    line = line.replace(',",', '",')
    line_array = line.split(',')
    size = len(line_array)
    #number = line_array[1]
    word = line_array[0]
    label = line_array[-1]
    label_txt = get_label(label)
    
    #print("{}-[{}] - {}: {}".format(number, size, word, label_txt)) #prints current line number and  word to label 
    print("[{}] - {}: {}".format(size, word, label_txt))
    #label = input("label?: ") or "10" #defaults with label 10 when no input (just hit enter)
    
    #output_file.write("{},{}\n".format(line.strip(),label))
    
#output_file.close()
searchfile.close()


