from selenium.webdriver import *
from selenium.webdriver.common.by import By
from time import sleep


#url = input("Insira a URL")


url="https://selenium.dunossauro.live/aula_04_a.html"
navegador = Chrome()
navegador.get(url)

#pesquisa aninhada
lista_n_ordenada = navegador.find_element(By.TAG_NAME, "ul")
texto = lista_n_ordenada.find_elements(By.TAG_NAME, "li")
#Caso tenha mais items e apenas dar mais finds
texto[0].find_element(By.TAG_NAME,'a')
"""
1. buscamos `ul`
2. buscamos todos `li`
3. No primeiro `li`, buscamos `a` e pegamos o seu texto
ul
    li
        a
            texto
    li
        a
            texto
"""


print(texto[1].text)

