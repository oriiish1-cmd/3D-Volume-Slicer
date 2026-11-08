import unittest
import numpy as np
import sys
import os

# Add the main project folder to the path so we can import from Ex0
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Ex0 import parse_csv_line, validate_plane

class TestEx0(unittest.TestCase):

    def test_parse_csv_line_valid(self):
        """Test that the function correctly parses a valid line and ignores the point count at the start."""
        line = ["3.0", "0", "0", "0", "1", "0", "0", "0", "1", "0"]
        points = parse_csv_line(line)
        self.assertEqual(len(points), 3) # Should create exactly 3 points
        np.testing.assert_array_equal(points[0], np.array([0.0, 0.0, 0.0]))

    def test_parse_csv_line_invalid_count(self):
        """Test that an error is raised when coordinates are missing in the row."""
        line = ["3.0", "1", "2", "3", "4", "5", "6", "7", "8"] # 8 coordinates instead of 9
        with self.assertRaises(ValueError):
            parse_csv_line(line)

    def test_validate_plane_valid_triangle(self):
        """Test a valid isosceles triangle - should pass and return 4 vertices."""
        points = [
            np.array([0, 1, 0]),  # Top vertex (a1)
            np.array([-1, 0, 0]), # Left vertex (b)
            np.array([1, 0, 0])   # Right vertex (c)
        ]
        a1, a2, b, c = validate_plane(points)
        np.testing.assert_array_equal(a1, a2) # For a triangle, the two top vertices must be identical

    def test_validate_plane_not_isosceles(self):
        """Test a triangle that is not isosceles - should raise an error."""
        points = [
            np.array([0, 1, 0]),
            np.array([-2, 0, 0]), # Left leg is longer
            np.array([1, 0, 0])
        ]
        with self.assertRaises(ValueError):
            validate_plane(points)

    def test_validate_plane_invalid_trapezoid(self):
        """Test a trapezoid where the top base is larger than the bottom base - should raise an error."""
        points = [
            np.array([-2, 1, 0]), # a1
            np.array([ 2, 1, 0]), # a2 - top base length is 4
            np.array([-1, 0, 0]), # b
            np.array([ 1, 0, 0])  # c - bottom base length is 2
        ]
        with self.assertRaises(ValueError):
            validate_plane(points)

if __name__ == '__main__':
    unittest.main()