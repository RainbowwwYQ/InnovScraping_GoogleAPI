#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:12:32 2020

@author: mayhe
"""
import pandas as pd

df = pd.read_csv("GoogleAPI_fuzzy.csv", encoding= 'unicode_escape')

# pick up the perfect URLs

def choose_toplink(var, level):
    
    choose = f'fuzzy_ratio_link({var})'
    choose2 = f'fuzzy_ratio_title({var})'
    print(f'You choose the {var} ratio of fuzzy matching for URLs!')
    
    global TopLinks
    TopLinks = pd.DataFrame({'Company': df["Company"],
                           'DisplayLinks': df["new_links"],
                           'Title': df["Title"],
                           choose: df[choose],
                           choose2: df[choose2]
                           })
    
    index = TopLinks.columns.get_loc(choose)
    index2 = TopLinks.columns.get_loc(choose2)
    for i in range(len(TopLinks)):
        temp = int(TopLinks.iat[i,index])
        temp2 = int(TopLinks.iat[i,index2])
        if (temp <= int(level)) or (temp2 <= int(level)):
            TopLinks.iloc[i,index] = None

    TopLinks.dropna(axis=0, how='any', inplace=True)
    TopLinks.drop_duplicates('DisplayLinks','first',inplace = True)
    
    x = len(TopLinks)
    print(f'We got {x} perfect-matching URLs!')
 
    
# choose the type of the fuzzy score we want        
# you can choose: 
#(definitions see: https://www.datacamp.com/community/tutorials/fuzzy-string-python)
#1) simple ratio -> enter "simple"
#2) partial ratio -> enter "partial"
#3) token sort ratio -> enter "token_sort"
#4) token set ratio -> enter "token_set"
    
choose_toplink("token_set", 70) # normally, 70 is a perfect matching!
TopLinks.to_csv("TopLinks.csv", index = False, sep=',')

# pick up the good-matching URLs

def choose_goodlink(var, level):
    
    choose = f'fuzzy_ratio_link({var})'
    choose2 = f'fuzzy_ratio_title({var})'
    print(f'You choose the {var} ratio of fuzzy matching for URLs!')
    
    global GoodLinks
    GoodLinks = pd.DataFrame({'Company': df["Company"],
                           'DisplayLinks': df["new_links"],
                           'Title': df["Title"],
                           choose: df[choose],
                           choose2: df[choose2]
                           })
    
    index = GoodLinks.columns.get_loc(choose)
    index2 = GoodLinks.columns.get_loc(choose2)
    index3 = GoodLinks.columns.get_loc('DisplayLinks')
    
    remove_toplevel = TopLinks['DisplayLinks'].drop_duplicates().values.tolist()
    
    for i in range(len(GoodLinks)):
        temp = GoodLinks.iat[i,index3]
        for item in remove_toplevel:
            if temp == item:
                GoodLinks.iat[i, index3] = None
                
    GoodLinks.dropna(axis=0, how='any', inplace=True)  
    
    for i in range(len(GoodLinks)):
        temp = int(GoodLinks.iat[i,index])
        temp2 = int(GoodLinks.iat[i,index2])
        if (temp <= int(level)) or (temp2 <= 90):
            GoodLinks.iloc[i,index] = None

    GoodLinks.dropna(axis=0, how='any', inplace=True)
    GoodLinks.drop_duplicates('DisplayLinks','first',inplace = True)
    
    x = len(GoodLinks)
    print(f'We got {x} good-matching URLs!')
 
    
# choose the type of the fuzzy score we want        
# you can choose: 
#(definitions see: https://www.datacamp.com/community/tutorials/fuzzy-string-python)
#1) simple ratio -> enter "simple"
#2) partial ratio -> enter "partial"
#3) token sort ratio -> enter "token_sort"
#4) token set ratio -> enter "token_set"
    
choose_goodlink("token_set", 40) # normally, 40 is a good matching!
GoodLinks.to_csv("GoodLinks.csv", index = False, sep=',')