from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@when('Input a product')
def product_name(context):
    context.driver.find_element(By.ID,'twotabsearchtextbox').send_keys('iphone')
    context.driver.find_element(By.CSS_SELECTOR,"#nav-search-submit-button").click()
    sleep(2)


@then('select a particular product')
def product_click(context):
    context.driver.find_element(By.CSS_SELECTOR,".a-section.aok-relative.s-image-fixed-height").click()
    sleep(2)


@then('Add product to the cart')
def product_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'#add-to-cart-button').click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]').click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR,'a[href="/cart?ref_=sw_gtc"]').click()
    sleep(2)


@then('Verify the added item is in the cart')
def added_item(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,'#sc-subtotal-label-buybox').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

