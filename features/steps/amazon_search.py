from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def amazon_1_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Returns and orders')
def return_orders(context):
    context.driver.find_element(By.ID,'nav-orders').click()


@then('Verify sign In page opens')
def sign_in_page_opens(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "// h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then('Verify email input field is present')
def email_input_field(context):
    expected_result = context.driver.find_element(By.XPATH,"// input[@type='email']").is_displayed()
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '#ap_email').is_displayed()
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


