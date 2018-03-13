import unittest
import ex3


class BasicTestCase(unittest.TestCase):

    def test_convert_dash(self):
        result = ex3.mac_converter('00-00-aa-aa-bb-bb')
        self.assertEqual(result, '00:00:AA:AA:BB:BB')

    def test_convert_dot(self):
        result = ex3.mac_converter('0000.aaaa.bbbb')
        self.assertEqual(result, '00:00:AA:AA:BB:BB')

    def test_convert_fill(self):
        result = ex3.mac_converter('a:b:c:d:e:f')
        self.assertEqual(result, '0A:0B:0C:0D:0E:0F')

    def test_error(self):
        with self.assertRaises(ValueError):
            ex3.mac_converter('000000.aaaaaa')
