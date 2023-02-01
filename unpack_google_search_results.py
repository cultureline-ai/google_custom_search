import pandas as pd
import os
import json
import re

top_n = 5 # number between 1 and 10

entity_dir = './google_results/json/'
entity_links = [entity_dir + f for f in os.listdir(entity_dir)]

names = pd.read_csv('./company_queries.csv')

output = []
for link in entity_links:
    with open(link, 'r') as f:
        json_data = json.load(f)

    if json_data.get('items') is not None:
        links = [i.get('link', '') for i in json_data.get('items')][:top_n]

        name_gds = [i.get('title', '').replace('Working at ', '').replace(' | Glassdoor', '')
                    for i in json_data.get('items')][:top_n]

        snippets = [i.get('snippet', '') for i in json_data.get('items')][:top_n]

        # links_df = pd.DataFrame({'rank': range(1, len(links) + 1), 'link': links})
        output.append(pd.DataFrame({
            'result_rank': list(range(1, len(links) + 1)),
            'name_x': link.rsplit('/')[-1].replace('.json', '').replace('-fwdslash-', '/'),
            'name_gd': name_gds,
            'gd_link': links,
            'snippet': snippets}))

# stack individual search response-sets
output_df = pd.concat(output)

# merge it all back with input file
all_data = names.merge(output_df, how='left', on='name_x')

# format and output
all_data['result_rank'] = all_data['result_rank'].fillna(0).astype(int)
all_data.drop(columns=['search_query'], inplace=True)
all_data.to_csv(f'./google_results/top{top_n}_google_results.csv', index=False)
