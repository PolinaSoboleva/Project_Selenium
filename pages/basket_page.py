from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
           "Success message is presented, but should not be"
    def should_be_text_about_empty_basket(self):
        text_basket = self.browser.find_element(*BasketPageLocators.CONTENT)
        assert "basket is empty" in text_basket.text, "Expected phrase that the cart is empty"
