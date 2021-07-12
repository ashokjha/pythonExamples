# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:07:59 2021

@author: Ashok Kumar Jha
"""

import unittest

from src.basiccert.asgn2 import a2 

class testa2(unittest.TestCase):
  
    def setUp(self):
        self.a = 5
        self.b = 15

    def tearDown(self):
        print('Executed')

    def testget_complement(self):
        nct = 'C'
        self.assertEqual(a2.get_complement(nct),'G')
       
    def testget_complementary_sequence(self):
        dna = 'ATCGGC'
        self.assertEqual(a2.get_complementary_sequence(dna),'TAGCCG')
    
    def testcount_nucleotides(self):
        dna, nucleotide = 'ATCGGC', 'G' 
        self.assertEqual(a2.count_nucleotides(dna, nucleotide),2)   
        
    def testcontains_sequence(self): 
        dna1, dna2 = 'ATCGGC', 'GT'
        self.assertEqual(a2.contains_sequence(dna1, dna2),False)

    def testis_valid_sequence(self):
        dna = 'ATCGGC'
        self.assertEqual(a2.is_valid_sequence(dna), True)
        
    def testis_valid_sequence1(self):
        dna = 'AtcGC'
        self.assertEqual(a2.is_valid_sequence(dna), False) 
        
if __name__ == '__main__':
    unittest.main()
       