from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def remove_item(self):
        """Remove an item from the cart by handling the confirmation modal."""
        try:
            # Wait for the initial 'Remove' button to be clickable
            remove_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CartPageLocators.REMOVE_ITEM)
            )
            # Scroll the 'Remove' button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", remove_button)
            # Click the 'Remove' button
            remove_button.click()

            # Wait for the confirmation modal's 'Remove' button to be clickable
            confirm_remove_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(CartPageLocators.CONFIRM_REMOVE_ITEM)
            )
            # Scroll the confirmation 'Remove' button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", confirm_remove_button)
            # Click the confirmation 'Remove' button
            confirm_remove_button.click()

            # Optionally, wait until the item is removed from the cart
            WebDriverWait(self.driver, 10).until(
                EC.staleness_of(remove_button)
            )
        except TimeoutException:
            print("Timeout: Element not found or not clickable.")
            self.driver.save_screenshot('timeout_exception.png')
            raise
        except NoSuchElementException:
            print("Element not found in the DOM.")
            self.driver.save_screenshot('nosuch_element_exception.png')
            raise
        except ElementClickInterceptedException:
            print("Click intercepted by another element.")
            self.driver.save_screenshot('click_intercepted_exception.png')
            raise

