from flask import Flask, render_template, request
from requests.auth import HTTPBasicAuth
import requests
import cleandata
import time

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])

################
#### routes ####
################
@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    bus_stop = ""
    today_data = ""

    #App ID
    client_id = '18d2b38b'
    #Key
    client_key = '5421a12f0194e02cd961472d58a52389'
    if request.method == "POST":
        try:
            response = requests.get('http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?'
                                    'Stopid=36012&ReturnList=Stoppointname,LineName,DestinationName,EstimatedTime',
                                    auth=HTTPBasicAuth(client_id, client_key))

            r = response.content
        except():
            errors.append('Unable to reach TFL')
            return render_template('index.html', errors=errors)

        if r:
            #Creates the Object
            tfl_data = cleandata.CleanData()
            #Clean the TFL array
            results = tfl_data.clea_array(r)
            results = tfl_data.set_list(results)
            bus_stop = 'Vicarage Rd / Wandle Park Tram Stop'
            today_data = time.strftime("%d-%m-%Y")
            #print results
    return render_template('index.html', errors=errors, results=results, today=today_data, bus_stop=bus_stop)


if __name__ == '__main__':
    app.run(debug=True)