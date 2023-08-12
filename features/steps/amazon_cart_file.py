from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep





@when('Click on the cart icon')
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"a[href='/gp/cart/view.html?ref_=nav_cart']").click()
    sleep(4)



@then('Verify Your Amazon Cart is empty')
def amazon_cart_empty(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,".a-row.sc-your-amazon-cart-is-empty").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
