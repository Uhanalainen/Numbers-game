import unittest
from number_game import calculate

class NumGameTests(unittest.TestCase):
	def test_calculate_should_raise_value_error_if_input_is_None(self):
		with self.assertRaises(ValueError):
			calculate(None)

	def test_calculate_should_raise_value_error_if_input_is_str(self):
		with self.assertRaises(ValueError):
			calculate("test")

	def test_calculate_should_raise_error_if_no_input_is_given(self):
		with self.assertRaises(TypeError):
			calculate()

	def test_calculate_should_be_at_least_two_digits(self):
		self.assertEqual(
			calculate(1),
			"The number should have at least two digits"
		)

	def test_calculate_number_should_not_start_with_zero(self):
		self.assertEqual(
			calculate(01),
			"The number can't start with 0"
		)

if __name__ == "__main__":
	unittest.main()