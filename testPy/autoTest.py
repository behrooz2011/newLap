#!/usr/bin/env python

from rearrange import rearrange_name
import unittest

class TestArrange(unittest.TestCase):
    def testttbasic(self):
        testcase = "Lovable, Dario"
        expected = "Dario Lovable"
        self.assertEqual(rearrange_name(testcase),expected)
unittest.main()