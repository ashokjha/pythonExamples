# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 20:00:23 2021

@author: Ashok Kumar Jha
"""
import dbconnection as db


def show():
    """Show all buses."""
    con = db.getbusconnection()
    cur = con.cursor()
    cur.execute("SELECT * FROM  busdetails")
    print("Following bus service are available")
    data = cur.fetchall()
    print("{:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "Bus ID", "Bus Name", "From Locaion", "To Location", "Start Time",
        "Stop Time", "Total Seat", "Fare"))
    for row in data:
        print("{:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    con.close()
