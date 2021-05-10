#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:33:19 2020

@author: mayhe
"""

from googleapiclient.discovery import build   # Import the API library
import pandas as pd
from tqdm import tqdm  # About progress report
import time   # About sleeptime
import random

# read company list

df = pd.read_csv("sample.csv")  # edit the file name of the company list
company_name = df['Company_name'].drop_duplicates().values.tolist()

# create a dataframe to put data we obtain

my_result = pd.DataFrame(columns=['Comapny', 'DisplayLink', 'Website','Title'])


# define a function for API searhing
def google_query(query, api_key, cse_id, **kwargs):
    query_service = build("customsearch", 
                          "v1", 
                          developerKey=api_key
                          )  
    query_results = query_service.cse().list(q=query, 
                                             cx=cse_id,
                                             **kwargs    
                                             ).execute()
    return query_results['items']

# enter your credentials:
    
api_key = "enter your API key here"  # enter API Keys
cse_id = "enter your Custom Search Engine ID here"   # enter Custom Search Engine ID

start = time.time()

for i in tqdm(company_name):
    temp = google_query(i,
                        api_key, 
                        cse_id, 
                        num = 10
                        )
    for j in temp:
        my_result.loc[len(my_result)]=[i,
                                       j['displayLink'],
                                       j['link'],
                                       j['title']]
    sleeptime=random.randint(0, 1)
    time.sleep(sleeptime)

end = time.time()
print("Task finished. Running time: {} second.".format(round(end-start, 2)))

# Task finished. Running time: 
# test1: 235 second fr 55
# test2: 68.78 second for 20
# test3: 68.2 second for 21
