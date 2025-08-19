import unittest
from patient_vitals_monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        self.assertFalse(vitals_ok(99, 102, 70))
        self.assertTrue(vitals_ok(98.1, 70, 98))
        self.assertTrue(vitals_ok(101.0, 75, 98))
        self.assertFalse(vitals_ok(94.5, 75, 98))
        self.assertFalse(vitals_ok(103, 75, 98))
        self.assertTrue(vitals_ok(98.6, 80, 98))
        self.assertTrue(vitals_ok(98.6, 61, 98))
        self.assertTrue(vitals_ok(98.6, 99, 98))
        self.assertFalse(vitals_ok(98.6, 50, 98))
if __name__ == '__main__':
  unittest.main()

