# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:05:44 2021

@author: Ashok Kumar Jha
"""
from configparser import RawConfigParser
from dbconnection import dbconnection 
import sqlutility
from datetime import datetime


config = RawConfigParser()
config.read('appconfig.properties')
def testdbactivity():
    dbconf=dict(config.items('DB SECTION'))
    dbc = dbconnection(dbconf) 
    try:
        dbc.createconnection()
        for db in dbc.dbList():
            print(db)
        if dbconf["ddlc"] == "1" :   
            dbc.createdb(sqlutility.createdbsql(dbconf['db']))
            dbc.createTable(sqlutility.createDdlTbSql())
            dbc.alterTable(sqlutility.updateDdlTSql("ashu.students",
                                                'ADD entrydate DATE not null, ADD temp VARCHAR(50)'))
            dbc.alterTable(sqlutility.alterDdlSql("ashu.students",'temp'))
        data ={'name':'Ashok Kumar Jha','entrydate':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        dbc.insert(sqlutility.insertSql(data))
        for d in dbc.fetchData(sqlutility.fetchsql()):
            print(d)
        data ={'name':'Rama','id':15}    
        dbc.updateData(sqlutility.updateRecordSql(data))
        dbc.removeData(sqlutility.removeRecordSql(7))
        for d in dbc.fetchData(sqlutility.fetchsql()):
            print(d)        
        
    except Exception as ex:
        print(ex)
    finally:
        dbc.closedbconnection()
    

if __name__ == '__main__' :
    testdbactivity()
 
