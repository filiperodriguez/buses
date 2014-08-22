import requests
from requests.auth import HTTPBasicAuth
import json
import csv
import re

#App ID
client_id = '18d2b38b'
#Key
client_key = '5421a12f0194e02cd961472d58a52389'

#Request TFL Bus data based on Stopid
response = requests.get('http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?'
                        'Stopid=36012&ReturnList=Stoppointname,LineName,DestinationName,EstimatedTime',
                        auth=HTTPBasicAuth(client_id, client_key))
tflfeed = response.content

#Spliting and removing the first item of the array
raw_data = (tflfeed.split('\n'))
raw_data.pop(0)
#print raw_data

#Loop through to convert each line into JSON objects
fieldnames = ("id", "DestinationName", "LineName", "Direction", "EstimatedTime")
lst = []
for lines in raw_data:
    #print lines
    #line = re.sub(r'\[', "", lines)
    #line = re.sub(r'\]', "", line)
    #print line
    #reader = csv.DictReader(line, fieldnames)
    simplejson.loads(lines)
    out = json.dumps()
    lst.append(out)

#print lst