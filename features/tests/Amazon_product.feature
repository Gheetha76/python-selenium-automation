# Created by Gheethvijay at 8/1/23
Feature:  Check if the cart has the added items






  Scenario:Verify if the added product is in the cart
     Given  Open Amazon page
      When  Input a product
      Then  select a particular product
      Then  Add product to the cart
      Then  Verify the added item is in the cart




