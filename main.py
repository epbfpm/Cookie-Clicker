from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

site = 'https://www.python.org/'

service = Service("C:/ChromeWebDriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url=site)


# events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text.splitlines()
#
# dict = {i: {"time": events[i], 'name': events[1+1]} for i in range(0, len(events), 2)}
#
# print(dict)

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

dictionary = {i: {'time': event_times[i].text, 'name': event_names[i].text} for i in range(0, len(event_times))}

print(dictionary)
# event = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# print(event.text)


# site = 'https://www.amazon.com/dp/B09F6XHB4C/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0'
# service = Service("C:/ChromeWebDriver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get(url=site)

# price = driver.find_element(by=By.CLASS_NAME, value='a-price-whole')
# print(price.text)
#
# price = driver.find_element(by=By.CLASS_NAME, value='a-offscreen').get_attribute('textContent')
# print(price)

# search_bar = driver.find_element(By.ID, 'twotabsearchtextbox').get_attribute('class')
# print(search_bar)

# link = driver.find_element(By.CSS_SELECTOR, '.nav-logo-link').get_attribute('href')
# print(link)
#
# price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')
# print(price.text)

driver.quit()

