import unittest

from design_patterns.bridge.shape_renderer import Square, VectorRenderer, RasterRenderer, Triangle


class Evaluate(unittest.TestCase):
    def test_square_vector(self):
        sq = Square(VectorRenderer())
        self.assertEqual(str(sq), 'Drawing Square as lines')

    def test_pixel_triangle(self):
        tr = Triangle(RasterRenderer())
        self.assertEqual(str(tr), 'Drawing Triangle as pixels')
