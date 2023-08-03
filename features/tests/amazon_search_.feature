# Created by Gheethvijay at 8/1/23
Feature: Testing if user can sign In when clicking on Returns and orders after logging out


  Scenario: Verify logged out user sees sign In when clicking on Returns and orders
     Given  Open Amazon page
     When   Click on Returns and orders
     Then   Verify sign In page opens
     Then   Verify email input field is present