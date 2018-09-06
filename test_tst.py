# coding = utf-8

import unittest
from tst import Tst


class TestTst(unittest.TestCase):
    def setUp(self):
        self.t = Tst('sddd')
        print('this is setup')

    def tearDown(self):
        print('this is teardown')

    def test_get_pathname(self):
        print('testing get pathname')
        self.assertEqual(self.t.get_pathname(), 'sddd')

    def test_get_nothing(self):
        print('testing get nothing')
        self.assertEqual(self.t.get_nothing(), 'nothing')


if __name__ == '__main__':
    unittest.main()
