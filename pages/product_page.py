from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    #SIZE_BUTTONS = (By.CLASS_NAME, 'size-buttons-size-button')
    #ADD_TO_BAG = (By.CLASS_NAME, 'pdp-add-to-bag')
    #GO_TO_BAG = (By.CLASS_NAME, 'pdp-go-to-bag')

    def select_first_available_size(self):
        """Wait for size options to appear and select the first available size."""
        try:
            sizes = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(ProductPageLocators.SIZE_BUTTONS)
            )
            if sizes:
                sizes[0].click()  # Select the first available size
            else:
                raise Exception("No sizes available")
        except TimeoutException:
            raise Exception("Timed out waiting for size options to appear")

    def add_to_cart(self):
        """Wait for the 'Add to Bag' button to become clickable and click it."""
        try:
            add_to_bag_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BAG)
            )
            add_to_bag_button.click()
        except TimeoutException:
            raise Exception("Timed out waiting for 'Add to Bag' button to become clickable")

    def go_to_bag(self):
        """Attempt to click the 'Go to Bag' button; if it fails, navigate directly to the cart page."""
        try:
            go_to_bag_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ProductPageLocators.GO_TO_BAG)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", go_to_bag_button)
            go_to_bag_button.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            print("Direct interaction with 'Go to Bag' button failed; navigating directly to the cart page.")
            self.driver.get('https://www.myntra.com/checkout/cart')
