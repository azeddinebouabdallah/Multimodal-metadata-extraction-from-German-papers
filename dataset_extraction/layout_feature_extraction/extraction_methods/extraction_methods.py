import re
from dateutil.parser import parse

import pickle

def get_word_size(y1, y2):
    return int(y1 - y2)

def get_count_cap_letters(word):
    if len(word) == 0:
        return 0
    return sum(1 for c in word if c.isupper())/len(word)

def starts_cap_letter(word):
    return 1 if word[0].isupper() else 0

def get_word_length(word):
    return len(word)

def get_count_digits(word):
    return len(re.sub("[^0-9]", "", word))

def get_count_slash(word):
    return len(re.findall('/', word))

def get_count_com(word):
    return len(re.findall(':', word))

def contains_alt(word):
    return 1 if len(re.findall('@', word)) > 0 else 0

def isYear(word):
    # From 1000 - 2999, and the word should contain only the year
    r = re.findall(r'[1-2][0-9]{3}', word)
    if len(r) > 0 and len(r) < 2 and len(word) == len(r[0]):
        return 1
    else:
        return 0

def isEmail(word):
    r = re.findall(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', word)
    
    return 1 if len(r)>0 else 0

def isLink(word):
    r = re.findall(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', word)
    return 1 if len(r)>0 else 0

# Should update this to support german language
def isDate(word):
    try: 
        parse(word, False)
        return 1
    except ValueError:
        return 0

def get_horizontal_space(previous_right, current_left):
    # Int because we are not interested in the exact position.
    return int(current_left - previous_right) 