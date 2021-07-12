# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:22:35 2021

@author: Ashok Kumar Jha
"""
import unittest

from src.rdb.DBSample import DBConnection 


class testmysqldb(unittest.TestCase):
  
    def setUp(self):
        self.cfg = {'host':"localhost", 'id':'root',
                        'key':'Ashu.Kr.Jha@gma1l.c0m'}
        self.dbs = DBConnection(self.cfg)
        

    def tearDown(self):
        print('Cleaned')
        
    def testdbconnection(self):
        self.assertTrue(self.dbs.checkconnection())
        
    def testexistingdb(self):
        self.assertNotEqual(self.dbs.existingdb(), [])
    
    def testgetResult(self):
        self.assertNotEqual(self.dbs.getresult('SELECT * FROM ashu.students'), [])
    

if __name__ == '__main__':
    unittest.main()


