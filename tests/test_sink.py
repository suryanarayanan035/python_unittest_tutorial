import unittest

from unit_testing.sink import FileSink

from os.path import isfile
import os
class TestFileSink(unittest.TestCase):
    def tearDown(self):
        if isfile('test.json'):
            os.remove('test.json')
    def test_sink(self):
        FileSink.sink("sample_data", "test.json")
        self.assertTrue(isfile('test.json'))
