from behave import given, when, then
from selenium.webdriver.common.by import By



RETURN_ORDERS_ICON = (By.ID,'nav-orders')
SIGN_IN_PAGE_CHECK = (By.XPATH,"// h1[@class='a-spacing-small']")
EPR_EMAIL_INPUT= (By.XPATH,"// input[@type='email']")
ACTR_EMAIL_FIELD = (By.CSS_SELECTOR, '#ap_email')

@given('Open Amazon page')
def open_amazon_page(context):
    # context.driver.get('https://www.amazon.com/')
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click on Returns and orders')
def return_orders(context):
    # context.driver.find_element(*RETURN_ORDERS_ICON).click()
    context.app.header.returns_and_orders()


@then('Verify {text} page opens')
def sign_in_page_opens(context,text):
    # expected_result = 'Sign in'
    # actual_result = context.driver.find_element(*SIGN_IN_PAGE_CHECK).text
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.header.verify_sign_in_page_opens(text)

@then('Verify email input field is present')
def email_input_field(context):
    # expected_result = context.driver.find_element(*EPR_EMAIL_INPUT).is_displayed()
    # actual_result = context.driver.find_element(*ACTR_EMAIL_FIELD ).is_displayed()
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.header.verify_email_input_field()

