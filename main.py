#The libraries are loading.
from flask import Flask
import googlemaps
import logging

app = Flask(__name__)

@app.route('/')

#The main function runs.
def main():
    #Various codes for log system registration.
    logging.basicConfig(
        filename='emirhan-project.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s',
        level=logging.DEBUG
    )
    #Trial opens
    try:
        #The loop is starting.
        while True:
            a = input("Press 'A' button to login: ")
            #'A' key will not enter external software.
            if a == ("A"):
                gmaps = googlemaps.Client(key='***************************************')
                # Requires cities name
                # You must enter a location. (b variable)
                b = input("Enter distance: ")
                distance = \
                    gmaps.distance_matrix("Moskovskaya Kol'tsevaya Avtomobil'naya Doroga, Russia", b)['rows'][0][
                        'elements'][
                        0]

                {u'distance': {u'text': u'1,431 km', u'value': 1417631,
                 u'duration': {u'text': u'1 day 0 hours', u'value': 87010},
                 u'status': u'OK'}
                #The code is projected onto the screen and the return process begins.
                return distance
            else:
                print("Try again or pull 31...")
                continue
    #It logs errors to the log file.
    except Exception as sex:
        logging.error(sex)
