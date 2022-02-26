
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.python.org")
WebDriverWait(driver, 10).until(lambda d:  "Python" in d.title)

print(driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[3]').text)




