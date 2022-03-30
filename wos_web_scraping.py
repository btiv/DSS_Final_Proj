import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 

chrome_options = webdriver.ChromeOptions()
#prefs = {'download.default_directory' : './biodiversity_data/'}
#chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www-webofscience-com.ezproxy.library.tufts.edu/wos/woscc/summary/8ee3f42c-f409-4e90-b1e6-7f748e74d9c8-29680c68/relevance/1')
driver.manage().window().maximize()

driver.refresh()
for low in range(20001, 110000, 1000): 
    high = low + 999
    #time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="snRecListTop"]/app-export-menu/div/button/span[1]')))
    driver.find_element(By.XPATH, '//*[@id="snRecListTop"]/app-export-menu/div/button/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="exportToExcelButton"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'radio3')))
    driver.find_element(By.XPATH, '//*[@id="radio3"]/label/span[1]').click()

    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').click()
    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').clear()
    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(low)

    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').click()
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').clear()
    driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(high)

    driver.find_element(By.XPATH, '/html/body/app-wos/div/div/main/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/div/div[1]/wos-select/button/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="global-select"]/div/div[2]/div[3]').click()
    driver.find_element(By.XPATH, '/html/body/app-wos/div/div/main/div/div[2]/app-input-route[1]/app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/div/div[2]/button[1]/span[1]/span').click()
    
    time.sleep(10)
    driver.refresh()
