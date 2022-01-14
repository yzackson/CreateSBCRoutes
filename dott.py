
import time
import pandas
import sbcController
from selenium import webdriver

lojas = pandas.read_excel("./lojas.xlsx")

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("../Drivers/chromedriver97.exe", chrome_options=options)

login = "admin"
password = "Gene7790"
url = "https://10.7.4.11/?language=pt-br"

# Acessa o site
driver.get(url)
time.sleep(3)

# Fazer login
sbcController.doLogin(driver, login, password)
time.sleep(2)

#Acessar página de NAPs
driver.get("https://10.7.4.11/KWebConfig/index.php")
time.sleep(2)

## Criar NAPs
sbcController.newNAP(driver, lojas, 1)
time.sleep(30)

driver.close()


## Criar rotas
#Acessar a parte de rotas
#clicar em "Nova Rota"
#preencher os campos
    #Nome = In_ + nome
    #NAP origem = Qualquer
    #Número de B = Número dos ramais das lojas no formaro correto
    #NAP Destino = mesma que do nome
#salvar
