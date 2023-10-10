#Import necessary packages
import requests
import pandas as pd
import json
import numpy as np
from tqdm import tqdm

pd.set_option('display.max_columns', None)


# Make a request to GET the data from the FPL API
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
response = requests.get(url)

# Convert JSON data to a python object
data = response.json()

team_name_id = pd.DataFrame.from_dict(data['teams'])
team_name_id = team_name_id[['name', 'id']]



#Look at elements in elements
df = pd.DataFrame.from_dict(data['elements'])

player_data= df[['first_name', 'second_name', 'id', 'element_type', 'team']]

all_upcoming_fixtures = pd.DataFrame()
all_old_fixtures = pd.DataFrame()    


for i in tqdm(df['id'], desc="Processing players", unit="player"):
    url = f"https://fantasy.premierleague.com/api/element-summary/{i}/"
    response = requests.get(url)
    data = json.loads(response.text)
    upcoming_fixtures = pd.DataFrame.from_dict(data['fixtures'])
    old_fixtures = pd.DataFrame.from_dict(data['history'])
    upcoming_fixtures['element'] = i
    old_fixtures['element'] = i

    # Concatenate each iteration of player_fixtures to all_player_fixtures
    all_upcoming_fixtures = pd.concat([all_upcoming_fixtures, upcoming_fixtures])
    all_old_fixtures = pd.concat([all_old_fixtures, old_fixtures])

