import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# options = webdriver.ChromeOptions()
# options.add_argument('ignore-certificate-errors')
# driver = webdriver.Chrome("../Drivers/chromedriver97.exe", chrome_options=options)

def doLogin(driver, login, password):
    # Fazer login
    driver.find_element_by_id("login").send_keys(login)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//*[@id=\"tableLogin\"]/tbody/tr[6]/td/input").send_keys(Keys.ENTER)



def newNAP(driver, lojas, countLoja):
    #Clicar em "Nova NAP"
    driver.find_element_by_xpath("//*[@id=\"menu-naps-gw\"]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"NAPsDivForm\"]/input").click()
    time.sleep(1)

    #Nome
    driver.find_element_by_id("gateway-nap-name").send_keys(lojas["Nome"][countLoja])
    
    #Tipo = Sip
    obj = driver.find_element_by_id("gateway-nap-type")
    selectObj = Select(obj)
    selectObj.select_by_value("SIP")
    time.sleep(1)
    
    #Dominio
    driver.find_element_by_id("gateway-nap-sip-domain").send_keys(lojas["Dominio"][countLoja])
    
    #Limite de canais = 10
    driver.find_element_by_id("gateway-nap-sip-channel-no-limit").send_keys(Keys.SPACE)
    time.sleep(1)
    driver.find_element_by_id("gateway-nap-sip-channel-limit").send_keys("10")
    
    #Selecionar interface de rede para o SIP e RTP
    obj = driver.find_element_by_id("gateway-nap-sip-force-sip-interface")
    selectObj = Select(obj)
    selectObj.select_by_value("ens192.ipv4")
    obj = driver.find_element_by_id("gateway-nap-sip-force-rtp-interface")
    selectObj = Select(obj)
    selectObj.select_by_value("ens192.ipv4")
    
    #salvar
    driver.find_element_by_xpath("//*[@id=\"NAPsDivForm\"]/div[2]/input[2]").send_keys(Keys.ENTER)