from .base_page import BasePage
from .locators import SearchResultsPageLocators

class SearchResultsPage(BasePage):
    def open_nth_product(self, n):
        products = self.driver.find_elements(*SearchResultsPageLocators.PRODUCT_LINKS)
        if n < len(products):
            products[n].click()
