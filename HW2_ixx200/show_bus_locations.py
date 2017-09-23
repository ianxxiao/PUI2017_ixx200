# PULL BUS DATA FROM METRO API
# Return a list of bus information

import sys
import pandas as pd
import sys
import json
import urllib3
import pprint

def setup(api_key, bus_line):

	'''
	This function creates a API URL based on user inputs

	Args:
		api_key (str): private API key the use received from MTA API service
		bus_line (str): a bus line of interest (i.e. b27)

	Return: a full url including API request details, API Key, and Buse Line of Interest

	'''

	return "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + api_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

def callAPI(url):

	'''
	This function triggers a url link for RESTful API Call

	Args:
		ulr (str): a full url link including API address, API Key, and Bus Line of interest

	Return: 
		r.data: raw json data receive from the API call

	'''

	http = urllib3.PoolManager()
	r = http.request('GET', url)
	
	if r.status == 200:
		print ('API Request Succeeded with Request Code: ' + str(r.status))
		print ('==================================================')
	else:
		print ('Check Again. Request Code: ' + str(r.status))
		print ('==================================================')

	return r.data


def parseData(bus_line, raw_data):

	'''
	This function prints out key location information regarding a bus line at the request time; it also returns the data in a json format

	Args:
		bus_line (str): bus line of interest provided by the user 
		raw_data (str): bus location data in plain text format received from API request

	Return: bus location data in json format

	'''

	json_data = json.loads(raw_data)

	numBus = len(json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

	print("Bus Line : " + bus_line)
	print("Number of Active Buses : " + str(numBus))

	for i in range(numBus):

		latitude = json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']\
			['VehicleLocation']['Latitude']
		longitude = json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']\
			['VehicleLocation']['Longitude']

		print("Bus " + str(i+1) + " is at latitude " + str(latitude) + " and longitude " + str(longitude))

	print ('==================================================')

	return json_data

def exportData(json_data):

	'''
	This function exports bus location data to a file with the request timestamp

	Args:
		json_data (json object): bus locaiton data in json format

	Return: None

	'''
	
	fileName = 'bus_location_' + str(json_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['ValidUntil'].split('.')[0]) + '.txt'
	with open(fileName, 'w') as outfile:
		json.dump(json_data, outfile)


def main():

	'''
	This is the main execution workflow of this script; it standardize user input and calls all sub-functions

	It takes in 2 parameters passed in by an user and stores in api_key and bus_line respectively. 

	Expected user call: python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52

	'''

	try:
		api_key = sys.argv[1]
		bus_line = str(sys.argv[2]).upper()
		url = setup(api_key, bus_line)
		raw_data = callAPI(url)
		json_data = parseData(bus_line, raw_data)
		exportData(json_data)

	except:
		e = sys.exc_info()
		print("Something went wrong: " + str(e))
		sys.exit(1)

if __name__ == "__main__":
	main()