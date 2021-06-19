# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:05:44 2021

@author: Ashok Kumar Jha
"""
from configparser import RawConfigParser
from dbconnection import dbconnection 

config = RawConfigParser()
config.read('appconfig.properties')

if __name__ == '__main__' :
    dbc = dbconnection(dict(config.items('DB SECTION'))) 
    try:
        print(config)
        print(dbc)
        dbc.createconnection()
        for db in dbc.dbList():
            print(db)
        dbc.createdb()
        dbc.createTable()
    except Exception as ex:
        print(ex)
    finally:
        dbc.closedbconnection()