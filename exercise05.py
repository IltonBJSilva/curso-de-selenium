'''

1. Pegar todos os links de aulas
    {'nome da aula': 'Link da aula'}
2. Navegar até o exercicio 3
    achar a url do exercicio 3 e ir até la

'''
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from pprint import pprint
import os

url = 'http://selenium.dunossauro.live/aula_04.html'
navegador = Chrome()
navegador.get(url)


def get_links(navegador, elemento):  # dicionario
    """
    Pega todos os links dentro de um elemento

    - Navegador = a instância do navegador
    - element = webelement ['aside', main, body, ul, ol]

    Parte 1

    :param navegador:
    :param elemento:
    :return:
    """
    sleep(3)
    resultado = {}
    element = navegador.find_element(By.TAG_NAME, elemento)
    ancoras = element.find_elements(By.TAG_NAME, 'a')

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')
    return resultado


def save_file(navegador, tag):
    lista_links = get_links(navegador, tag)

    arc = '.\log.txt'

    if os.path.isfile(arc):
        print('O caminho {} existe'.format(arc))

    arquivo = open("log.txt", "w")
    arquivo.write(str(lista_links))
    arquivo.close()


save_file(navegador, 'main')

pprint(get_links(navegador, 'main'))

"""
Parte 2
"""
