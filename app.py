from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import os
from geopy.distance import vincenty


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

import mainProcessor

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/api/getroutes',methods=['GET'])
def getRoutes():
	lat = request.args.get('lat')
	lng = request.args.get('lng')
	radius = request.args.get('radius')

	stops = mainProcessor.getStopIds(lat,lng,radius)
	resultDict = dict()
	for stop in stops:
		stopId = stop.stop_id
		routes = mainProcessor.getRoutesWithStopID(stopId)
		routeNames = [route.route_id for route in routes]
		resultDict[stopId] = [routeNames,mainProcessor.getDistance(lat,lng,stop.stop_lat,stop.stop_lon)]
		

	return jsonify(resultDict)

@app.route('/api/getroutesusingstopid',methods=['GET'])
def getroutesusingstopid():
	stopId = request.args.get('stopId')
	result = mainProcessor.getRoutesWithStopID(stopId)
	resultDict = dict()
	index = 0
	for route in result:
		resultDict[route.route_id] = route.route_long_name

	return jsonify(resultDict)

@app.route('/api/getstopidsaround',methods=['GET'])
def getStopIdsAround():
	lat = request.args.get('lat')
	lng = request.args.get('lng')
	radius = request.args.get('radius')
	result = mainProcessor.getStopIds(lat,lng,radius)
	resultDict = dict()
	index = 0
	for stop in result:
		resultDict[stop.stop_id] = mainProcessor.getDistance(lat,lng,stop.stop_lat,stop.stop_lon)

	return jsonify(resultDict)
	
if __name__ == '__main__':
	app.run()
