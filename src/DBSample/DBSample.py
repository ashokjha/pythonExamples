# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from getpass import getpass
import mysql.connector 
class DBConnection(object):
    def __init__(self, db_cfg):
        self.db_cfg = db_cfg
    
    def dbconnection(self):
        try:
            with mysql.connector.connect(host = self.db_cfg['host'],
                                         user = self.db_cfg['id'], 
                                         password = self.db_cfg['key'],) as connection:
                print("Connected ",connection)
                #connection.close()  #with clause abstract away the cleanup activity'
        except mysql.connector.Error as e:
            print(e)
            
    def createdb(self,dbname="online_movie_rating"):
        try:
            with mysql.connector.connect(host = self.db_cfg['host'],
                                         user = self.db_cfg['id'], 
                                         password = self.db_cfg['key']) as connection:
                print("Connected ")
                create_db_query = "CREATE DATABASE "
                with connection.cursor() as cursor:
                    cursor.execute(create_db_query+dbname)
        except mysql.connector.Error as e:
            print(e)
    def existingdb(self):
        try:
            with mysql.connector.connect(host = self.db_cfg['host'],
                                         user = self.db_cfg['id'], 
                                         password = self.db_cfg['key']) as connection:
                print("Connected ")
                show_db_query = "SHOW DATABASES"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    for db in cursor:
                        print(db)      
        except mysql.connector.Error as e:
            print(e)

db_cfg={}
db_cfg['host']="localhost"
db_cfg['id']=input("Enter username: ")
db_cfg['key']=getpass("Enter password: ")
dbins = DBConnection(db_cfg) 
dbins.dbconnection()
dbins.createdb()
dbins.existingdb()
