
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import time


class loggin(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\yoezi\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9\chromedriver.exe")
        
        
        
    def test_HappyPath(self):
        
        #Ingresa a la pagina
        driver = self.driver
        driver.get("https://www.gamesfull.org/")
        
        #Busca el icono para iniciar sesion y hace click
        iniciarSesion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/header/div[2]/button[2]/img")))
        if iniciarSesion is not None:
            iniciarSesion.click()
            
        #Busca campo email y lo completa
        ingresarEmail = driver.find_element_by_class_name("form__input")
        if ingresarEmail is not None:
            ingresarEmail.send_keys("ingresar email")
            
        #Busca campo contrasena y lo completa
        ingresarContra = driver.find_element_by_id("password1")
        if ingresarContra is not None:
            ingresarContra.send_keys("ingresar password")
            
        #Busca el botton submit y hace click
        iniciar = driver.find_element_by_class_name("form__submit")
        if iniciar is not None:
            iniciar.click()
            
        #Compruebo el inicio de sesion buscando nombre de usuario y envio notificacion de registro exitoso
        comprobarIngreso = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Yoe91")))
        if comprobarIngreso is not None:
            time.sleep(2)
            print("Registro con exito")
            
    def test_CamposVacios(self):
        #Ingresa a la pagina
        driver = self.driver
        driver.get("https://www.gamesfull.org/")
        
        #Busca el icono para iniciar sesion y hace click
        iniciarSesion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/header/div[2]/button[2]/img")))
        if iniciarSesion is not None:
            iniciarSesion.click()
            
        #Click en iniciar sesion sin completar los campos
        iniciar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "form__submit")))
        #iniciar = driver.find_element_by_class_name("form__submit")
        if iniciar is not None:
            iniciar.click()
            
        #buscar el mensaje de error
        mensajeError = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.LINK_TEXT, "Completa este campo")))
        if mensajeError is not None:
            time.sleep(2)
            print('NO se puede ingresar, mensaje "Completa todos los campos"')
            
    def test_contraIncorrecta(self):
        #Ingresa a la pagina
        driver = self.driver
        driver.get("https://www.gamesfull.org/")
        
        #Busca el icono para iniciar sesion y hace click
        iniciarSesion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/header/div[2]/button[2]/img")))
        if iniciarSesion is not None:
            iniciarSesion.click()
            
        #Busca campo email y lo completa
        ingresarEmail = driver.find_element_by_class_name("form__input")
        if ingresarEmail is not None:
            ingresarEmail.send_keys("ingresar email")
            
        #Busca campo contrasena y lo completa
        ingresarContra = driver.find_element_by_id("password1")
        if ingresarContra is not None:
            ingresarContra.send_keys("ingresar password")
            
        #Busca el botton submit y hace click
        iniciar = driver.find_element_by_class_name("form__submit")
        if iniciar is not None:
            iniciar.click()
        
        #Cartel de contrasena incorrecta
        incorrecta = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.LINK_TEXT, "ERROR")))
        if incorrecta is not None:
            time.sleep(2)
            print("NO se puede ingresar, Contrasena incorrecta")
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="resultados de mi test"))