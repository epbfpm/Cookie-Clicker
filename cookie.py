from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from time import time
from selenium.webdriver.chrome.options import Options

site = 'https://orteil.dashnet.org/experiments/cookie/'
chrome_driver = "G:/My Drive/Programming/z - tools/chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver))
# keep window open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver))
driver.get(url=site)

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

var = 10
timeout = time() + var
five_min = time() + 60*5

items = driver.find_elements(By.CSS_SELECTOR, '#store div')
ids = [item.get_attribute('ID') for item in items][:7]
correct = 0
while True:
    cookie.click()
    if time() > timeout:
        moni = int(driver.find_element(By.ID, 'money').text.replace(',', ''))
        item_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        price_list = [int(price.text.split(' - ')[1].replace(',', '')) for price in item_prices[:7]]
        # for n in ids[::-1]:
        #     price = price_list[ids.index(n) + correct]
        #     if moni >= price:
                # if price >= price_list[ids.index(n) + correct + 1]:
                #     ids.remove(ids[0])
                #     correct += 1
                #     print(ids)
                #     break
                # else:
                #     higher_id = n
                #     print(n)
                #     driver.find_element(By.ID,higher_id).click()
                #     break
        for n in ids[::-1]:
            price = price_list[ids.index(n) + correct]
            if moni >= price:
                    higher_id = n
                    if ids.index(n) > 0:
                        ids.remove(ids[0])
                        correct += 1
                    driver.find_element(By.ID, higher_id).click()
                    break
        timeout += 10
        if time() >= five_min:
            cps = driver.find_element(By.ID, 'cps').text
            print(f'Your cps after 5 min is{cps}')
            break


        # price_list = [price.text.split("- ")[1] for price in item_prices]


