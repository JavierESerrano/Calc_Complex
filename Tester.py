import unittest
import main as cplx


class SumTest(unittest.TestCase):
    def test_SumCplx(self):
        c1 = (3,8)
        c2 = (6,-8.6)
        suma = cplx.sumacmpl(c1,c2)
        self.assertAlmostEqual(suma[0], 9)  # add assertion here
        self.assertAlmostEqual(suma[1], -0.6)

    def test_SumCplx2(self):
        c1 = (3.7,10.8)
        c2 = (2.3,-18.6)
        suma = cplx.sumacmpl(c1,c2)
        self.assertAlmostEquals(suma[0], 6)  # add assertion here
        self.assertAlmostEquals(suma[1], -7.8)


if __name__ == '__main__':
    unittest.main()
