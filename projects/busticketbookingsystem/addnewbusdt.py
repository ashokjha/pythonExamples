# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:55:05 2021

@author: Ashok Kumar Jha
"""

import dbconnection as db


def addbus():
    """Add New Bus in service."""
    con = db.getbusconnection()
    cur = con.cursor()
    busid = input("Enter a New Bus ID: ")
    cur.execute("select busid from busdetails where busid=%s", (busid,))
    data = cur.fetchone()
    if data is not None:
        print("Bus ID is aleady present. ")
        return
    name = input("Enter Bus Name: ")
    fromloc = input("Enter From Location: ")
    toloc = input("Enter To Location: ")
    starttime = input("Enter Start Time: ")
    stoptime = input("Enter Stop Time: ")
    fare = input("Enter Fare  in Rs. : ")
    totalseat = input("Enter Number of seats: ")
    insertstmt = """INSERT INTO busdetails(
        busid,name,fromloc,toloc,starttime,stoptime,totalseat,fare)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(insertstmt, (busid, name, fromloc, toloc, starttime,
                             stoptime, totalseat, fare))
    con.commit()
    print(cur.rowcount, " record inserted")
    print("Showing all Buses")
    cur.execute("SELECT * FROM  busdetails ")
    data = cur.fetchall()
    print("{:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "Bus ID", "Bus Name", "From Locaion", "To Location", "Start Time",
        "Stop Time", "Total Seat", "Fare"))
    for row in data:
        print("{:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    con.close()
