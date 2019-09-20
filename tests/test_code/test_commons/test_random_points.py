from unittest import TestCase

from code.commons import Point, generate_random_points


class RandomPointsTest(TestCase):

    def setUp(self):
        self.prepared_data = [
            Point(x=1.0, y=1.0)
            for i in range(10)
        ]

    def test_generation(self):
        self.assertListEqual(
            self.prepared_data,
            generate_random_points(1.0, 1.0, 10)
        )
