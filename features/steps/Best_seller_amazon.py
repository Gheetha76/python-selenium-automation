from behave import given, when, then
from selenium.webdriver.common.by import By

SELLER_BEST_PAGE =(By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
NUMBER_OF_LINKS =(By.CSS_SELECTOR,'._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR')

@when('Click on best sellers')
def open_best_seller_page(context):
    context.driver.find_element(*SELLER_BEST_PAGE).click()


@then('verify if there are {n1} links')
def Verify_number_link(context,n1):
    n1 = int(n1)
    link_number = context.driver.find_elements(*NUMBER_OF_LINKS)
    assert len(link_number) == n1 , f'Error, expected {n1} but got only {len(link_number)}'
