# test_add_remove_product.py
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import logger, test_step_logger

def test_add_and_remove_product_from_cart(driver, config):
    test_step_logger.log_step("Starting test: Add and Remove Product")
    with open('data/test_data.json') as f:
        data = json.load(f)

    base_url = config['base_url']

    test_step_logger.log_step(f"Opening home page: {base_url}")
    home_page = HomePage(driver)
    home_page.open(base_url)

    test_step_logger.log_step(f"Searching for product: {data['product_name']}")
    home_page.search_product(data['product_name'])

    test_step_logger.log_step(f"Opening product at index: {data['product_index']}")
    search_results_page = SearchResultsPage(driver)
    search_results_page.open_nth_product(data['product_index'])

    driver.switch_to.window(driver.window_handles[1])

    test_step_logger.log_step("Selecting first available size and adding to cart")
    product_page = ProductPage(driver)
    product_page.select_first_available_size()
    product_page.add_to_cart()
    product_page.go_to_bag()

    test_step_logger.log_step("Waiting for cart page to load")
    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout/cart")
    )

    test_step_logger.log_step("Removing item from cart")
    cart_page = CartPage(driver)
    cart_page.remove_item()
    test_step_logger.log_step("Test completed: Add and Remove Product")

def test_search_no_results_for_invalid_product(driver, config):
    test_step_logger.log_step("Starting test: No Results Found")
    with open('data/test_data.json') as f:
        data = json.load(f)

    base_url = config['base_url']

    test_step_logger.log_step(f"Opening home page: {base_url}")
    home_page = HomePage(driver)
    home_page.open(base_url)

    test_step_logger.log_step("Searching for a non-existent product")
    home_page.search_product("nonexistentproduct12345")

    test_step_logger.log_step("Verifying 'No results found' message")
    assert home_page.verify_no_results_message(), "'No results found' message not displayed."
    test_step_logger.log_step("Test completed: No Results Found")


