# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime
import logging

logging.basicConfig(filename="./seleniumlog630.log", format="%(asctime)s %(message)s",
                    filemode="w", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
# Start the browser and login with standard_user
def login(user, password):
    print('Starting the browser...')
    logging.info('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    print('Browser started successfully. Navigating to the demo page to login.')
    logging.info('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    # login
    print('Now logging in')
    logging.info('Now logging in ')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()

    # Check successful login
    product_listings = driver.find_element_by_class_name("product_label").text
    assert "Products" in product_listings
    print('Welcome ' + user + '! You are Logged In. Happy Shopping!')
    logging.info('Welcome ' + user + '! You are Logged In. Happy Shopping!')

    # Add items to cart
    print("Adding all products to cart")
    logging.info("Adding all products to cart")

    for item in range(6):
        name = "a[id='item_" + str(item) + "_title_link']"
        driver.find_element_by_css_selector(name).click()
        driver.find_element_by_css_selector("button[class='btn_primary btn_inventory']").click()
        product_name = driver.find_element_by_class_name("inventory_details_name").text
        print(" " + product_name + " added to cart!")
        logging.info(" " + product_name + " added to cart!")
        driver.find_element_by_css_selector("button[class='inventory_details_back_button']").click()
    else:
        print("Cart Adding Finished!")
        logging.info("Cart Adding Finished!")

    # Remove items from cart
    print("Removing all products from cart")
    logging.info("Removing all products from cart")

    for item in range(6):
        name = "a[id='item_" + str(item) + "_title_link']"
        driver.find_element_by_css_selector(name).click()
        driver.find_element_by_css_selector("button[class='btn_secondary btn_inventory']").click()
        product_name = driver.find_element_by_class_name("inventory_details_name").text
        print(" " + product_name + " removed from cart!")
        logging.info(" " + product_name + " removed from cart!")
        driver.find_element_by_css_selector("button[class='inventory_details_back_button']").click()
    else:
        print('Cart Removing Finished!')
        logging.info('Cart Removing Finished!')
        print('Test Completed')
        logging.info('Test Completed')

login('standard_user', 'secret_sauce')
