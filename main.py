from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

#assert driver.title == "WUSTL" # => "Google"

driver.implicitly_wait(10)

driver.get("https://screening.wustl.edu")

driver.maximize_window()

i = driver.find_element_by_name("ucWUSTLKeyLogin$txtUsername")
i.send_keys("USERNAME")

i = driver.find_element_by_name("ucWUSTLKeyLogin$txtPassword")
i.send_keys("PASSWORD")
i.send_keys(Keys.RETURN)

driver.find_element_by_xpath("//mat-radio-button [@class='sub-text mat-radio-button mat-accent ng-star-inserted']").click()

driver.find_element_by_xpath("//mat-checkbox [@id='mat-checkbox-9']").click()

driver.find_element_by_xpath("//mat-radio-button [@id='mat-radio-8']").click()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(0.5)

driver.find_element_by_xpath("//mat-radio-button [@id='mat-radio-10']").click()

time.sleep(0.5)

driver.find_element_by_xpath("//mat-radio-button [@id='mat-radio-11']").click()

#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Danforth Campus']"))).click()

#WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Danforth Campus']"))).click()

time.sleep(20)


#danforth = driver.find_elements_by_class_name('mat-radio-label-content')
#print(danforth)

driver.quit()
