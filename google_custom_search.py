import requests
import pandas as pd
import os
import traceback
import json
import time
import config

# list of existing results/errors
results = os.listdir('./google_results/json')
errors = os.listdir('./google_results/errors')

# list of names and their cleaned queries to work from
names = pd.read_csv('./company_queries.csv')

# loop through names
output = []
for i, r in names.iterrows():
    output_file = r['name_x'].replace('/','-fwdslash-') + '.json'
    try:
        if output_file not in (results + errors):
            query_string = {"key": config.GoogleCSE.key,
                            "cx": config.GoogleCSE.cx,
                            "q": r['name_x']}
            response = requests.get(
                config.GoogleCSE.base_url, 
                params=query_string)

            time.sleep(0.5)

            print(response.status_code)
            if response.status_code != 200:
                print('response.text:')
                print(response.text[0:200])

            json_data = response.json()

            if json_data.get('error') is None:

                with open(f'./google_results/json/{output_file}', 'w') as f:
                    json.dump(json_data, f)
                print('*** successfully processed for ***')
                print(r)
            else:
                print('*** error from google ***')
                print(r)
                with open(f'./google_results/errors/{output_file}', 'w') as f:
                    json.dump(json_data, f)

        else:
            print('*** already processed for ***')
            print(r)

    except BaseException as err:
        print(str(err))
        with open(f'./google_results/errors/{output_file}', 'w') as f:
            f.write(str(err))
            f.write(traceback.format_exc())
