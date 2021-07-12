# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:15:33 2021

@author: Ashok Mumar Jha

"""
import mysql.connector 

class DBConnection(object):
    def __init__(self, db_cfg):
        self.db_cfg = db_cfg
    
    def checkconnection(self):
        successful = False
        try:
            with mysql.connector.connect(host = self.db_cfg['host'],
                                         user = self.db_cfg['id'], 
                                         password = self.db_cfg['key'],):
                successful = True
                
        except mysql.connector.Error as e:
            print(e)
        return successful
            
    def createdb(self,dbname="online_movie_rating"):
        result = None
        try:
            with mysql.connector.connect(host = self.db_cfg['host'],
                                         user = self.db_cfg['id'], 
                                         password = self.db_cfg['key']) as connection:
                create_db_query = "CREATE DATABASE "
                with connection.cursor() as cursor:
                    result = cursor.execute(create_db_query+dbname)
        except mysql.connector.Error as e:
            print(e)
        return result


    def existingdb(self):
        dbs = []
        try:
            with mysql.connector.connect(host = self.db_cfg['host'],
                                         user = self.db_cfg['id'], 
                                         password = self.db_cfg['key']) as connection:
                show_db_query = "SHOW DATABASES"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    dbs = [db for db in cursor] 
        except mysql.connector.Error as e:
            raise(e)
        return dbs
    
    def getresult(self,query):
        records = []
        try:
            with mysql.connector.connect(host = self.db_cfg['host'],
                                         user = self.db_cfg['id'], 
                                         password = self.db_cfg['key']) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    records = cursor.fetchall()
        except mysql.connector.Error as e:
            raise(e)
        return records    
    
    
            
if __name__ == '__main__':
    db_cfg={'host':"localhost", 'id':'root', 'key':'Ashu.Kr.Jha@gma1l.c0m'}
    dbins = DBConnection(db_cfg) 
    if dbins.checkconnection():
        print('Connection successful')
    else:
        print('Connection failed')
    try : 
        result = dbins.createdb() 
        print(result)
    except mysql.connector.Error as e:
        print(e)
    print(dbins.existingdb())
    try : 
        result = dbins.getresult('SELECT * FROM ashu.students') 
        print(result)
    except mysql.connector.Error as e:
        print(e)
    
