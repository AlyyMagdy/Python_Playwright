*** Settings ***
Library        Keywords/UI_Keywords.py

Test Teardown        close browser and application

*** Test Cases ***
Register User With Generated Data
    Given User opens application
    When User clicks on register button
    And User register with random generated data
    Then User registered successfully

Login With The Generated Data
    Given User opens application
    When User clicks on login button
    And User login with random generated data
    Then User logged in successfully

Register With The existing Generated Data
    Given User opens application
    When User clicks on register button
    And User register with existing generated data
    Then Verify Error Message Appears

Verify Compatibility When Changing Resolution To Mobile
    Given User opens application
    Then Verify Compatibility In Mobile Resolution
    