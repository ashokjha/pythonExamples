# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:50:25 2021

@author: Abhiroop
"""

import dbconnection as db


def createdb():
    """Return DB connection for default schema."""
    con = db.getconnection()
    cur = con.cursor()
    sqlscript = "CREATE DATABASE if not exists onlinebusbk"
    cur.execute(sqlscript)
    sqlscript = "use onlinebusbk"
    cur.execute(sqlscript)

    sqlscript = '''CREATE TABLE if not exists login
    (user VARCHAR(15) primary key, pass VARCHAR(15) NOT NULL)'''
    cur.execute(sqlscript)

    sqlscript = '''insert ignore into login (user,pass)
                   values('bkadmin','A123456')'''
    cur.execute(sqlscript)

    sqlscript = '''CREATE TABLE if not exists busdetails (
                        busid VARCHAR(5) primary key,
                        name VARCHAR(20) NOT NULL,
                        fromloc VARCHAR(20) NOT NULL,
                        toloc  VARCHAR(20) NOT NULL,
                        starttime VARCHAR(10) NOT NULL,
                        stoptime VARCHAR(10) NOT NULL,
                        totalseat VARCHAR(2) NOT NULL,
                        fare VARCHAR(4) NOT NULL
                   )'''
    cur.execute(sqlscript)

    sqlscript = '''CREATE TABLE if not exists bkingdetails (
                        passid VARCHAR(6) primary key,
                        busid VARCHAR(5) NOT NULL,
                        passname VARCHAR(20) NOT NULL,
                        seatno VARCHAR(3) NOT NULL,
                        mobileno  VARCHAR(13) NOT NULL,
                        dateofjourney VARCHAR(10) NOT NULL,
                        status VARCHAR(10) NOT NULL,
                        FOREIGN KEY (busid)
                            REFERENCES busdetails(busid)
                   )'''
    cur.execute(sqlscript)

    con.commit()
    con.close()
    print("""Database with tables and user created successfully """)
