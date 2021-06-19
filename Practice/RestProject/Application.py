# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:05:44 2021

@author: Ashok Kumar Jha
"""
import configparser
import dbconnection

config = configparser.RawConfigParser()
config.read('appconfig.properties')

app_cfg = dict(config.items('APP SECTION'))

conn = dbconnection.getdbconnection(dict(config.items('DB SECTION')))
print(conn)
dbconnection.closedbconnection(conn)