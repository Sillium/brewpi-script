#!/usr/bin/python

import socket
import logging
from BrewPiUtil import logMessage

def pushToInfluxDB(row, host, port):
  try:
    pointString = getLineString(row)
    # logMessage("InfluxDB: '" + pointString + "', '" + host + "', " + str(port))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(pointString, (host, port))
  except:
    logging.exception("Pushing to InfluxDB failed.")
  return

# test 2

def getLineString(row):
  lineString = "brewPi,origin=brewpi-script,host=%s" % (socket.gethostname())

  if row['State'] is not None:
    lineString += " state=%si" % (row['State'])

  if row['BeerTemp'] is not None:
    lineString += ",beerTemp=%s" % (row['BeerTemp'])

  if row['BeerSet'] is not None:
    lineString += ",beerSet=%s" % (row['BeerSet'])

  if row['BeerAnn'] is not None:
    lineString += ",beerAnn=%s" % (row['BeerAnn'])

  if row['FridgeTemp'] is not None:
    lineString += ",fridgeTemp=%s" % (row['FridgeTemp'])

  if row['FridgeSet'] is not None:
    lineString += ",fridgeSet=%s" % (row['FridgeSet'])

  if row['FridgeAnn'] is not None:
    lineString += ",fridgeAnn=%s" % (row['FridgeAnn'])

  if row['RoomTemp'] is not None:
    lineString += ",roomTemp=%s" % (row['RoomTemp'])

  return lineString
