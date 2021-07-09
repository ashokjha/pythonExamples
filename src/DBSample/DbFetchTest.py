# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:15:33 2021

@author: USER
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="************"
  #,
  #database="ashu"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM ashu.students "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
