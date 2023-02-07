#Bibliotecas
import pyautogui as gui
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#Navegar ate o wpp web
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://web.whatsapp.com')
    time.sleep(15)
    #Definir contatos e mensagens para enviar
    contatos = ['']
    mensagem = 'Mensagem de teste robo python'
    #Buscar contatos
    def buscar_contato(contato):
        campo_pesquisa = driver.find_element("xpath", '//div[contains(@class,"copyable-text selectable-text")]')
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)

    def enviar_mensagem(mensagem):
        campo_mensagem = driver.find_elements("xpath", '//div[contains(@class,"selectable-text copyable-text")]')
        gui.write(mensagem)
        gui.press('enter')
        time.sleep(4)

    for contato in contatos:
        buscar_contato(contato)
        enviar_mensagem(mensagem)
except:
    print('Ocorreu um erro !!')


