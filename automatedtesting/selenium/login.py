#For Selenium: Udacity project requirements
#For Selenium:
#Create a UI Test Suite that adds all products to a cart, and then removes them.
#Include print() commands throughout the tests so the actions of the tests can easily be determined.
# E.g. A login function might return which user is attempting to log in and whether or not the outcome was successful.
#Deploy the UI Test Suite to the linux VM and execute the Test Suite via the CI/CD pipeline.

#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime
import logging
#Logging Tutorial in Python https://www.youtube.com/watch?v=gsa1oFn9n0M
#logging.basicConfig(filename='/home/<unixuser>/logs/selenium.log', filemode='a', level=logging.INFO)
logging.basicConfig(filename='E:/udacityDevopsP3/automatedtesting/selenium/logs/selenium.log', filemode='a', level=logging.INFO)
logger = logging.getLogger(__name__)

URL_LOGIN = 'https://www.saucedemo.com/'
URL_INVENTORY = 'https://www.saucedemo.com/inventory.html'
URL_CART = 'https://www.saucedemo.com/cart.html'


def log_status(text):
    """log_status log status including timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(timestamp + " " + text)
    print(f"{timestamp} - {text}")

def login(driver, user, password):
    """Login to the website"""
    log_status('Navigating to the demo page to login.')
    driver.get(URL_LOGIN)
    driver.maximize_window()
    driver.find_element_by_id("user-name").send_keys(user)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login-button").click()
    assert URL_INVENTORY in driver.current_url
    log_status(f"Login with username {user} and password {password} successful")


def add_items(driver):
    """Add items to the cart"""
    cart = []
    log_status('Add all items to the cart')
    items = driver.find_elements_by_class_name('inventory_item')
    for item in items:
        item_name = item.find_element_by_class_name('inventory_item_name').text
        cart.append(item_name)
        item.find_element_by_class_name('btn_inventory').click()
        log_status(f'Added {item_name}')
    cart_item = driver.find_element_by_class_name('shopping_cart_badge')
    assert int(cart_item.text) == len(items)

    driver.find_element_by_class_name('shopping_cart_link').click()
    assert URL_CART in driver.current_url

    for item in driver.find_elements_by_class_name('inventory_item_name'):
        assert item.text in cart
    log_status('test is done,  adding items to the cart')


def remove_items(driver):
    """Remove items from the cart"""
    driver.find_element_by_class_name('shopping_cart_link').click()
    assert URL_CART in driver.current_url

    cart_items = len(driver.find_elements_by_class_name('cart_item'))

    log_status(f"Number of items in the cart = {cart_items}")
    for item in driver.find_elements_by_class_name('cart_item'):
        item_name = item.find_element_by_class_name('inventory_item_name').text
        item.find_element_by_class_name('cart_button').click()
        log_status(f'Removed {item_name}')

    cart_items = len(driver.find_elements_by_class_name('cart_item'))
    assert cart_items == 2
    log_status(' test is done, remove items from the cart')


def run_tests():
    """Run the test"""
    log_status("Starting the browser...")
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    log_status('Browser started successfully.')
    log_status('Login')
    login(driver, "standard_user", "secret_sauce")
    log_status('Add items')
    add_items(driver)
    log_status('Remove items')
    remove_items(driver)
    log_status("Tests Completed")


if __name__ == "__main__":
    run_tests()
