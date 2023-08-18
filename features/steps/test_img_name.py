# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from time import sleep
#
#
#
# PRODUCT_NAME = (By.CSS_SELECTOR, '.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2')
# PRODUCT_IMAGE = (By.CSS_SELECTOR, 'div.a-section.aok-relative.s-image-fixed-height img.s-image')
#
# @then('Verify every product has a product name and product image')
# def find_pdt_name_img(context):
#      prdt_name = []
#      prdt_img =[]
#
#      name = context.driver.find_elements(*PRODUCT_NAME)
#      for n2 in name[:62]:
#          n3 = context.driver_find_elements(*PRODUCT_NAME).text