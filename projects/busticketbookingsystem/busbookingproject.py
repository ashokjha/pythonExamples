# -*- coding: utf-8 -*
"""
Created on Fri Dec 24 17:47:53 2021

@author: Abhiroop
"""
# Menu driven application for bus booking

import dbconnection as db
import addnewbusdt
import booknewticket
import cancelticket
import createdb
import searchbusbyname
import searchpassengerbyname
import showallbooking
import showallbuses
import showallcancelbooking

WELCOMEMSG = '''
        ###################################################################
        \t\tWelcome to Online Bus Ticket Booking
        ###################################################################
        *******************************************************************
        *******************************************************************'''


def welcome():
    """Welcome."""
    print(WELCOMEMSG)


def authenticate():
    """Authenticate USER."""
    con = db.getbusconnection()
    cursor = con.cursor()
    print("Please login to continue")

    while(1):
        uid = input("Please Enter User ID : ")
        pwd = input("Please Enter Pssword : ")
        cursor.execute(
            "select user from login where user = %s and pass = %s", (uid, pwd))
        data = cursor.fetchone()
        if data is None:
            print("User ID or password is incorrect! Please try again.. ")
            continue
        break
    con.close()
    return True


def bookingsystem():
    """Booking System."""
    welcome()
    infotext = '''\t\t\tSystem does following
            \t1. TO CREATE BUS DATABASE, BUS DETAIL AND PASSENGER TABLE
            \t2. TO ADD NEW BUS DETAILS
            \t3. TO BOOK A NEW TICKET
            \t4. TO CANCEL A TICKET
            \t5. TO SHOW ALL THE BUS DETAILS
            \t6. TO SHOW ALL THE DETAILS OF BUS TICKET BOOKING
            \t7. TO SHOW ALL THE DETAILAS OF CANCEL BUS TICKETS
            \t8. TO SEARCH A BUS DETAILS BY NAME
            \t9. TO SEARCH A PASSENGER DETAILS BY NAME
            \t10. EXIT
            ***************************************************************
            ***************************************************************
           '''

    print(infotext)

    option = "Enter required service from  1~10 options e.g. 3 : "
    choice = int(input(option))
    authenticated = False

    while(1):
        if choice == 1:
            createdb.createdb()
            choice = int(input(option))
        else:
            if not authenticated:
                authenticated = authenticate()
            if choice == 2:
                addnewbusdt.addbus()
                choice = int(input(option))
            elif choice == 3:
                booknewticket.book()
                choice = int(input(option))
            elif choice == 4:
                cancelticket.cancel()
                choice = int(input(option))
            elif choice == 5:
                showallbuses.show()
                choice = int(input(option))
            elif choice == 6:
                showallbooking.show()
                choice = int(input(option))
            elif choice == 7:
                showallcancelbooking.show()
                choice = int(input(option))
            elif choice == 8:
                searchbusbyname.search()
                choice = int(input(option))
            elif choice == 9:
                searchpassengerbyname.search()
                choice = int(input(option))
            elif choice == 10:
                print("Thank you. ")
                break


if __name__ == '__main__':
    bookingsystem()
