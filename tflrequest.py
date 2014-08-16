import requests
from requests.auth import HTTPBasicAuth
import cleandata

#App ID
client_id = '18d2b38b'
#Key
client_key = '5421a12f0194e02cd961472d58a52389'

response = requests.get('http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?'
                        'Stopid=36012&ReturnList=Stoppointname,LineName,DestinationName,EstimatedTime',
                        auth=HTTPBasicAuth(client_id, client_key))

tflfeed = response.content

#Creates the Object
tfl_data = cleandata.CleanData()
#Clean the TFL array
to_clean = tfl_data.clea_array(tflfeed)
#Transform in to JSON
print tfl_data.set_json(to_clean)
