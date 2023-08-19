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

class ResTest(unittest.TestCase):
    def test_ResCplx(self):
        c1 = (3,8)
        c2 = (6,-8.6)
        resta = cplx.restacmpl(c1,c2)
        self.assertAlmostEqual(resta[0], -3)  # add assertion here
        self.assertAlmostEqual(resta[1], 16.6)

    def test_ResCplx2(self):
        c1 = (3.7,10.8)
        c2 = (2.3,-18.6)
        resta = cplx.restacmpl(c1,c2)
        self.assertAlmostEquals(resta[0], 1.4)  # add assertion here
        self.assertAlmostEquals(resta[1], 29.4)

class MultTest(unittest.TestCase):
    def test_MultCplx(self):
        c1 = (3,8)
        c2 = (6,-8.6)
        mult = cplx.multcmpl(c1,c2)
        self.assertAlmostEqual(mult[0], 86.8)  # add assertion here
        self.assertAlmostEqual(mult[1], 22.2)

    def test_MultCplx2(self):
        c1 = (3.7,10.8)
        c2 = (2.3,-18.6)
        mult = cplx.multcmpl(c1,c2)
        self.assertAlmostEquals(mult[0], 209.39)  # add assertion here
        self.assertAlmostEquals(mult[1], -43.98)

class DivTest(unittest.TestCase):
    def test_DivCplx(self):
        c1 = (3,8)
        c2 = (6,-8.6)
        div = cplx.divcmpl(c1,c2)
        self.assertAlmostEqual(div[0], -0.46198617679156057)  # add assertion here
        self.assertAlmostEqual(div[1], 0.7893779556202255)

    def test_DivCplx2(self):
        c1 = (3.7,10.8)
        c2 = (2.3,-18.6)
        div = cplx.divcmpl(c1,c2)
        self.assertAlmostEquals(div[0], -0.5476725978647687)  # add assertion here
        self.assertAlmostEquals(div[1], 0.5961281138790036)

class ConjTest(unittest.TestCase):
    def test_ConjCplx(self):
        c1 = (3,8)
        conj = cplx.conjcmpl(c1)
        self.assertAlmostEqual(conj[0], 3)  # add assertion here
        self.assertAlmostEqual(conj[1], -8)

    def test_ConjCplx2(self):
        c1 = (3.7,10.8)
        conj = cplx.conjcmpl(c1)
        self.assertAlmostEquals(conj[0], 3.7)  # add assertion here
        self.assertAlmostEquals(conj[1], -10.8)

class ModTest(unittest.TestCase):
    def test_ModCplx(self):
        c1 = (3,8)
        mod = cplx.modcmpl(c1)
        self.assertAlmostEqual(mod, 8.54400374531753)  # add assertion here

    def test_ModCplx2(self):
        c1 = (3.7,10.8)
        mod = cplx.modcmpl(c1)
        self.assertAlmostEquals(mod, 11.416216536138407)  # add assertion here

class FaseTest(unittest.TestCase):
    def test_FaseCplx(self):
        c1 = (3,8)
        fase = cplx.fasecmpl(c1)
        self.assertAlmostEqual(fase, 1.2120256565243244)  # add assertion here

    def test_FaseCplx2(self):
        c1 = (3.7,10.8)
        fase = cplx.fasecmpl(c1)
        self.assertAlmostEquals(fase, 1.2407357143854625)  # add assertion here

class PolarTest(unittest.TestCase):
    def test_PolarCplx(self):
        c1 = (3,8)
        polar = cplx.polarcmpl(c1)
        self.assertAlmostEqual(polar[0], 8.54400374531753)  # add assertion here
        self.assertAlmostEqual(polar[1], 1.2120256565243244)

    def test_PolarCplx2(self):
        c1 = (3.7,10.8)
        polar = cplx.polarcmpl(c1)
        self.assertAlmostEquals(polar[0], 11.416216536138407)  # add assertion here
        self.assertAlmostEquals(polar[1], 1.2407357143854625)

class CarteTest(unittest.TestCase):
    def test_CarteCplx(self):
        c1 = (3,8)
        Carte = cplx.cartecmpl(c1)
        self.assertAlmostEqual(Carte[0], -0.4365001014258406)  # add assertion here
        self.assertAlmostEqual(Carte[1], 2.9680747398701453)

    def test_CarteCplx2(self):
        c1 = (3.7,10.8)
        Carte = cplx.cartecmpl(c1)
        self.assertAlmostEquals(Carte[0], -0.7190206538847388)  # add assertion here
        self.assertAlmostEquals(Carte[1], -3.629464051246019)



if __name__ == '__main__':
    unittest.main()
