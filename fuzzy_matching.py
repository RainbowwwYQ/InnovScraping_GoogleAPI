#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:32:51 2020

@author: mayhe
"""
import pandas as pd
from fuzzywuzzy import fuzz

df = pd.read_csv("GoogleAPI_cleaned.csv", encoding= 'unicode_escape')

# get all fuzzy scores:

def fuzzy(dataframe):
    
    index = df.columns.get_loc("Company")
    index2 = df.columns.get_loc("new_links")
    index3 = df.columns.get_loc("Title")
    
    # simple ratio
    
    dataframe["fuzzy_ratio_link(simple)"] = 0
    dataframe["fuzzy_ratio_title(simple)"] = 0
    
    index4 = df.columns.get_loc("fuzzy_ratio_link(simple)")
    index5 = df.columns.get_loc("fuzzy_ratio_title(simple)")
    
    # partial ratio
    
    dataframe["fuzzy_ratio_link(partial)"] = 0
    dataframe["fuzzy_ratio_title(partial)"] = 0
    
    index6 = df.columns.get_loc("fuzzy_ratio_link(partial)")
    index7 = df.columns.get_loc("fuzzy_ratio_title(partial)")
    
    # token sort ratio
    
    dataframe["fuzzy_ratio_link(token_sort)"] = 0
    dataframe["fuzzy_ratio_title(token_sort)"] = 0
    
    index8 = df.columns.get_loc("fuzzy_ratio_link(token_sort)")
    index9 = df.columns.get_loc("fuzzy_ratio_title(token_sort)")

    # token set ratio
    
    dataframe["fuzzy_ratio_link(token_set)"] = 0
    dataframe["fuzzy_ratio_title(token_set)"] = 0
    
    index10 = df.columns.get_loc("fuzzy_ratio_link(token_set)")
    index11 = df.columns.get_loc("fuzzy_ratio_title(token_set)")

    for i in range(len(df)):
        str_company = df.iat[i,index]
        str_new_links = df.iat[i,index2]
        str_title = df.iat[i,index3]
        
        df.iat[i,index4] = fuzz.ratio(str_company, str_new_links)
        df.iat[i,index5] = fuzz.ratio(str_company, str_title)
        
        df.iat[i,index6] = fuzz.partial_ratio(str_company, str_new_links)
        df.iat[i,index7] = fuzz.partial_ratio(str_company, str_title)

        df.iat[i,index8] = fuzz.token_sort_ratio(str_company, str_new_links)
        df.iat[i,index9] = fuzz.token_sort_ratio(str_company, str_title)

        df.iat[i,index10] = fuzz.token_set_ratio(str_company, str_new_links)
        df.iat[i,index11] = fuzz.token_set_ratio(str_company, str_title)

    
fuzzy(df)

df.to_csv("GoogleAPI_fuzzy.csv", index = False, sep=',')
