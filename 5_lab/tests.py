import unittest
from lab import Rocket, Rocket_2
import time


class TestMyLab(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Виконається лише один раз")
        cls.name = "Ares V"
        cls.mass = 3700000.0

    def setUp(self) -> None:
        print("Створюємо обєкт")
        self.obj = Rocket_2(self.name, self.mass)

    def tearDown(self) -> None:
        del self.obj

    def test_converter_correct(self):
        for mass in [3700000, 3800000]:
            obj = Rocket("Ares V", mass)
            self.assertAlmostEqual(obj.convert_mass(), mass * 2.20462262)

    def test_obj_correct(self):
        self.assertIsInstance(self.obj, Rocket)
        for class_type in [str, int, float]:
            self.assertNotIsInstance(self.obj, class_type)

    def test_correct_attributes(self):
        self.assertEqual(self.obj.name, self.name)
        self.assertEqual(self.obj.mass, self.mass)
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(self.obj.mass, float)

    def test_info(self):
        self.assertIn(self.obj.name, self.obj.info)
        self.assertIn(str(self.obj.mass), self.obj.info)
        self.assertIn(self.obj.name, self.obj.info_en)
        self.assertIn(str(self.obj.convert_mass()), self.obj.info_en)
    
    def test_fail_github_actions(self):
        #for i in range(5):
        #    time.sleep(5)
        #    print(f"Запускаємо тест {i}")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
