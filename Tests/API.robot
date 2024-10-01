*** Settings ***
Library        Keywords/API_Keywords.py


*** Test Cases ***
Generate Data & Register & Login 
    Given registeration data is generated
    When User register by API
    Then User login by API

Simple Request & Verify Status Code
    Add User and verify status code   John    Software Engineer
