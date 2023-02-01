# Glassdoor URL Mapping via Google Custom Search
Map iShares names to Glassdoor URLs using Google Custom Search

## Google Custom Search Info
- Filter Results to anything starting with `https://www.glassdoor.com/Overview/Working-at-`
- Let API do the Rest

## Process Overview
1. Create a Google Custom Search Engine: https://programmablesearchengine.google.com/controlpanel/create
   - Filter Results to anything starting with `https://www.glassdoor.com/Overview/Working-at-`
2. Run `google_custom_search.py`
   - This loops through all the names in the input file `unique_ishares_missing_urls.csv`(iShares names) and search for them using Google CSE from Step 1
   - Each search gets saved as a file in `google_results/json/<iShares company name>.json`
   - Errors get saved as a file in in `google_results/errors/<iShares company name>.json`
3. Run `unpack_google_search_results.py` 
   - This loops through all the files in `google_results/json/`, extracts the relevant items, and stackes them into a single DataFrame and exports to CSV
   - Output File: `google_results/top5_google_results.csv`
   
## Output
### Column definitions:
`ticker` = ticker from "unique_ishares_missing_urls.csv"
`name_x` =  name from "unique_ishares_missing_urls.csv"
`result_rank` = where it showed up in googles response
`name_gd` = the name associated with the glassdoor url
`gd_link` = the link to the pagesnippet = snippet from google's search response metadata, often the company's overview/description or mission statement (from their homepage on glassdoor.com)

### Example


   

