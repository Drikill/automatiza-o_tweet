from ast import keyword
from time import sleep
from xml.dom.xmlbuilder import DOMEntityResolver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


options = webdriver.ChromeOptions() 
options.add_argument("--headless")


options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDriver\chromedriver.exe')
driver.get('https://twitter.com/i/flow/login')
time.sleep(6)
login = driver.find_element(by=By.NAME, value= "text")
login.send_keys("1mbpo")
botao = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
driver.execute_script("arguments[0].click(); ", botao)
time.sleep(6)
senha = driver.find_element(by=By.NAME, value= "password")
senha.send_keys("codigoamigo123")
time.sleep(6)
botoa_log = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
driver.execute_script("arguments[0].click(); ", botoa_log)
time.sleep(6)
tweet = tweet = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
driver.execute_script("arguments[0].click(); ", tweet)
time.sleep(6)
camp_text = tweet = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
camp_text.send_keys(" MEL EU TE AMO MT @rxposy")
camp_text.send_keys(Keys.ENTER)

botao_pub =  driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
driver.execute_script("arguments[0].click(); ", botao_pub)






