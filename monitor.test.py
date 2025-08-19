import unittest
from patient_vitals_monitor import check_vital_signs


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        self.assertFalse(check_vital_signs(99, 102, 70))
        self.assertTrue(check_vital_signs(98.1, 70, 98))
        self.assertTrue(check_vital_signs(101.0, 75, 98))
        self.assertFalse(check_vital_signs(94.5, 75, 98))
        self.assertFalse(check_vital_signs(103, 75, 98))
        self.assertTrue(check_vital_signs(98.6, 80, 98))
        self.assertTrue(check_vital_signs(98.6, 61, 98))
        self.assertTrue(check_vital_signs(98.6, 99, 98))
        self.assertFalse(check_vital_signs(98.6, 50, 98))
        
if __name__ == '__main__':
  unittest.main()


