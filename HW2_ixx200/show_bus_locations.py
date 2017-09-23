# PULL BUS DATA FROM METRO API
# Return a list of bus information

# 1. Import Libraries
import sys
import pandas as pd
import sys
import json
import urllib3
import pprint

def setup():

	#TODO: Parametarize
	#api_key = sys.argv[1]
	#bus_line = sys.argv[2]

	api_key = "4b4429ca-da0e-498b-aa13-a84ae243276e"
	bus_line = "B26"

	return "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + api_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

def callAPI(url):

	# Make a REST API Call

	http = urllib3.PoolManager()
	r = http.request('GET', url)
	
	if r.status == 200:
		print ('API Request is Successful with Request Code: ' + str(r.status))
	else:
		print ('Check Again. Request Code: ' + str(r.status))

	return r.data


def parseData(raw_data):

	# load raw data into json
	json_data = json.loads(raw_data)

	numBus = len(json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

	for i in range(numBus):

		latitude = json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']\
			['VehicleLocation']['Latitude']
		longitude = json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']\
			['VehicleLocation']['Longitude']

		print("Bus " + str(i+1) + " is at latitude " + str(latitude) + " and longitude " + str(longitude))

	return json_data

def exportData(json_data):

	# export json to csv with request timestamp
	fileName = 'bus_location_' + str(json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['ValidUntil'].split('.')[0]) + '.txt'
	with open(fileName, 'w') as outfile:
		json.dump(json_data, outfile)


def main():

	try:
		url = setup()
		raw_data = callAPI(url)
		json_data = parseData(raw_data)
		exportData(json_data)

	except:
		e = sys.exc_info()
		print("Something went wrong: " + str(e))
		sys.exit(1)

if __name__ == "__main__":
	main()