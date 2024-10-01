import os
import json
import logging
from playwright.sync_api import expect,Page
from Utils.data_generator import *

# load_dotenv()
class RegisterationPage():

    def __init__(self,page: Page) -> None:
        self.driver = page
    signup_with_email = "//button[contains(@data-test-id,'sign-up-with-email')]"
    register_full_name = "//input[@id='user_name']"
    register_email = "//input[@id='user_email']"
    register_password = "//input[@id='password']"
    registered_username = "//span[@class='navbar-current-user']"
    signup_button = "//input[contains(@data-testid,'signup-button')]"
    error_msg = "//span[@class='text-with-icon']//*"

    def open(self):
        self.driver.goto(url=os.getenv('URL'))
    
    def generate_data(self):
        global test_data
        test_data = generate_user_data()

    def register_with_random_data(self):
        # global test_data
        self.generate_data()
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.driver.wait_for_selector(self.signup_with_email)
        self.driver.click(self.signup_with_email)
        logging.info(f"============== filling full name : {test_data['username']}")
        self.driver.fill(self.register_full_name, test_data['username'])
        logging.info(f"============== filling email : {test_data['username']}@gmail.com")
        self.driver.fill(self.register_email, test_data['username']+"@gmail.com")
        logging.info(f"============== filling password : {test_data['password']}")
        self.driver.fill(self.register_password, test_data['password'])
        logging.info("============== Clicking on Sign Up Button")
        self.driver.click(self.signup_button)

    def register_with_existing_random_data(self):
        # global test_data
        with open('./Test_Data/generated_data.json') as f:
            test_data = json.load(f)
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.driver.wait_for_selector(self.signup_with_email)
        self.driver.click(self.signup_with_email)
        logging.info(f"============== filling full name : {test_data['username']}")
        self.driver.fill(self.register_full_name, test_data['username'])
        logging.info(f"============== filling email : {test_data['username']}@gmail.com")
        self.driver.fill(self.register_email, test_data['username']+"@gmail.com")
        logging.info(f"============== filling password : {test_data['password']}")
        self.driver.fill(self.register_password, test_data['password'])
        logging.info("============== Clicking on Sign Up Button")
        self.driver.click(self.signup_button)

    def is_user_registered_successfully(self):
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.driver.wait_for_selector(self.registered_username)
        username = self.driver.locator(self.registered_username).inner_text()
        
        if username.lower() == test_data['username']:
             with open('./Test_Data/generated_data.json', 'w') as f:
                json.dump(test_data, f)
                return True
        else:
            return False
    
    def is_error_message_appeared(self):
        self.driver.is_visible(self.error_msg)