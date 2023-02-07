import pyautogui as gui
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'tina' in comando:
                comando = comando.replace('tina', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Erro localizado !!')
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        pywhatkit.playonyt(musica)
        maquina.say('Rodando vídeo')
        maquina.runAndWait()
    elif 'se apresente' in comando:
        maquina.say('Prazer, sou a tina, inteligência artificial mais legal do mundo, criada para a feira técnica de 2 mil e 20 e 2 do COLÉGIOS UNIVAP')
        maquina.runAndWait()
    elif 'nome do criador' in comando:
        maquina.say('O meu criador é: Gustavo Pacheco')
        maquina.runAndWait()
    elif 'horários da feira' in comando:
        maquina.say('A feira ocorrerá de manhã das 8 às 12 e 30, e a noite das 19 às 20 e 2 horas')
        maquina.runAndWait()
    elif 'suas funções' in comando:
        maquina.say('Minhas funções são: Pesquisar algo no google, buscar por vídeos no YouTube, apresentar meus criadores, indicar o horário de funcionamento da Feira, dizer que horas são e me apresentar ')
        maquina.runAndWait()
    elif 'abrir whatsapp' in comando:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://web.whatsapp.com')
        time.sleep(20)
        # Definir contatos e mensagens para enviar
        contatos = []
        mensagem = ''
        # Buscar contatos
        def buscar_contato(contato):
            campo_pesquisa = driver.find_element("xpath", '//div[contains(@class,"copyable-text selectable-text")]')
            time.sleep(3)
            campo_pesquisa.click()
            campo_pesquisa.send_keys(contato)
            campo_pesquisa.send_keys(Keys.ENTER)

        def enviar_mensagem(mensagem):
            campo_mensagem = driver.find_elements("xpath", '//div[contains(@class,"selectable-text copyable-text")]')
            time.sleep(3)
            gui.write(mensagem)
            time.sleep(2)
            gui.press('enter')
            time.sleep(5)

        for contato in contatos:
            buscar_contato(contato)
            enviar_mensagem(mensagem)


print('SEMPRE DIGA O NOME "TINA" ANTES DE QUALQUER COMANDO ABAIXO')
print('='*40)
print('COMANDOS = HORAS: SABER AS HORAS | PROCURE POR: ACHAR ALGO NO GOOGLE | TOQUE: TOCAR MUSICA DO YOUTUBE | SE APRESENTE: BREVE APRESENTAÇÃO DA MESMA |')
print('NOME DOS CRIADORES: APRESENTA OS CRIADORES | HORARIO DA FEIRA: FUNCIONAMENTO DA FEIRA | SUAS FUNÇÕES: APRESENTA SUAS FUNÇÕES')
while True:
    comando_voz_usuario()
    break
