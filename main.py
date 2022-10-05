from selenium.webdriver import *
from selenium.webdriver.common.by import By
from time import sleep


url="https://curso-python-selenium.netlify.app/exercicio_02.html"
navegador = Chrome()
navegador.get(url)

sleep(1)
a = navegador.find_element(By.TAG_NAME, "a")


for click in range(10):
    ps = navegador.find_elements(By.TAG_NAME,"p")
    a.click()
    print(f'Valor do ultimo p:{ps[-1].text} | valor do click: {click}')
