# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:32:37 2021

@author: Ashok Kumar Jha
"""

import mysql.connector 

def  getdbconnection(dct):
    print(dct)
    return mysql.connector.connect(host= dct['host'],user= dct['key'],password=dct['val'] )
    #return connect(host= 'localhost',user= 'root',password='Ashu.Kr.Jha@gma1l.c0m' )
 
def closedbconnection(conn):
    if conn and conn.is_connected():
        try:
            conn.close()
        except mysql.connector.Error as e:
            print(e)