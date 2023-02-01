import pandas as pd
import re
from collections import Counter

# get list of names
names = pd.read_csv('unique_ishares_missing_urls.csv')[['ticker','name_x']].drop_duplicates()

# evaluation step for stop words
all_names = ' '.join(names['name_x']).lower()
all_names = re.sub('[^a-z]', ' ', all_names)
all_names = re.sub('\\b.{1}\\b', ' ', all_names)
all_names = re.sub('\\s+', ' ', all_names)

name_count = Counter(all_names.split(' ')).most_common(100)
stop_names_count = [(k, v) for k, v in name_count]

# manually evaluate names
stop_names_count

# curated list of stop words
stop_names = ['inc', 'class', 'ltd', 'corporation', 'co', 'limited', 'corp', 'company',
              'plc', 'sa', 'of', 'sab','nav','com','pt','tbk','ad','se','nv',
              'ag', 'trust', 'incorporated', 'de',
              'sponsored', 'adr', 'nvdr',
              'bhd', 'ab', 'series','warrant','rt','pfd','non','voting','an']

# build the cleaner
def clean_names(name):
    name = name.lower() # to lower
    name = re.sub('[^a-z0-9]', ' ', name) # remove anything that isn't a letter or a number
    name = re.sub('\\b.{1}\\b', ' ', name) # remove anything that is only 1 character
    name = re.sub('\\b\\d*\\b', ' ', name) # remove anything that's just one number
    name = re.sub('\\s+', ' ', name)
    name = ' '.join([n for n in name.split(' ') if n not in stop_names])
    return name.strip()

# run the cleaner
names['search_query'] = names['name_x'].apply(clean_names)
names.to_csv('./company_queries.csv',index=False)