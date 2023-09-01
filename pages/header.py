from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):

    SEARCH_FIELD = (By.ID,'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    PARTICULAR_PRODUCT = (By.CSS_SELECTOR, ".a-section.aok-relative.s-image-fixed-height")
    RETURN_ORDERS_BTN = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    GOTO_CART_ICON = (By.CSS_SELECTOR, 'a[href="/gp/cart/view.html?ref_=nav_cart"]')
    BEST_SELLER_BTN = (By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


    def click_product(self):
        self.click(*self.PARTICULAR_PRODUCT)

    def click_orders(self):
        self.click(*self.RETURN_ORDERS_BTN)


    def click_cart_btn(self):
        self.click(*self.GOTO_CART_ICON)


    def click_best_seller_btn(self):
        self.click(*self.BEST_SELLER_BTN)


    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(*self.SIGNIN_BTN)


    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_clickable(*self.SIGNIN_BTN)








