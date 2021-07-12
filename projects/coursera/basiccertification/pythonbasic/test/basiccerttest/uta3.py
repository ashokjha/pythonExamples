# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:26:25 2021

@author: Ashok Kumar Jha
"""

import unittest
import os

from src.basiccert.asgn3 import a3 

class testa3(unittest.TestCase):
    
    def setUp(self):
        ''
        #self.databfile = os.path.join('testdata','test_b_data')
        #self.datawfile = os.path.join('testdata','test_w_data')
        #self.words_file = open(self.datawfile)
        #self.words = a3.read_words(self.words_file)
        #self.words_file.close()
        #self.brd_file = open(self.databfile)
        #self.board = a3.read_board(self.brd_file)
        #self.brd_file.close()        

    def tearDown(self):
        #self.databfile = None
        #self.datawfile = None
        #self.words_file = None
        #self.words = None
        #self.brd_file = None
        #self.board = None          
        print('Cleaned')
        
    def testnum_words_on_board(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        words = ['ANT', 'BOX', 'SOB', 'TO','NTT']
        self.assertEqual(a3.num_words_on_board(board, words),4)
        
    def testword_score(self): 
        word= 'PYTHON'
        self.assertEqual(a3.word_score(word),6)

if __name__ == '__main__':
    unittest.main()
       