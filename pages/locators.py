from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")
    REG_USERNAME=(By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD=(By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2=(By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON=(By.CSS_SELECTOR, "[name='registration_submit']")
    
class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME=(By.CSS_SELECTOR, "div.product_main h1")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
    BASKET_ITEMS=(By.CSS_SELECTOR, ".basket-items")
    CONTENT=(By.CSS_SELECTOR,".content #content_inner")