import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re



import unittest
import time
base_dir = os.path.dirname(__file__) or '.'
sys.path.append("..")
from Locators.locators import Locators


class MainPage():

    def __init__(self,driver):
        self.driver = driver

    def buscarProducto(self, producto):
        self.driver.find_element('xpath',Locators.busquedalocator).send_keys(producto)
        self.driver.find_element('xpath',Locators.BusquedaButtonLocator).click()

    def agregarProductoPorMarca(self, marca):
        self.driver.find_element('xpath',"//li[@aria-label='"+ marca +"']/span").click()
        self.driver.find_element('xpath',Locators.primerResultadoLocator).click()
        self.driver.find_element('xpath',Locators.agregarAlCarritoButtonLocator).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(('xpath',Locators.noAgregarSeguroButton)))
        self.driver.find_element('xpath',Locators.noAgregarSeguroButton).click()
        wait.until(EC.url_contains('smart-wagon'))
        self.driver.find_element('xpath',Locators.amazonLogoLocator).click()

    def obtenerSubtotal(self):
        self.driver.find_element('xpath',Locators.carritoLogoLocator).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(('xpath',Locators.subtotalLocator)))
        elemento =  self.driver.find_element('xpath',Locators.subtotalLocator)
        subtotal = float(re.sub("[$,]",'',elemento.text))
        return subtotal



        