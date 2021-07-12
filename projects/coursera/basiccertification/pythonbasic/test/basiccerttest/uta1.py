# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 09:27:29 2021

@author: Ashok Kumar Jha
"""
import unittest

from src.basiccert.asgn1 import a1 


class testa1c(unittest.TestCase):
  
    def setUp(self):
        self.a = 5
        self.b = 15

    def tearDown(self):
        
        print('Executed')
        
    def testseconds_difference(self):
        time_1, time_2 = 1800.0, 2160.0
        self.assertEqual(a1.seconds_difference(time_1, time_2),time_2-time_1)
        
    def testhours_difference(self):
        t1,t2  = 3600.0, 1800.0
        self.assertEqual(a1.hours_difference(t1,t2),(t2-t1)/3600)

    def testto_float_hours(self):
        h, m, s =  2, 45, 9
        self.assertEqual(a1.to_float_hours(h, m, s),(h + (m + s/60)/60))
    
    
    def testto_24_hour_clock(self):
        hour = 34.65
        self.assertEqual(a1.to_24_hour_clock(hour),hour % 24)
    
    
    def testget_hours(self):
        timeinsec = 3280
        self.assertEqual(a1.get_hours(timeinsec),timeinsec//3600)
    
    
    def testget_minutes(self):
        timeinsec = 124531     
        self.assertEqual(a1.get_minutes(timeinsec),(timeinsec%3600)//60)
    
    
    def testget_seconds(self):
        timeinsec = 124531     
        self.assertEqual(a1.get_seconds(timeinsec),(timeinsec%3600)%60)
    
    
    def testtime_to_utc(self):
        utc_offset, time = -11, 18.0
        self.assertEqual(a1.time_to_utc(utc_offset, time),
                         a1.to_24_hour_clock(24 + time - utc_offset))
     
    def testtime_from_utc(self):
        utc_offset, time = -7, 6.0
        self.assertEqual(a1.time_from_utc(utc_offset, time),
                         a1.to_24_hour_clock(24 + time + utc_offset))


if __name__ == '__main__':
    unittest.main()
