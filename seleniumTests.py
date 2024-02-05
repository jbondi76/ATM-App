# Verify that Depositing 5 increases Account Balance by 5

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
 
try:
    driver.get('{{localhost}}/index.html')
    
    elm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "deposit-selection"))
    )
    print(elm)
    elm.click()
    numberInputElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "number-input"))
    )
    numberInputElm.clear();
    numberInputElm.send_keys("5");
    submitElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "submit-input"))
    )
    submitElm.click();
    statusElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "total"))
    )
    print(statusElm.text)
    assert("Account Balance $ 5" in statusElm.text)
 
finally:
    driver.close()

# Verify that Disabled on submit works correctly

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
 
try:
    driver.get('{{localhost}}/index.html')
    
    elm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "cashback-selection"))
    )
    print(elm)
    elm.click()
    numberInputElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "number-input"))
    )
    numberInputElm.clear();
    numberInputElm.send_keys("5");
    submitElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "submit-input"))
    )
    print(submitElm.is_enabled());
    assert(submitElm.is_enabled() is False)
 
finally:
    driver.close()

# Verify nothing other than Select shows if there is no selection

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
 
try:
    driver.get('{{localhost}}/index.html')
    elmFound = False
    print(driver.find_elements_by_xpath('//*[@id="number-input"]'))
    if len(driver.find_elements_by_xpath('//*[@id="number-input"]')) > 0: 
        elmFound = True
    print(elmFound)

    assert(elmFound is False)
 
finally:
    driver.close()

# Verify multiple transaction functionality

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
 
try:
    driver.get('{{localhost}}/index.html')
    
    elm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "deposit-selection"))
    )
    print(elm)
    elm.click()
    numberInputElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "number-input"))
    )
    numberInputElm.clear();
    numberInputElm.send_keys("100");
    submitElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "submit-input"))
    )
    submitElm.click();
    numberInputElm.clear();
    numberInputElm.send_keys("100");
    submitElm.click();

    cashBackElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "cashback-selection"))
    )
    print(cashBackElm)
    cashBackElm.click()

    numberInputElm.clear();
    numberInputElm.send_keys("50");

    submitElm.click();

    statusElm = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.ID, "total"))
    )
    print(statusElm.text)
    assert("Account Balance $ 150" in statusElm.text)
 
finally:
    driver.close()