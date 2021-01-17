import pandas as pd
import numpy as np
import os
import xml.etree.ElementTree as ET
import pickle

from extraction_methods.extraction_methods import *

words_list = []
documentName = ''
vectors = []


file = ET.parse('test.cermstr')
root = file.getroot()

for element in root:
    if (element.tag == 'Page'):
        # Feature vector for the doc
        document_vector = []
        

        for zone in element:
            if zone.tag == 'Zone':
                for line in zone:
                    if line.tag == 'Line':
                        for e in line:
                            if e.tag == 'LineID': # Get the number of line.
                                line_num = int(e.attrib['Value'])
                            for word in e.iter('Word'):

                                word_vector = []

                                actual_word = '' # new word
                                # Initializing features
                                cap_letters = 0
                                starts_cap = 0
                                line_num = 0
                                len_word = 0
                                count_num = 0
                                count_slash = 0 # /
                                count_com = 0 # :
                                is_alt = 0 # @ 
                                is_email = 0 
                                is_link = 0 
                                is_year = 0
                                is_date = 0
                                actual_word = ''
                                font_size = 0
                                for we in word: # we: Word element
                                    if we.tag == 'WordCorners': # get position
                                        # get the top and bottom position then substract
                                        y2 = float(we[0].attrib['y'])
                                        y1 = float(we[2].attrib['y'])
                                        font_size = get_word_size(y1, y2)
                                    if we.tag == 'Character':                                        
                                        actual_word += we[4].attrib['Value']
                
                                # Clean the word
                                actual_word = actual_word.replace('(', '').replace('.', '').replace('„', '').replace(')', '').replace('“', '')

                                words_list.append(actual_word)
                                cap_letters = get_count_cap_letters(actual_word)
                                starts_cap = starts_cap_letter(actual_word)
                                len_word = get_word_length(actual_word)
                                count_num = get_count_digits(actual_word)
                                count_slash = get_count_slash(actual_word)
                                count_com = get_count_com(actual_word)
                                is_alt = contains_alt(actual_word)
                                is_email = isEmail(actual_word)
                                is_link = isLink(actual_word)
                                is_year = isYear(actual_word)
                                is_date = isDate(actual_word)
                                word_vector = [
                                    cap_letters, starts_cap, line_num, len_word,
                                    count_num, count_slash, count_com, 
                                    is_alt, is_email, is_link, is_year, 
                                    is_date, font_size
                                ]

                                document_vector.append(word_vector)
                                

        with open('feature_vectors/document'+str(1)+'.pickle', 'wb') as handle:
            pickle.dump(document_vector, handle, protocol=pickle.HIGHEST_PROTOCOL)

        df = pd.DataFrame(document_vector, columns=['Cap letters', 'Starts cap', 'Line number','Len Word', 'Count num', 'Count slash', 'Count com', 'Is Alt'
        ,'Is email', 'Is link', 'Is Year', 'Is date', 'Font size'])
        df.insert(0, 'Word', words_list, True)
        df.to_csv('./feature_vectors/document'+str(1)+'vectors.csv')


