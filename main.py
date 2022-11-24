import time
from asyncio import proactor_events
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link_twitter = "https://twitter.com/i/flow/login"

usuario_twitter = "@1mbpo"
senha_twitter = "codigoamigo123"
link_tweet = "https://twitter.com/compose/tweet"
usuario_mel = "@rxposy" 
dia = 0
texto_tweet = "MEL EU TE AMO MUITO " + usuario_mel 

dia = str(0)
while (dia < str(365)):
    print(dia)
    dia = dia + str(1)

options = webdriver.ChromeOptions() 
# options.add_argument("--headless")    
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\Webdriver\chromedriver.exe')
driver.get(link_twitter)

# acesso ao login
time.sleep(7)
campo_login = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
campo_login.send_keys(usuario_twitter)
print("                           ")
print("Usuário Adicionado")
print("Seguindo...")
print("                           ")

# acesso ao botão "avançar"

botao_avancar = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
driver.execute_script("arguments[0].click();", botao_avancar)

print("                  ")
print("Botão acionado!!!")
print("Seguindoo...")
print("                  ")

time.sleep(6)

# inserindo campo senha twitter

campo_senha = driver.find_element(by=By.NAME, value='password')
campo_senha.send_keys(senha_twitter)

print("                 ")
print("Senha adicionada")
print("Seguindo...")
print("                 ")

#localizando e acionado botao login do twitter

botao_login = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
driver.execute_script("arguments[0].click();", botao_login)

print("                 ")
print("Usuario logado!!!")
print("Seguindo...")
print("                 ")

time.sleep(6)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(link_tweet)

time.sleep(6)

inserir_texto = driver.find_element(by=By.CLASS_NAME, value='public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
inserir_texto.send_keys("Dias " + dia + texto_tweet)
inserir_texto.send_keys(Keys.ENTER)

botao_enviar = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div')
#driver.execute_script("arguments[0].click();", botao_enviar)









