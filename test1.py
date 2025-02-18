from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--headless")
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--disable-infobars")
options.add_argument("--disable-logging")  # Disable logging
options.add_argument("--log-level=3")  # Set log level to SEVERE
options.add_argument("--silent")  # Disable info logs
options.add_argument("--disable-logging")  # Disable logging

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
print("Test Executed")
time.sleep(5)