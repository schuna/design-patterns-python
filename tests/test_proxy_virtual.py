from unittest import TestCase

from parameterized import parameterized

from src.design_patterns.proxy.virtual import Bitmap, LazyBitmap


class TestVirtualProxy(TestCase):
    @parameterized.expand([
        (Bitmap("flower.png"), "Drawing image flower"),
        (LazyBitmap("flower.png"), "Drawing image flower")
    ])
    def test_draw_when_called_return_drawing_image_name(self, bitmap, expected):
        bitmap.draw()
        actual = bitmap.draw()
        self.assertEqual(expected, actual)

    def test_Bitmap_when_initialized_load_image(self):
        actual = Bitmap("flower.png").image
        self.assertEqual("flower", actual)

    def test_LazyBitmap_when_initialized_not_load_image(self):
        actual = LazyBitmap("flower.png").image
        self.assertEqual(None, actual)
