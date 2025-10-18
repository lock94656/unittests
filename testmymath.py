import mymath
import unittest

class TestMyMath(unittest.TestCase):
	"""Test absolute function for different values"""
	def test_upper(self):
		"""Test for values greater than 0"""
		self.assertEqual(abs(2.1), 2.1)
		self.assertEqual(abs(5.2), 5.2)
		self.assertEqual(abs(789), 789)
		
	def test_lower(self):
		"""Test for values lower than 0"""
		self.assertEqual(abs(-2.58), 2.58)
		self.assertEqual(abs(-3.56), 3.56)
		self.assertEqual(abs(-789), 789)
		
	def test_zero(self):
		"""Test for values equal to 0"""
		self.assertEqual(abs(0), 0)
		self.assertEqual(abs(0.0), 0.0)
		self.assertEqual(abs(-0.0), 0.0)
		
if __name__ == '__main__':
	unittest.main()