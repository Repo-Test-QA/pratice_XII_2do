from selenium import webdriver
import unittest
from pageIndex import PageIndex
from pageResult import PageResult
from pageItem import PageItem
import time
#Clase XI, importamos chrome options para poder pasarle opciones al explorador Chrome
from selenium.webdriver.chrome.options import Options

class TestCase(unittest.TestCase):
    #Precondiciones
    def setUp(self):

        #Clase XI, instanciamos la clase Options
        option = Options()
        #Podemos ahora pasarle argumentos, en este caso el navegador, se va a mostrar maximizado
        option.add_argument('start-maximized')
        #Podemos testear en modo incognito
        option.add_argument('incognito')
        #Considerar, levantar un browser en modo gráfico (en el explorador), es muy pesado y usa tiempo.
        #Por eso existe algo llamado Modo Headless, no se va a ver, pero si se va a ejecutar de manera
        #rápida (background).
        #Cuando estemos programando el caso de prueba, no debemos trabajar en modo headless, cuando
        #este listo el testcase, activamos tal modo.
        option.add_argument('--headless')
        #Por tanto, tenemos dos formas o maneras de controlar ciertas cosas del browser.
        #1. A partir de Selenium
        #2. A partir de las opciones de Chrome (Recomendable)

        # Ahora voy a pasar al webdriver.Chrome un segundo argumento, el objeto option de la clase Options.
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)

        #self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)

        #Creamos un objeto de tipo PageIndex(clase)
        self.indexPage = PageIndex(self.driver)
        #Creamos un objeto de tipo PageResult(clase)
        self.resultPage = PageResult(self.driver)
        #Creamos un objeto de tipo PageItem(clase)
        self.itemPage = PageItem(self.driver)


    #@unittest.skip('Not need now')
    def test_search_no_element(self):
        self.indexPage.search('Hola')
        self.assertEqual(self.resultPage.return_no_element_text(), 'No results were found for your search "Hola"')

        # Clase XI, para capturar la pantalla de evidencia, hacemos lo siguiente, agregamos el nombre del archivo
        # con su extensión. Considerar, no se debe utilizar try para los Assert.
        self.driver.save_screenshot('no_elements.jpg')

    #@unittest.skip('Not need now')
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.resultPage.return_section_title())

    #@unittest.skip('Not need now')
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirts')
        self.assertTrue('T-SHIRTS' in self.resultPage.return_section_title(), self.resultPage.return_section_title())

    #@unittest.skip('Not need now')
    def test_tarea(self):
        self.indexPage.search('t-shirts')
        self.resultPage.click_orange_button()
        self.itemPage.enter_quantity('25')
        self.itemPage.add_elements(3)
        # Asigno a una variable lo que devuelve el método (28), en este caso el valor del elemento
        number = self.itemPage.get_number_of_elements()
        # Verificamos mediante el assert si el valor es igual a 28 (lo que nosotros sabemos)
        self.assertTrue(number == '28')
        # Vamos a agregar unos segundos solo para verificar que se muestre la cantidad ingresada, luego comentamos
        time.sleep(3)

    #@unittest.skip('Not need now')
    def test_selection(self):
        self.indexPage.search('t-shirts')
        # Seleccionamos el elemento por el texto, es decir el parámetro text
        self.resultPage.select_by_text('Product Name: A to Z')
        # Vamos a agregar unos segundos solo para verificar que se muestre la cantidad ingresada, luego comentamos
        time.sleep(3)

        # Seleccionamos el elemento por el valor, es decir el parámetro value
        self.resultPage.select_by_value('reference:asc')
        # Vamos a agregar unos segundos solo para verificar que se muestre la cantidad ingresada, luego comentamos
        time.sleep(3)

        # Seleccionamos el elemento por el indice (4 => Product Name: Z to A), es decir el parámetro number
        self.resultPage.select_by_index(4)
        # Vamos a agregar unos segundos solo para verificar que se muestre la cantidad ingresada, luego comentamos
        time.sleep(3)

    #@unittest.skip('Not need now')
    def test_dresses_options(self):
        #Clase XII.-
        # Elegir la opción Dresses
        self.indexPage.click_dresses()
        # Agregamos un tiempo para verificar que llegamos a la página Dresses
        time.sleep(3)

        #Seleccionar el filtro Summer índice 2 de la clase => checkbox
        self.resultPage.click_checkbox(2)
        # Agregamos un tiempo para verificar 
        time.sleep(3)

        #Seleccionar el filtro M índice 4 de la clase => checkbox
        self.resultPage.click_checkbox(4)
        # Agregamos un tiempo para verificar 
        time.sleep(3)

        #Seleccionar el filtro color Negro índice 2 de la clase tiene dos espacios al final => color-option  
        self.resultPage.click_color_check(2)
        # Agregamos un tiempo para verificar 
        time.sleep(3)


    #Postcondiciones, que quiero que pase, cuando termine una prueba
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()








