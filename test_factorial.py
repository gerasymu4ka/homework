import unittest
from factorial import factorial

class FactorialTestCase(unittest.TestCase):
	def test_factorial(self):
		self.assertEqual(factorial(4), 24)

	def test_zero(self):
		self.assertEqual(factorial(0), 'Factorial of 0 is 1')

	def test_minus(self):
		self.assertEqual(factorial(-6), "Factorial doesn't exist")



if __name__ == '__main__':
	unittest.main(verbosity=1) 