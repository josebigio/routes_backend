#!/usr/bin/env python

from geopy.distance import vincenty
import random
from app import app
import models
from app import db


DEBUG = 0

def getSecsFromZero(timeString):
	timeArr = timeString.split(':')
	return int(timeArr[0])*3600+int(timeArr[1])*60+int(timeArr[2])

def getSecondsBetweenDates(earlyTime,laterTime):
	return getSecsFromZero(laterTime)-getSecsFromZero(earlyTime)

def getRouteWithTripId(tripId):
	trip =  models.Trips.query.filter_by(trip_id=tripId).first()
	return models.Routes.query.filter_by(route_id=trip.route_id).first()


def getRoutesWithStopID(stopId):
	stopId = str(stopId)

	sql = "SELECT DISTINCT gtfs_trips.route_id FROM gtfs_stops INNER JOIN gtfs_stop_times ON gtfs_stop_times.stop_id = gtfs_stops.stop_id INNER JOIN gtfs_trips ON gtfs_trips.trip_id=gtfs_stop_times.trip_id INNER JOIN gtfs_calendar ON gtfs_trips.trip_id=gtfs_stop_times.trip_id WHERE gtfs_stops.stop_id=" + stopId + " and gtfs_calendar.saturday=0 and gtfs_calendar.sunday=0;"
	result = db.engine.execute(sql)
	resultList = list()
	for column in result:
		resultList.append(column[0])

	return resultList

def getUpcomingRoutesWithStopId(stopId,time,limit,weekend):

	sql = ""
	if weekend:
		sql = "SELECT  gtfs_trips.route_id, gtfs_stop_times.arrival_time FROM gtfs_stops INNER JOIN gtfs_stop_times ON gtfs_stop_times.stop_id = gtfs_stops.stop_id INNER JOIN gtfs_trips ON gtfs_trips.trip_id=gtfs_stop_times.trip_id INNER JOIN gtfs_calendar ON gtfs_trips.service_id=gtfs_calendar.service_id WHERE gtfs_stops.stop_id=" + str(stopId) + " and gtfs_stop_times.pickup_type='0' and gtfs_calendar.saturday=1 and gtfs_calendar.sunday=1 and gtfs_calendar.friday=0;"
	else:
		sql = "SELECT  gtfs_trips.route_id, gtfs_stop_times.arrival_time FROM gtfs_stops INNER JOIN gtfs_stop_times ON gtfs_stop_times.stop_id = gtfs_stops.stop_id INNER JOIN gtfs_trips ON gtfs_trips.trip_id=gtfs_stop_times.trip_id INNER JOIN gtfs_calendar ON gtfs_trips.service_id=gtfs_calendar.service_id WHERE gtfs_stops.stop_id=" + str(stopId) + " and gtfs_stop_times.pickup_type='0' and gtfs_calendar.saturday=0 and gtfs_calendar.sunday=0 and gtfs_calendar.friday=1;"

	result = db.engine.execute(sql)
	resultList = list()
	result = db.engine.execute(sql)
	print(result)
	sortedResult = sorted(result,key=lambda column:getSecsFromZero(column[1]))
	resultList = list()
	for column in sortedResult:
		secsAway = getSecondsBetweenDates(time,column[1])
		if secsAway>0:
			if secsAway>limit:
				return resultList
			resultList.append((column[0],column[1]))


	return resultList


def getDistance(lat1,long1,lat2,long2):
	loc1 = (lat1,long1)
	loc2 = (lat2,long2)
	return vincenty(loc1, loc2).miles
	

def getRoutes(lat, lng, radius):
	stops = getStopIds(lat,lng,radius)
	resultList = list()
	for stop in stops:
		stopId = stop.stop_id
		resultList.append(getRoutesWithStopID(stopId))

	return resultList
		

def getStopIds(lat, lng, radius):
	
	result = models.Stops.query.all()
	radius = float(radius)

	resultList = list()
	for stop in result:
		distance = getDistance(lat,lng,stop.stop_lat,stop.stop_lon)
		if distance < radius:
			resultList.append(stop)

	
	return resultList


