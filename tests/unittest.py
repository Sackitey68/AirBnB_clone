#!/usr/bin/python3
import unittest

def calculate_mul(a, b):
	return a * b

class TestCalculateProduct(unittest.TestCase):

def test_calcuate_mul_positive_numbers(self):
	result=calculate_mul(3, 4)
	self.assertEqual(result, 12)

def test_calcuate_mul_negative_numbers(self):
        result=calculate_mul(-5, -10)
        self.assertEqual(result, 50)

def test_calcuate_mul_zero(self):
        result=calculate_mul(0, 0)
        self.assertEqual(result, 0)

if _name_=='__main__':
	unittest.main()

