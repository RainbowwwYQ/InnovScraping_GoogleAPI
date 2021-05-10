#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:08:20 2020

@author: mayhe
"""
import pandas as pd
import string

# please notice: no comma in original documents!

df = pd.read_csv("GoogleAPI_all.csv", encoding= 'unicode_escape') 
remove_url = pd.read_csv("remove_list.csv").drop_duplicates()

# change the file name if it is different from yours!!

# ---- step one: remove strings such as "www" ----

def remove(dataframe, col):
    
    remove_head = ["www","http"]

    dataframe["new_links"] = None  # the links used to compare
    
    for i in range(len(dataframe)):
    
        temp = dataframe.iloc[i,int(col)]

        for m in remove_head:
            if (temp.startswith('.') != True) and (m in temp):
                    temp = temp.lstrip(m).strip(string.punctuation)
        
        index = dataframe.columns.get_loc("new_links") 
        dataframe.iloc[i,index] = temp
    
    
remove(remove_url, 0) # which column you put the links
remove(df, 1)
    
# ---- step two: remove the common websites such as LinkedIn ----  

remove_url = remove_url["new_links"].tolist()
index = df.columns.get_loc("new_links")
    
for i in range(len(df)):
    temp = df.iloc[i,index]
    for item in remove_url:
        if item in temp:
            df.iloc[i,index] = None

before = len(df)
df.dropna(axis=0, how='any', inplace=True)
after =len(df)
diff = before - after
print(f'You have removed {diff} high-frequency URLs!')

df.to_csv("GoogleAPI_cleaned.csv", index = False, sep=',')

# df is data frame we obtain. transfer df to next py file
    
