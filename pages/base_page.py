import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger('MyntraApplication')

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)  # Increased timeout to 10 seconds

    def open(self, url):
        if self.driver.current_url != url:  # Check if the URL is already open
            logger.info(f"Opening URL: {url}")
            self.driver.get(url)
        else:
            logger.info(f"URL already open: {url}")

    def find_element(self, locator):
        try:
            # logger.info(f"Finding element with locator: {locator}")
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Timeout while waiting for element with locator: {locator}")
            logger.error(f"Current URL: {self.driver.current_url}")
            logger.error(f"Page Source: {self.driver.page_source[:500]}...")  # Log first 500 characters of page source
            raise

    def click(self, locator):
        logger.info(f"Clicking on element with locator: {locator}")
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        logger.info(f"Entering text into element with locator: {locator}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
