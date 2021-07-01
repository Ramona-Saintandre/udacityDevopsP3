from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
import logging
logging.basicConfig(filename="./seleniumlog.txt", format="%(asctime)s %(message)s",
                    filemode="w", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
# Open browser and login
def login(user, password):
    print('Starting the browser...')
    logging.info('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    print('Browser started successfully. Navigating to the demo page to login.')
    logging.info(
        'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    # login
    print('Logging in...')
    logging.info('Logging in...')
    login_user = driver.find_element_by_id("user-name")
    login_password = driver.find_element_by_id("password")
    login_user.send_keys(user)
    login_password.send_keys(password)
    driver.find_element_by_id("login-button").click()
    if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "inventory_container"))):
        print('The Login was successful by the user name: ' + user)
        logging.info('The Login was successful by the user name: ' + user)
    else:
        print('The login was unsuccessful')
        logging.info('The login was unsuccessful')
        driver.close()
    # List of inventory
    productList = driver.find_elements_by_class_name("inventory_list")
    items = driver.find_elements_by_class_name("inventory_item_name")
    addList = driver.find_elements_by_css_selector(
        "button[class='btn_primary btn_inventory']")
    removeList = driver.find_elements_by_css_selector(
        "button[class='btn_secondary btn_inventory']")
    # Add items to cart
    print("Adding all products to cart")
    logging.info("Adding all products to cart")
    for item in items:
        print("Adding " + item.text + " to cart")
        logging.info("Adding " + item.text + " to cart")
    for btn in addList:
        btn.click()
    print("All the products are added to cart")
    logging.info("All the products are added to cart")
    # removing the products
    for item in items:
        print("Removing " + item.text + " from cart")
        logging.info("Removing " + item.text + " from cart")
    for btn in removeList:
        btn.click()
    print("All products are removed from cart")
    logging.info("All products are removed from cart")
    driver.close()
login('standard_user', 'secret_sauce')