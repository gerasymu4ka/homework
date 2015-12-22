import unittest
from deviders import deviders as d

class DevidersTestCase(unittest.TestCase):
	def test_valid_range(self):
		self.assertEqual(d(1, 6), [3, 5])

	def test_invalid_range(self):
		self.assertEqual(d(1, 1), 'Last number in range have to be bigger than first')
		self.assertEqual(d(6, 1), 'Last number in range have to be bigger than first')


if __name__ == '__main__':
	unittest.main(verbosity=1) 