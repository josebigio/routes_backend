#!/usr/bin/env python

from geopy.distance import vincenty
import random
from app import app
import models
from app import db


DEBUG = 0

def getRouteWithTripId(tripId):
	trip =  models.Trips.query.filter_by(trip_id=tripId).first()
	return models.Routes.query.filter_by(route_id=trip.route_id).first()


def getRoutesWithStopID(stopId):
	stopId = str(stopId)

	sql = "SELECT DISTINCT gtfs_trips.route_id FROM gtfs_stops INNER JOIN gtfs_stop_times ON gtfs_stop_times.stop_id = gtfs_stops.stop_id INNER JOIN gtfs_trips ON gtfs_trips.trip_id=gtfs_stop_times.trip_id WHERE gtfs_stops.stop_id=506;"
	result = db.engine.execute(sql)
	resultList = list()
	for column in result:
		resultList.append(column[0])

	return resultList

	# routeIdSet = set()
	# #stopTimes has all the trips that go stopId
	# stopTimes = models.StopTimes.query.filter_by(stop_id=stopId).all()
	# for stopTime in stopTimes:
	# 	routeIdSet.add(getRouteWithTripId(stopTime.trip_id))
	
	# return routeIdSet

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


