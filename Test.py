import main as m
import unittest


class ftest(unittest.TestCase):
    def test(self):
        self.assertEqual(m.login("juan", "1234"), True)


if __name__ == '__main__':
    unittest.main()
