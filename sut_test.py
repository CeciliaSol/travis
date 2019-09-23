import unittest 
import sut
from unittest.mock import MagicMock
import math

class TestSut(unittest.TestCase):

	def tests_area(self):
		area = sut.area(3,2)
		self.assertTrue(area==6)

	def tests_saludar(self):	
		saludar = sut.saludar('cecilia')
		self.assertTrue(saludar =='hola' + 'cecilia')

	def tests_sumar(self):
		resultado = sut.sumar(3,2)
		self.assertTrue(resultado==5)

	def test_multiplicar(self):
		self.assertEqual(sut.multiplicar(2,5),10)

	def test_valor_absoluto(self):
		pass


	def tests_comparar_a_menor_que_b(self):
		self.assertEqual(sut.comparar(1,10),"A menor que B")
    
	def test_comparar_a_mayor_que_b(self):
		self.assertNotEqual(sut.comparar(2,0),"B menor que A")

	def test_comparar_a_y_b_son_iguales(self):
		self.assertEqual(sut.comparar(5,5),"A y B son iguales")


	def test_costototal(self):
		sut.sumar=MagicMock(return_value= 2)
		a = sut.costototal(1,4)
		self.assertEqual(a, "El costo total es $2")
    
	def test_supercalc(self):
		math.exp=MagicMock(return_value=2)
		math.sqrt=MagicMock(return_value=2)
		a = sut.supercalc(3)
		self.assertTrue(a == 2)		



if __name__ == '__main__':
	unittest.main()