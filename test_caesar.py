from caesar import encode, decode
import unittest

class CaesarTestCase(unittest.TestCase):
	def test_encode_valid(self):
		self.assertEqual(encode('Google forever', 5), 'Gttlqj ktwjajw')
		
	def test_encode_invalid(self):
		self.assertEqual(encode('Google forever', 30), 'Invalid key!')
		self.assertEqual(encode('Google forever', 0), 'Invalid key!')

	def test_decode_valid(self):
		self.assertEqual(decode('Gttlqj ktwjajw', 5), 'Google forever')

	def test_decode_invalid(self):
		self.assertEqual(decode('Gttlqj ktwjajw', 30), 'Invalid key!')
		self.assertEqual(decode('Gttlqj ktwjajw', 0), 'Invalid key!')


if __name__ == '__main__':
	unittest.main(verbosity=1) 
