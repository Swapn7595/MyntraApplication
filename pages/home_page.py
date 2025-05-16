from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import HomePageLocators
from .base_page import BasePage
from utils.config import logger

class HomePage(BasePage):
    def search_product(self, product_name):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'desktop-searchBar')))
        search_box = self.find_element(HomePageLocators.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)  # Replaced submit() with send_keys(Keys.ENTER)

    def verify_no_results_message(self):
        """Verify that the 'No results found' message is displayed."""
        # Avoid duplicate logging
        if not hasattr(self, '_no_results_logged'):
            logger.info("Verifying 'No results found' message")
            self._no_results_logged = True
        return self.wait.until(EC.presence_of_element_located(HomePageLocators.NO_RESULTS_MESSAGE))
