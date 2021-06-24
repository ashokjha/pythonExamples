# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:45:33 2021

@author: Ashok Kumar Jha
"""

def createdbsql(db):
    '''
    Return DB create SQL
    db: Database name with other criteria
    '''
    return "CREATE DATABASE IF NOT EXISTS "+db


def updateDdlTSql(table,column):
    '''
        return update sql 
        db: database name
        table: Table
        column : Column To add with datatype and other criterias
        
    '''
    return " ALTER TABLE "+table + " " +column 


def alterDdlSql(table,column):
    '''
        return alter sql 
        db: database name
        table: Table
        Column : Column To remove
        Prerequisite : No contraint on column
        
    '''
    return " ALTER TABLE "+table + " DROP COLUMN " +column 


def createDdlTbSql():
    '''
        return create sql 
    '''     
    return '''CREATE TABLE IF NOT EXISTS ashu.Students 
                    (id INT AUTO_INCREMENT PRIMARY KEY, 
                    name VARCHAR(255))
          '''
          
def insertSql(data):
    '''
        return insert sql 
    '''     
    return '''insert into ashu.Students (name,entrydate)
                    VALUES ('{name}','{entrydate}')
          '''.format(**data)    
          
def updateRecordSql(data):
    '''
        return update sql 
    '''     
    return '''UPDATE ashu.Students set name ='{name}'
                    where id={id}
          '''.format(**data)    

def removeRecordSql(cnd):
    '''
        return remove data sql 
        cnd: Id of record
    '''     
    return "DELETE from ashu.students where id ="+str(cnd)
            


def fetchsql() :
    '''
        return fetch sql 

    '''     
    return "select * from ashu.Students"