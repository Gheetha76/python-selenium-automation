from selenium.webdriver.common.by import By
from behave import *
from time import sleep




COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')




@then('Verify that the user can click on each color and select it')
def verify_can_click_colors(context):

    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage', 'Dark Indigo', 'Dark Wash', 'Indigo Wash',
                   'Light Wash', 'Medium Blue Vintage', 'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black',
                   'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive', 'Light Blue Vintage',
                   'Washed Grey', 'Sage Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'