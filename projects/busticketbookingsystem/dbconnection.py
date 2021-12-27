# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 17:49:25 2021

@author: Ashok Kumar Jha
"""

import mysql.connector as mycon


def getconnection():
    """Return DB connection for default schema."""
    return mycon.connect(
        host="localhost",
        user="root",
        password="Ashu.Kr.Jha@gma1l.c0m"
    )


def getbusconnection():
    """Return connection to Bus Database connection."""
    return mycon.connect(
        host="localhost",
        database='onlinebusbk',
        user="root",
        password="Ashu.Kr.Jha@gma1l.c0m"
    )
