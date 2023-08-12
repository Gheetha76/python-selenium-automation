from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

AMAZON_CUSTOMER_SERVICE = (By.CSS_SELECTOR,'a[href="/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice"]')
WELCOME_CUSTOMER = (By.CSS_SELECTOR,'h1.fs-heading.bolded')
ISSUE_CARD = (By.CSS_SELECTOR,'.issue-card-container')
UI_ELEMENTS = (By.CSS_SELECTOR,'.issue-card-wrapper')
SEARCH_HELP_SEARCH = (By.CSS_SELECTOR,'h2.fs-heading.bolded')
INPUT_FIELD = (By.CSS_SELECTOR,'.a-input-text.a-span12')
ALL_HELP_TOPICS = (By.CSS_SELECTOR,'.help-topics')

@when('Click on Amazon Customer Service tab')
def open_amazon_customer_service(context):
    context.driver.find_element(*AMAZON_CUSTOMER_SERVICE).click()

@when('Check for UI elements are visible')
def ui_elements(context):
    context.driver.find_element(*WELCOME_CUSTOMER)
    context.driver.find_element(*ISSUE_CARD)
    # context.driver.find_element(*UI_ELEMENTS)

@then('Verify all {num} UI elements')
def elements_ui(context,num):
    num = int(num)
    num3 = context.driver.find_elements(*UI_ELEMENTS)
    assert len(num3) == num, f'Error, expected {num} links but got {len(num3)}'

@then('Check for search help library')
def search_help_library(context):
    context.driver.find_element(*SEARCH_HELP_SEARCH)

@then('Check for input field to search library')
def input_field(context):
    context.driver.find_element(*INPUT_FIELD)

@then('Verify all {h1} links under all help topics')
def verify_link(context,h1):
    h1 = int(h1)
    h2 = context.driver.find_elements(*ALL_HELP_TOPICS)
    assert len(h2) == h1, f'Error, expected {h1} but got only {len(h2)}'