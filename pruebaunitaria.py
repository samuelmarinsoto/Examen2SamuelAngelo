import unittest
from Examen2 import MiClase

class Prueba(unittest.TestCase):
    def probar_init(self):
        mc = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(mc.Valencia, 5)
        self.assertEqual(mc.Tempo, 120)
        self.assertEqual(mc.Tonos, 12)
        self.assertEqual(mc.listaCanciones, ["Canción 1", "Canción 2", "Canción 3"])
        self.assertEqual(mc.listaBailabilidad, [0.8, 0.9, 0.7])

if __name__ == '__main__':
    unittest.main()
