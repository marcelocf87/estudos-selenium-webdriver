"""
@author Marcelo Custódio Freitas
@version 1.0
@since 20/03/2023
"""

import time
from selenium import webdriver

# Abre o navegador
browser = webdriver.Chrome()

#Informa qual site irá acessar
browser.get("https://google.com")
time.sleep(5)
