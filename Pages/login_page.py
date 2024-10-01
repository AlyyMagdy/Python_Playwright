import os
import json
import logging
from playwright.sync_api import expect,Page
from Utils.data_generator import *

# load_dotenv()
class LoginPage():

    def __init__(self,page: Page) -> None:
        self.driver = page
    email_field = "//input[contains(@id,'email')]"
    password_field = "//input[contains(@id,'password')]"
    login_btn_form = "//input[contains(@value,'Log in')]"


    def login_with_random_data(self):
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        with open('./Test_Data/generated_data.json') as f:
            test_data = json.load(f)
        self.driver.fill(self.email_field,test_data['username']+"@gmail.com")
        self.driver.fill(self.password_field,test_data['password'])
        self.driver.click(self.login_btn_form)
    
    def is_user_logged_in_successfully(self):
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        return True
    

    def log_requests(self,page, requests_data):
        def handle_request(route):
            request = route.request
            # Capture the request details
            request_info = {
                'url': request.url,
                'method': request.method,
                'headers': dict(request.headers),
            }
            
            # Capture request POST data if available
            if request.method == "POST":
                post_data = request.post_data
                if post_data:
                    request_info['post_data'] = post_data
            
            # Append the request info to the list
            requests_data.append(request_info)
            route.continue_()
        
        # Intercept and log every request
        page.route("**/*", handle_request)