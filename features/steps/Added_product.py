from behave import given, when, then
from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_NAME = (By.ID,'twotabsearchtextbox')
SEARCH_BUTTON = (By.CSS_SELECTOR,"#nav-search-submit-button")
PARTICULAR_PRODUCT= (By.CSS_SELECTOR,".a-section.aok-relative.s-image-fixed-height")
PRODUCT_ADD = (By.CSS_SELECTOR,'#add-to-cart-button')
THANKS_BUTTON = (By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]')
CART_ADD = (By.CSS_SELECTOR,'a[href="/cart?ref_=sw_gtc"]')
SUB_TOTAL_ITEM = (By.CSS_SELECTOR,'#sc-subtotal-label-buybox')


@when('Input a product')
def product_name(context):
    # context.driver.find_element(*SEARCH_NAME).send_keys('Apple Watch')
    # # # context.driver.find_element(*SEARCH_BUTTON).click()
    # context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BUTTON)).click()
    context.app.header.search_product('Apple Watch')



@then('select a particular product')
def product_click(context):
    context.driver.find_element(*PARTICULAR_PRODUCT).click()



@then('Add product to the cart')
def add_product_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_ADD)).click()

    # context.driver.find_element(*PRODUCT_ADD).click()

    context.driver.find_element(*THANKS_BUTTON).click()

    context.driver.find_element(*CART_ADD).click()



@then('Verify the added item is in the cart')
def added_item(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(*SUB_TOTAL_ITEM).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

