
from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    RETURN_ORDERS_ICON = (By.ID, 'nav-orders')
    SIGN_IN_PAGE_CHECK = (By.XPATH, "// h1[@class='a-spacing-small']")
    EPR_EMAIL_INPUT = (By.XPATH, "// input[@type='email']")
    ACTR_EMAIL_FIELD = (By.CSS_SELECTOR, '#ap_email')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


    def returns_and_orders(self):
        self.click(*self.RETURN_ORDERS_ICON)

    def verify_sign_in_page_opens(self,text1):
        actual_text1 = self.find_element(*self.SIGN_IN_PAGE_CHECK).text
        assert actual_text1 == text1, \
            f'Error, expected {text1} did not match actual {actual_text1}'


    def verify_email_input_field(self):
         expected_result = self.display(*self.EPR_EMAIL_INPUT)
         actual_result = self.display(*self.ACTR_EMAIL_FIELD)
         assert expected_result == actual_result, \
             f'Error, expected {expected_result} did not match actual {actual_result}'






