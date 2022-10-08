from selenium.webdriver import *
from selenium.webdriver.common.by import By
from time import sleep



#Função para procurar o texto
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

#Como pega pelo href, não necessariamente precisa ter a tag, pois as vezes serve apenas como ancora
def find_by_href(navegador, link):
    """
        Encontrar o elemento 'a' com o link "link".

    Argumentos:
        - Browser = Instancia do browser [firefox, chrome, ...]
        - link = link que sera procurado em todas as tag 'a'
    :param navegador:
    :param link:
    :return:
    """

    elementos = navegador.find_elements(By.TAG_NAME, 'a')
    #Iterar sobre essa lista
    for elemento in elementos:
        #return URL
        if link in elemento.get_attribute('href'):
            return elemento







#elemento_ddg = find_by_text(navegador, "li", "DuckDuckGo")
#elemento_ddg = find_by_href(navegador, "ddg")


url = 'http://selenium.dunossauro.live/aula_04_a.html'
navegador = Chrome()
navegador.get(url)


