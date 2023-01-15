from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

site = 'https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/'
chrome_driver = "G:/My Drive/Programming/z - tools/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver))
driver.get(url=site)

fname = driver.find_element(By.NAME, 'fName')
fname.send_keys('Élder')
fname = driver.find_element(By.NAME, 'lName')
fname.send_keys('Barbosa')
fname = driver.find_element(By.NAME, 'email')
fname.send_keys('eldrelrk@gmail.com')
fname.send_keys(Keys.ENTER)

# btn = driver.find_element(By.XPATH, '/html/body/form/button')
# btn.click()



# service = Service("G:/My Drive/Programming/z - tools/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
#
# articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # print(articles.text)
#
# # all_portals = driver.find_element(By.LINK_TEXT, articles.text)
# # all_portals.click()
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Python')
#
#
# search.send_keys(Keys.ENTER)

