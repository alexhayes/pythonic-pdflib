from __future__ import absolute_import
from django.utils import unittest
from ..helpers import *

class ToOptlistTestCase(unittest.TestCase):
    
    def test_false(self):
        self.assertEqual(to_optlist(None), '')
        self.assertEqual(to_optlist(False), '')
        self.assertEqual(to_optlist({}), '')
        
    def test_string(self):
        self.assertEqual(to_optlist(''), '')
        self.assertEqual(to_optlist('font=1'), 'font=1')
        
    def test_dict(self):
        self.assertEqual(to_optlist({'eggs': 1}), 'eggs=1')
        self.assertEqual(to_optlist({'eggs': 1, 'spam': 'asdf'}), 'eggs=1 spam=asdf')
        self.assertEqual(to_optlist({'eggs': (1, 3), 'spam': 'asdf'}), 'eggs={1 3} spam=asdf')

