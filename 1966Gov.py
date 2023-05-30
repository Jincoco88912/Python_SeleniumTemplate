from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
# 關閉彈跳視窗
options.add_argument("--disable-notifications")
# 不打開圖形畫面
# options.add_argument("headless")

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get("https://1966.gov.tw/LTC/lp-6440-207.html")

wait = WebDriverWait(driver, 30)

# find_elements 預設為 List 型別
titleList = driver.find_elements(By.XPATH, '//*[@id="center"]/div/div[3]/div[2]/section/div[2]/ul/li')
print(titleList[3].text)

