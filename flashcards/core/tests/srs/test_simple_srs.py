
from django.test import TestCase

from ...srs.simple_srs import SimpleSRS


class SimpleSRSTest(TestCase):
    def setUp(self):
        self.simple_srs = SimpleSRS()