import unittest
from lab import Rocket

class TestMyLab(unittest.TestCase):
    def test_converter_correct(self):
        for mass in [3700000, 3800000]:
            obj = Rocket("Ares V", mass)
            self.assertAlmostEqual(obj.convert_mass(), mass * 2.20462262)
        self.assertTrue(False)
    
    def test_mock(self):
        pass
    
    def tt(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)