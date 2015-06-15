#!/usr/bin/env python
from geopy.distance import vincenty
import random


DEBUG = 0

def getRouteWithTripId(tripId):
	tripId = str(tripId)
	file = open("GTFS/trips.txt")
	for line in file:
		lineArr = line.split(',')
		if tripId in lineArr[2]:
			routeId = lineArr[0]
			if DEBUG:
				print("found routeId: %s" % routeId)
			return routeId

def getRoutesWithStopID(stopId):
	stopId = str(stopId)
	print("requested stopId: %s" % stopId)

	routeIdSet = set()
	file = open("GTFS/stop_times.txt")
	for line in file:
		lineArr = line.split(',')
		stopIdR = lineArr[3]
		if stopIdR in stopId:
			tripId = lineArr[0]
			if DEBUG:
				print("found tripId %s" % tripId)
			routeIdSet.add(getRouteWithTripId(tripId))

	return list(routeIdSet)

def getDistance(lat1,long1,lat2,long2):
	loc1 = (lat1,long1)
	loc2 = (lat2,long2)
	return vincenty(loc1, loc2).miles
	

def getBusStops(lat, lng, radius):
	print("requested lat,lng: " + str(lat) + ", " + str(lng))
	file = open("GTFS/stops.txt")
	file.readline()
	for line in file:
			lineArr = line.split(',')
			latR = str(lineArr[4])
			lngR = str(lineArr[5])
			distance = getDistance(lat,lng,float(latR),float(lngR))
			if distance<radius:
				stopId = lineArr[0]
				routes = getRoutesWithStopID(stopId)
				print("distance: %f; name: %s"%(distance,lineArr[2]))
				print(routes)	




getBusStops(30.2642580,-97.7323400,0.5)


