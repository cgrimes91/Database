import os
import pymysql
import pandas as pd # offers data structures and operations for manipulating numerical tables and time series.
import matplotlib


def MakeConnection(host, port, user, password, database):
	conn=""
	try:
		conn = pymysql.connect(
		host=host,
		port=int(port),
		user=user,
		passwd=password,
		db=database)
		print("Connected to Database Successfully");
	except pymysql.Error as e:
		print("Error %d: %s" % (e.args[0], e.args[1]))
	finally:
		return conn;

