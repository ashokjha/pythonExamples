# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:56:33 2021

@author: Abhiroop
"""
import dbconnection as db


def book():
    """Book Ticket."""
    con = db.getbusconnection()
    cur = con.cursor()

    print("Find Blank Seat")
    doj = input("Enter date of journey in yyyy-mm-dd format e.g. 2022-12-26: ")
    busid = input("Enter Bus Id: ")
    cur.execute("SELECT * FROM  busdetails where busid=%s", (busid,))
    data = cur.fetchone()
    if data is None:
        print("Bus Not Available")
        return
    numberofseat = data[6]

    seatno = input("Enter Seat No: ")

    selectsql = """SELECT * FROM bkingdetails WHERE dateofjourney = %s AND
                busid = %s AND seatno = %s AND status = 'CONFIRMED'"""
    cur.execute(selectsql, (doj, busid, seatno))
    data = cur.fetchone()
    if data is not None:
        print("Seat already booked")
        print("{:<10} {:<15} {:<17} {:<17} {:<14} {:<10} {:<12}".format(
            "PID", "Name", "Journey Date", "Mobile No", "Seat No", "Bus ID",
            "Status"))
        print("{:<10} {:<15} {:<17} {:<17} {:<14} {:<10} {:<12}".format(
            data[0], data[2], data[5], data[4], data[3], data[1], data[6]))
        return
    if(int(seatno) > int(numberofseat)):
        print("Invalid seat")
        return

    print("Yes, Seat is available.")
    pid = input("Enter New Passenger id:  ")
    selectsql = "SELECT * FROM bkingdetails WHERE passid= %s"
    cur.execute(selectsql, (pid, ))
    data = cur.fetchone()
    if data is not None:
        print("Passenger ID is already present.")
        return

    passname = input("Enter Name:  ")
    mobileno = input("Enter Mobile No:  ")
    status = "CONFIRMED"
    insersql = """INSERT INTO bkingdetails (passid, busid, passname, seatno,
    mobileno, dateofjourney, status) values (%s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(insersql, (pid, busid, passname, seatno, mobileno,
                           doj, status))
    con.commit()
    print(cur.rowcount, " record inserted")

    print("Detail information of Booked Seat")
    selectsql = "SELECT * FROM bkingdetails WHERE passid= %s"
    cur.execute(selectsql, (pid, ))
    row = cur.fetchone()

    print("{:<10} {:<15} {:<17} {:<17} {:<14} {:<10} {:<12}".format(
        "PID", "Name", "Journey Date", "Mobile No", "Seat No", "Bus ID",
        "Status"))
    print("{:<10} {:<15} {:<17} {:<17} {:<14} {:<10} {:<12}".format(
        row[0], row[2], row[5], row[4], row[3], row[1], row[6]))

    print("Bus Details")
    cur.execute("SELECT * FROM  busdetails where busid=%s", (busid,))
    row = cur.fetchone()
    print("{:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "Bus ID", "Bus Name", "From Locaion", "To Location", "Start Time",
        "Stop Time", "Total Seat", "Fare"))
    print("{:<10} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    con.close()
