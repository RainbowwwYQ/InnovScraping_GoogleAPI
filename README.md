
## Instructions for Google API:


### Preparation before using Google Custom API:


#### 1) A company-name list. Format examples are shown as below:

| Company_name |
| ------------ |
| Acadian Fishermen's Co-Operative Association Limited |
| Acadian Supreme Inc. |
| Acc Atlantic Canada Connection Inc |
| Ace Liquor Corporation |
| Acema Importations, Inc. |
		
Please: 
- don't insert more than one company in each row; 
- don't forget to add a column name "Company_name". 
- More samples are attached in the file "sample"


#### 2) API keys and custom engine ID

API key:https://console.cloud.google.com/home/

Custom engine ID:https://cse.google.com/cse/create/new

More informatino in the document "PREP_GoogleAPI".


### Once you have your account set up, go ahead and install the library:

```
pip install google-api-python-client
```

### Then open the file "GoogleAPI_scraping.py" and edit following the comments.

- put the "company list" file and the coding script into the sampe folder. 
- edit the file name
- edit your API key and custom search engine ID
- record running time if needed
- copy and paste the data from the data frame "my_result" to the csv file you create.





