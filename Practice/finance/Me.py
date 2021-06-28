# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:01:08 2021

@author: Ashok Kumar Jha
"""
import pandas as pd
from datetime import datetime as dt

cyear = dt.now().year

df = pd.DataFrame(
        {
            "Name": [
                        "Jha, Ashok Kumar",
                        "Jha, Sharda",
                        "Jha, Aayiush",
                        "Jha, Devbrata"
                    ],
            "Age": [cyear-1975, cyear-1977, cyear-2003, cyear-2006],
            "Sex": ["Male", "Female", "Male", "Male"],
            "Edu": [
                        "Graduate In Electronics and Telecommunication",
                        "Master Bi-Technology, Gate , CSIR-NET, SSC,etc..",
                        "XII-Science",
                        "IX"
                  ],
            "Prof": [
                        "IT,EDU",
                        "Teaching",
                        "Student",
                        "Student"
                  ]
        }
   )
print(df)
print(df['Age'])
