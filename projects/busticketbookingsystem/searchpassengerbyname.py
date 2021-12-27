# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:52:33 2021

@author: Abhiroop
"""
import dbconnection as db


def search():
    """Search Passenger by Name."""
    pname = input("Enter Passenger name few or all parts of name : ")
    con = db.getbusconnection()
    cur = con.cursor()
    cur.execute("SELECT * FROM  bkingdetails where passname like '"+pname+"%'")

    datas = cur.fetchall()
    print("{:<10} {:<15} {:<17} {:<17} {:<14} {:<10} {:<12}".format(
        "PID", "Name", "Journey Date", "Mobile No", "Seat No", "Bus ID",
        "Status"))
    for data in datas:
        print("{:<10} {:<15} {:<17} {:<17} {:<14} {:<10} {:<12}".format(
            data[0], data[2], data[5], data[4], data[3], data[1], data[6]))
    con.close()
