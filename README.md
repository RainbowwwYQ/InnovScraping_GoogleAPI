
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

More informatino in the document "PREP_GoogleAPI". The removed company list is in the file of "remove_list.csv".


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

#### The results you will have from Google API:

| Company | DisplayLink | Website | Title |
| ------- | ----------- | ------- | ----- |
| Wiberg Corporation | wiberg.ca | http://wiberg.ca/ | Wiberg Corporation |
| Wiberg Corporation | www.perfumerflavorist.com | https://www.perfumerflavorist.com/networking/news/company/IFF-Completes-Buyout-of-Wiberg-Corporation--510758411.html | IFF Completes Buyout of Wiberg Corporation |
| ... | ... | ... | ... |

### Then open the file "Cleaning.py" and run it.

- If the file name is different, please remember to edit it. 
- Please record how many URLs are removed if needed. 
- (Normally, the common websites should be removed at the step of scraping.) 
- You will get a file "GoogleAPI_cleaned.csv" as the results at this step.

### Run the file "fuzzy_matching.py" to get the fuzzy scores.

### Run the file "pick_up.py" to get the good-matching URLs.

- Perfect-matching URLs are those with fuzzy scores for both URLs and titles greater than 70
- Good-matching URLs are those with a fuzzy score for titles greater than 90 and a fuzzy score for URLs greater than 40.
- Record how many perfect-matching URLs and good-matching URLs, if needed!
- The perfect matching is not 100 percent matching but all of the URLs are highly related.
- It might have the situation that one company has more than one good-matching websites.
