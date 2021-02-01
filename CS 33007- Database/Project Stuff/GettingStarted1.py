#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
#                                                          #
# Simple script to connect to mysql database      #
#                                                          #
#                                                          #
############################################################

import pymysql as db


HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "root"
DB = "university"

connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB) # create database connecition
try:
    dbhandler = connection.cursor() # create a cursor object
    dbhandler.execute("select * from instructor;") # exceute the query
    result = dbhandler.fetchall() # fetch all data from the cursor area
    for row in result:  # result is a two dimensional array now, print using two loops.
        for cell in row:
            print cell, " ",
        print "\n"

except Exception as e:
    print e

finally:
    connection.close()