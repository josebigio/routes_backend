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
	lat = float(request.args.get('lat'))
	lng = float(request.args.get('lng'))
	radius = request.args.get('radius')
	weekday = int(request.args.get('weekday'))
	limit = int(request.args.get('limit'))
	time = str(request.args.get('time'))

	stops = mainProcessor.getStopIds(lat,lng,radius)
	resultList = []
	for stop in stops:
		stopId = stop.stop_id
		routes = mainProcessor.getUpcomingRoutesWithStopId(stopId,time,limit,weekday)
		distance = mainProcessor.getDistance(lat,lng,stop.stop_lat,stop.stop_lon)
		d = {"stop_id":stopId, "routes":routes,"distance":distance}
		resultList.append(d)
		
	resultDict = {"stops":resultList}
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

@app.route('/api/getstopidsforroute',methods=['GET'])
def getStopsForRoute():
	route = request.args.get('route')
	sql = "SELECT DISTINCT gtfs_stops.stop_id, gtfs_stops.stop_name FROM gtfs_trips INNER JOIN gtfs_stop_times ON gtfs_stop_times.trip_id = gtfs_trips.trip_id INNER JOIN gtfs_stops ON gtfs_stops.stop_id = gtfs_stop_times.stop_id WHERE route_id = " + route + ";"
	result = db.engine.execute(sql)
	resultDict = dict()
	for row in result:
		resultDict[row[0]] = row[1]

	return jsonify(resultDict)
	
if __name__ == '__main__':
	app.run()
