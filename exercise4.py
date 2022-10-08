from selenium.webdriver import *
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse



def find_by_text(navegador,tag, text):
    """
    Encontrar o elemento com o texto 'text'.

    Argumentos:
        - Browser = Instancia do browser [firefox, chrome, ...]
        - texto = conteúdo que deve estar na tag
        - tag = tag onde o texto sera procurado

    :param btext:
    :return:
    """
    #Pegar a tag que vai ser passada e gerar uma lista com varios elementos
    elementos = navegador.find_elements(By.TAG_NAME, tag)

    #Iterar sobre essa lista
    for elemento in elementos:
        if elemento.text == text:
            return elemento


url = 'http://selenium.dunossauro.live/aula_04_b.html'
navegador = Chrome()
navegador.get(url)


nome_das_caixas = ['um','dois','tres','quatro']


for texto in nome_das_caixas:
    sleep(0.3)
    find_by_text(navegador, "div", texto).click()


for texto in nome_das_caixas:
    sleep(0.3)
    navegador.back()


for texto in nome_das_caixas:
    sleep(0.3)
    navegador.forward()