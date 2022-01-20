
from operator import concat
import time
import pandas
import sbcController
import logging
from selenium import webdriver

# Logging config
logging.basicConfig(filename="logging.log", level=logging.INFO, format="%(asctime)s | %(levelno)s | %(levelname)s | %(message)s")

login = input("Login: ")
password = input("Password: ")
ip = input("SBC IP adrress (xxx.xxx.xxx.xxx): ")
path = input("File name of branchs list (.xlsx file): ")

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("./chromedriver97.exe", chrome_options=options)

url = "https://" + ip + "/?language=pt-br"

# Access website
driver.get(url)
time.sleep(3)

# Do login
sbcController.doLogin(driver, login, password)
time.sleep(2)

i = 0 # row count

while i < (lojas["Nome"].length - 1):
    logging.info("#################################################################")
    logging.info("Adicionando loja - Nome: " + str(i) + "." + lojas["Nome"][i])

    # Access NAPs/Routes page
    driver.get("https://" + ip + "/KWebConfig/index.php")
    time.sleep(1)
    
    ########## Create NAP ##########
    logging.info("Creating NAP...")
    sbcController.newNAP(driver, lojas, i)
    time.sleep(1)

    ########## Create Route ##########
    logging.info("Creating Rota")
    sbcController.newRoute(driver, lojas, i)
    time.sleep(1)
    
    # logging the branch created
    logging.info(" Loja adicionada")
    logging.info("Name: " + lojas["Nome"][i])
    logging.info("Domain: " + lojas["Dominio"][i])
    logging.info("Sets range: " + lojas["Ramais"][i])
    i += 1

driver.close()
