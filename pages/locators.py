from selenium.webdriver.common.by import By

class HomePageLocators:
    SEARCH_BOX = (By.CLASS_NAME, 'desktop-searchBar')
    SEARCH_BUTTON = (By.XPATH, '//a[@class="desktop-submit"]')  # Button to initiate search
    CART_ICON = (By.XPATH, "//span[normalize-space()='Bag']")  # Cart icon in the header
    NO_RESULTS_MESSAGE = (By.XPATH, "//p[@class='index-infoBig']")  # Locator for 'No results found' message


class SearchResultsPageLocators:
    PRODUCT_LINKS = (By.CSS_SELECTOR, '.product-base a')
    FILTER_SECTION = (By.XPATH, '//div[@class="filter-container"]')  # Sidebar filter section
    SORT_DROPDOWN = (By.XPATH, '//div[@class="sort-sortBy"]')  # Sort by dropdown menu

class ProductPageLocators:
    #SIZES = (By.XPATH, '//p[@class="size-buttons-unified-size"]')
    #ADD_TO_BAG = (By.XPATH, '//div[@class="pdp-add-to-bag"]')
    #GO_TO_BAG = (By.CSS_SELECTOR, "a[class='desktop-cart'] span[class='desktop-userTitle']")  # Button to navigate to the cart

    SIZE_BUTTONS = (By.CLASS_NAME, 'size-buttons-size-button')
    ADD_TO_BAG = (By.CLASS_NAME, 'pdp-add-to-bag')
    #GO_TO_BAG = (By.CLASS_NAME, 'pdp-go-to-bag')
    GO_TO_BAG = (By.XPATH, "//span[normalize-space()='Bag']")


class CartPageLocators:
    REMOVE_ITEM = (By.XPATH, "//button[normalize-space()='REMOVE']")
    CONFIRM_REMOVE_ITEM = (By.CSS_SELECTOR, "button[class='inlinebuttonV2-base-actionButton ']")
    ITEM_QUANTITY = (By.XPATH, '//div[@class="itemContainer-base-quantitySelector"]')  # Dropdown to select item quantity
    EMPTY_CART_MESSAGE = (By.XPATH, '//div[@class="cart-base-emptyCart"]')  # Message displayed when the cart is empty
    CHECKOUT_BUTTON = (By.XPATH, '//div[@class="cart-base-checkout"]')  # Button to proceed to checkout
