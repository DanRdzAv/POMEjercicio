import sys
import os
from selenium import webdriver
import time
import unittest
base_dir = os.path.dirname(__file__) or '.'
sys.path.append("..")
from Pages.paginaPrincipal import MainPage
import HtmlTestRunner

class CompraTest(unittest.TestCase):
    ##el SetUpClass significa que estas acciones se ejecutaran una vez por clase y no una vez por metodo
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()

        cls.driver.implicitly_wait(10)

        cls.driver.maximize_window()

        cls.driver.get("https://www.amazon.com.mx")

    def test_busquedaProductoCaro(self):
        driver = self.driver
        mainpaige = MainPage(driver)
        mainpaige.buscarProducto('refrigerador')
        mainpaige.agregarProductoPorMarca('Mabe')
        self.assertTrue(mainpaige.obtenerSubtotal() > 10000, 'el subtotal es menor')

    def test_busquedaProductoBarato(self):
        driver = self.driver
        mainpaige = MainPage(driver)
        mainpaige.buscarProducto('refrigerador')
        mainpaige.agregarProductoPorMarca('SAMSUNG')
        self.assertTrue(mainpaige.obtenerSubtotal() < 10000, 'el subtotal es mayor')    
    
    ##el teardownclass significa que estas acciones se ejecutaran una vez por clase y no una vez por metodo
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

##esta linea de comandos sirve para cuando queramos ejecutar con normalidad desde linea de comando evitando el -m unittest
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/senju/Documents/PruebasDeTest/POMDemo/reports'))        




##El POM es un pantron de diseño que permite una mejor organizacion del codigo y permite la reutilizacion de metodos y evita la duplicacion
