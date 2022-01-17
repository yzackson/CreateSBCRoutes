
import time
import pandas
import sbcController
from selenium import webdriver

lojas = pandas.read_excel("./lojas.xlsx")

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("../Drivers/chromedriver97.exe", chrome_options=options)

login = ""
password = ""
ip = ""
url = "https://" + ip + "/?language=pt-br"

# Acessa o site
driver.get(url)
time.sleep(3)

# Fazer login
sbcController.doLogin(driver, login, password)
time.sleep(2)

i = 2

while i < 5:
    ########## NAPs ########## 
    # Acessar página de NAPs
    driver.get("https://" + ip + "/KWebConfig/index.php")
    time.sleep(2)
    # Criar NAPs
    sbcController.newNAP(driver, lojas, 1)
    time.sleep(3)

    ########## Rotas ########## 
    # Acessar a página de rotas
    driver.get("https://" + ip + "/KWebConfig/index.php")
    time.sleep(2)
    # Criar rotas
    sbcController.newRoute(driver, lojas, 1)
    time.sleep(10)

driver.close()