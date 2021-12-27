# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:58:37 2021

@author: Abhiroop
"""
import dbconnection as db


def cancel():
    """Cancell Bus Booking."""
    pid = input("Enter Passenger ID : ")
    con = db.getbusconnection()
    cur = con.cursor()

    cur.execute("SELECT * FROM  bkingdetails where passid=%s", (pid,))
    data = cur.fetchone()
    if data is None:
        print("No Booking  Available")
        return
    status = 'CANCELLED'
    cur.execute("update bkingdetails set status = %s where passid =%s",
                (status, pid))
    con.commit()
    print("Booking Cancelled successfully")

    print("Detail information of Booked Seat")
    selectsql = "SELECT * FROM bkingdetails WHERE passid= %s"
    cur.execute(selectsql, (pid, ))
    row = cur.fetchone()

    print("{:<10} {:<15} {:<17} {:<17} {:<14} {:<10} {:<12}".format(
        "PID", "Name", "Journey Date", "Mobile No", "Seat No", "Bus ID",
        "Status"))
    print("{:<10} {:<15} {:<17} {:<17} {:<14} {:<10} {:<12}".format(
        row[0], row[2], row[5], row[4], row[3], row[1], row[6]))
    con.close()
