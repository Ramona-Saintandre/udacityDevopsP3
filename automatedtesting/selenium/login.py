from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime
import logging

logging.basicConfig(filename="./seleniumlog.txt", format="%(asctime)s %(message)s",
                    filemode="w", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
# Start the browser and login with standard_user
def login (user, password):
    print('Starting the browser...')
    logging.info('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    print('Browser started successfully. Navigating to the demo page to login.')
    logging.info('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

