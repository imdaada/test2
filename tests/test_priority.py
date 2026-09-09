import unittest
from priority import normalize_priority
class PriorityTests(unittest.TestCase):
    def test_values(self):
        for value in ("low", "normal", "high"):
            self.assertEqual(normalize_priority(value), value)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            normalize_priority("urgent")
