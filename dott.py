
from operator import concat
import time
import pandas
import sbcController
import logging
from selenium import webdriver

logging.basicConfig(filename="logging.log", level=logging.INFO, format="%(asctime)s | %(levelno)s | %(levelname)s | %(message)s")
lojas = pandas.read_excel("./lojas.xlsx")

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("../Drivers/chromedriver97.exe", chrome_options=options)

login = "admin"
password = "Gene7790"
ip = "10.7.4.11"
url = "https://" + ip + "/?language=pt-br"

# Acessa o site
driver.get(url)
time.sleep(3)

# Fazer login
sbcController.doLogin(driver, login, password)
time.sleep(2)

i = 37
j = 37

while i < 48:
    logging.info("#################################################################")
    logging.info("Adicionando loja - Nome: " + str(i) + "." + lojas["Nome"][i])
    ########## NAPs ##########
    logging.info("Criando NAP...")
    # Acessar página de NAPs
    driver.get("https://" + ip + "/KWebConfig/index.php")
    time.sleep(1)
    # Criar NAPs
    sbcController.newNAP(driver, lojas, i)
    time.sleep(1)
    #logging.info("NAP criada")

    ########## Rotas ########## 
    # Acessar a página de rotas
    #driver.get("https://" + ip + "/KWebConfig/index.php")
    #time.sleep(1)
    # Criar rotas
    logging.info("Criando Rota")
    sbcController.newRoute(driver, lojas, i)
    time.sleep(1)
    #logging.info("Rota Criada")
    
    # Loja criada
    logging.info(" Loja adicionada")
    logging.info("Nome: " + lojas["Nome"][i])
    logging.info("Dominio: " + lojas["Dominio"][i])
    logging.info("Ramais: " + lojas["Ramais"][i])
    i += 1

driver.close()