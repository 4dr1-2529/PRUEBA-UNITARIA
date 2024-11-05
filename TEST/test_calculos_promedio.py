# Test/test_calculos_promedio.py

import unittest
from SRC.calculos_promedio import CalculosPromedio

class TestCalculosPromedio(unittest.TestCase):
    def setUp(self):
        self.calculos = CalculosPromedio()

    def tearDown(self):
        self.calculos = None

    def test_calcular_promedio(self):

        conjunto = [1, 2, 3, 4, 5]
        resultado_esperado = 3.0
        resultado_actual = self.calculos.calcular_promedio(conjunto)
        self.assertEqual(resultado_esperado, resultado_actual)


        conjunto = [10, 20, 30, 40, 50]
        resultado_esperado = 30.0
        resultado_actual = self.calculos.calcular_promedio(conjunto)
        self.assertEqual(resultado_esperado, resultado_actual)

    def test_promedio_lista_vacia(self):

        conjunto = []
        resultado_actual = self.calculos.calcular_promedio(conjunto)
        self.assertIsNone(resultado_actual)

if __name__ == '__main__':
    unittest.main()
