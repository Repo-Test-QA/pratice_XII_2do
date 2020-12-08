from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class PageResult:
    def __init__(self, my_driver):
        self.no_results_banner = (By.XPATH, '//*[@id="center_column"]/p')
        self.title_banner = (By.XPATH, '//*[@id="center_column"]/h1/span[1]')
        self.orange_button = (By.ID, 'color_1')
        self.order = (By.ID, 'selectProductSort')
        self.checkbox = (By.CLASS_NAME, 'checkbox')
        self.color_check = (By.CLASS_NAME, 'color-option  ')
        self.driver = my_driver

    def return_no_element_text(self):
        return self.driver.find_element(*self.no_results_banner).text

    def return_section_title(self):
        return self.driver.find_element(*self.title_banner).text
    
    def click_orange_button(self):
        self.driver.find_element(*self.orange_button).click()

    # Seleccionamos una opción de la lista desplegable
    def select_by_text(self, text):
        select_option_text = Select(self.driver.find_element(*self.order))
        # Seleccionar por el texto visible, le pasamos como parámetro text
        select_option_text.select_by_visible_text(text)

    def select_by_value(self, value):
        select_option_value = Select(self.driver.find_element(*self.order))
        select_option_value.select_by_value(value)

    def select_by_index(self, number):
        select_option_index = Select(self.driver.find_element(*self.order))
        select_option_index.select_by_index(number)

    def click_checkbox(self, number_filtro):
        #Clase XII, estoy pasando como parámetro el índice, para seleccionar los filtros Summer y M
        self.driver.find_elements(*self.checkbox)[number_filtro].click()

    def click_color_check(self, number_color):
        #Clase XII, estoy pasando como parámetro el índice, para seleccionar el filtro de color Negro
        self.driver.find_elements(*self.color_check)[number_color].click()        

    



    


    

    
