from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def should_be_add_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "Button is not presented"
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()
    def should_cost_equal(self):
        item_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        item_product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert item_basket_cost.text == item_product_cost.text, "Prices in basket and in product page isn't equal"

    def should_name_equal(self):
        items_strong = self.browser.find_elements(*ProductPageLocators.BASKET_STRONG_NAMES)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        names_equal = False
        for item_strong in items_strong:
            if item_strong.text == product_name:
                names_equal = True
        assert names_equal, "Names of product isn't equal"
