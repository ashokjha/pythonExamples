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
        self.cfg = db_cfg

    def createconnection(self):
        '''
            Return Database connection Based on Configuration
        '''
        try:
             self.conn = mysql.connector.connect(host= self.cfg['host'],
                                       user= self.cfg['key'],
                                       password=self.cfg['val'] )
        except Exception as ex:
            raise ex

     
    def createdb(self,sql):
        '''
            Create Database based on configuration
            sql: Sql Statement
            Raise error in case of failure
        '''
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
        except mysql.connector.Error as ex:
            raise ex
            
    def dbList(self):
        '''
            Fetches list of existing Database based on onfiguration 
            Raise error in case of failure
        '''        
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
    
    def createTable(self,sql):
        '''
            Create Table
            Raise error in case of failure
        '''           
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql) 
        except mysql.connector.Error as ex:
            raise ex

    def alterTable(self,sql):
        '''
            Alter Table
            Raise error in case of failure
        '''  
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql) 
        except mysql.connector.Error as ex:
            raise ex

    def fetchData(self,sql):
        '''
            Fetch Data
            Raise error in case of failure
        '''   
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql) 
                data = cursor.fetchall()
                return data
        except mysql.connector.Error as ex:
            raise ex  

    def updateData(self,sql):
        '''
            Update Data
            SQL: sql to be executed
            Raise error in case of failure
        '''   
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql) 
            self.conn.commit()   
        except mysql.connector.Error as ex:
            raise ex  

    def removeData(self,sql):
        '''
            Remove Data
            SQL: sql to be executed
            Raise error in case of failure
        '''   
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql) 
            self.conn.commit()   
        except mysql.connector.Error as ex:
            raise ex 


    def insert(self,insertstmt):
        '''
            Insert Data
            Raise error in case of failure
        '''   
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(insertstmt)
            self.conn.commit()    
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
