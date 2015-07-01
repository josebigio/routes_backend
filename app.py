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
		d = {"stop_id":stopId, "routes":routes,"distance":distance,"lat":stop.stop_lat,"lng":stop.stop_lon,'data':True}
		resultList.append(d)
		
	resultDict = {"stops":resultList}
	return jsonify(resultDict)

#IN USE
@app.route('/api/getroutesandcoordinates',methods=['GET'])
def getRoutesAndCoordinates():
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
		routes = mainProcessor.getPolylineCoordinatesWithStopId(stopId,time,limit,weekday)
		distance = mainProcessor.getDistance(lat,lng,stop.stop_lat,stop.stop_lon)
		d = {"stop_id":stopId, "routes":routes,"distance":distance,"lat":stop.stop_lat,"lng":stop.stop_lon,"data":True}
		resultList.append(d)
		
	resultDict = {"stops":resultList}
	return jsonify(resultDict)

@app.route('/api/getallstops',methods=['GET'])
def getAllStops():
	resultDict = {"stops":mainProcessor.getAllStops()}
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

@app.route('/api/getstopsforroutes',methods=['GET'])
def getStopsForRouteHeadsign():
	headsignsString = str(request.args.get('headsigns'))
	weekday = int(request.args.get('weekday'))
	limit = int(request.args.get('limit'))
	time = str(request.args.get('time'))

	headSignsList = headsignsString.split(',')
	headSignQueryString = "trip_headsign='" + headSignsList[0] + "'"
	for headsign in headSignsList[1:]:
		headSignQueryString = headSignQueryString + " OR trip_headsign='" + headsign + "'"

	print(headSignQueryString)

	sql = "SELECT DISTINCT gtfs_stops.stop_id, gtfs_stops.stop_lat, gtfs_stops.stop_lon FROM gtfs_trips INNER JOIN gtfs_stop_times ON gtfs_stop_times.trip_id = gtfs_trips.trip_id INNER JOIN gtfs_stops ON gtfs_stops.stop_id = gtfs_stop_times.stop_id WHERE " + headSignQueryString + ";"
	result = db.engine.execute(sql)
	stopList = list()
	for row in result:
		routes = mainProcessor.getUpcomingRoutesWithStopId(row[0],time,limit,weekday)
		d = {"stop_id":row[0], "routes":routes,"distance":None,"lat":row[1],"lng":row[2],"data":True}
		stopList.append(d)

	return jsonify({"stops":stopList})
	
if __name__ == '__main__':
	app.run()
