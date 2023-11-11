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

        # prueba 2
        mc2 = MiClase(30, 210, 10, ["I'm Still standing Elton John", "Sirius Alan Parson", "Take on me a-ha"], [0.4, 0.6, 0.5])
        self.assertEqual(mc2.Valencia, 30)
        self.assertEqual(mc2.Tempo, 210)
        self.assertEqual(mc2.Tonos, 10)
        self.assertEqual(mc2.listaCanciones, ["I'm Still standing Elton John", "Sirius Alan Parson", "Take on me a-ha"])
        self.assertEqual(mc2.listaBailabilidad, [0.4, 0.6, 0.5])

    def test_ObtieneValencia(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.ObtieneValencia(1234567), 4)

        # prueba 2
        mc2 = MiClase(30, 210, 10, ["I'm Still standing Elton John", "Sirius Alan Parson", "Take on me a-ha"], [0.4, 0.6, 0.5])
        self.assertEqual(mc2.ObtieneValencia(34567), 3)
        
    def test_DivisibleTempo(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.DivisibleTempo(10), [1, 2, 5, 10])

        # prueba 2
        mc2 = MiClase(30, 210, 10, ["I'm Still standing Elton John", "Sirius Alan Parson", "Take on me a-ha"], [0.4, 0.6, 0.5])
        self.assertEqual(mc2.DivisibleTempo(20), [1, 2, 4, 5, 10, 20])

    def test_ObtieneMasBailable(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)

        # prueba 2
        mc2 = MiClase(30, 210, 10, ["I'm Still standing Elton John", "Sirius Alan Parson", "Take on me a-ha"], [0.4, 0.6, 0.5])
        self.assertEqual(mc2.ObtieneMasBailable([0.4, 0.6, 0.5]), 0.6)

    def test_VerificaListaCanciones(self):
        # prueba 1
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertTrue(mc.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))

        # prueba 2
        mc2 = MiClase(30, 210, 10, ["I'm Still standing Elton John", "Sirius Alan Parson", "Take on me a-ha"], [0.4, 0.6, 0.5])
        self.assertTrue(mc2.VerificaListaCanciones(["I'm Still standing Elton John", "Sirius Alan Parson", "Take on me a-ha"]))

if __name__ == '__main__':
    unittest.main()
