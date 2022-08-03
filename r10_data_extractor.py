import pandas as pd
import json

sim_file = 'Golf-SIM_SESSION.json'
my_clubs_file = 'Golf-CLUB.json'
club_types_file = 'Golf-CLUB_TYPES.json'
output = 'output_converted_data.csv'

with open(my_clubs_file) as f:
    my_club_data = json.load(f)

with open(club_types_file) as f:
    club_types_data = json.load(f)

with open(sim_file) as f:
    simdata = json.load(f)

my_clubdata = pd.DataFrame(my_club_data['data'])
club_typesdata = pd.DataFrame(club_types_data['data'])
simdata = pd.DataFrame(simdata['data']).explode('shots', ignore_index=True)

bag = pd.merge(my_clubdata, club_typesdata, left_on='clubTypeId', right_on='value')

shotFrame = pd.DataFrame(simdata['shots'].tolist()).reset_index()
summaryFrame = pd.DataFrame(simdata['summary'].tolist()).reset_index()

t = pd.merge(summaryFrame, shotFrame)
t = pd.merge(t, bag, left_on='clubId', right_on='id')
t.to_csv(output)
print('You should now have a file called output_converted_data.csv in this directory.')
