import unittest
from Examen2 import MiClase

class TestCocinero(unittest.TestCase):
    def test_init(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.Valencia, 5)
        self.assertEqual(mc.Tempo, 120)
        self.assertEqual(mc.Tonos, 12)
        self.assertEqual(mc.listaCanciones, ["Canción 1", "Canción 2", "Canción 3"])
        self.assertEqual(mc.listaBailabilidad, [0.8, 0.9, 0.7])

    def test_ObtieneValencia(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.ObtieneValencia(1234567), 4)

    def test_DivisibleTempo(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.DivisibleTempo(10), [1, 2, 5, 10])

    def test_ObtieneMasBailable(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)

    def test_VerificaListaCanciones(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertTrue(mc.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))

if __name__ == '__main__':
    unittest.main()
