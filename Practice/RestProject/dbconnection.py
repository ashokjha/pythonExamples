# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:32:37 2021

@author: Ashok Kumar Jha
"""

import mysql.connector 

class dbconnection(object):
    def __init__(self, db_cfg):
        '''
            Create Database communication interface
            db_cfg: {host:<HOST IP>,key:<Database User ID>,val:<password>,db:<Database Name>}
        '''        
        self.db_cfg = db_cfg

    def createconnection(self):
        '''
            Return Database connection Based on Configuration
        '''
        print(self.db_cfg)
        try:
             self.conn = mysql.connector.connect(host= self.db_cfg['host'],
                                       user= self.db_cfg['key'],
                                       password=self.db_cfg['val'] )
        except Exception as ex:
            raise ex

     
    def createdb(self):
        '''
            Create Database Database based on onfiguration 
            Raise error in case of failure
        '''
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("CREATE DATABASE IF NOT EXISTS "+self.db_cfg['db'])
        except mysql.connector.Error as ex:
            raise ex
            
    def dbList(self):
        
        dblst=[]
        try:
            show_db_query = "SHOW DATABASES"
            with self.conn.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    dblst.append(db)      
        except mysql.connector.Error as ex:
            raise ex
        return dblst
    
    def createTable(self):
        sql = "CREATE TABLE IF NOT EXISTS " +self.db_cfg['db']+'''.Students 
                    (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))'''
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql) 
        except mysql.connector.Error as ex:
            raise ex

    def fetch(self,sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql) 
        except mysql.connector.Error as ex:
            raise ex  

    def insert(self,insertstmt):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(insertstmt) 
        except mysql.connector.Error as ex:
            raise ex    
            
    def closedbconnection(self):
        '''
            Close Database connection
        '''
        if self.conn.is_connected():
            try:
                self.conn.close()
                self.conn=None
            except mysql.connector.Error as ex:
                raise ex
