import requests
import json
import logging
import os
from Utils.data_generator import *
from Pages.registeration_login_api_page import RegisterationLoginAPIPage
class API_Keywords():
    def __init__(self):
        self.registerationLoginAPIPage = RegisterationLoginAPIPage()
    
    def registeration_data_is_generated(self):
        global test_data
        test_data = generate_user_data()
        return test_data

    def user_register_by_API(self):
        self.registerationLoginAPIPage.post_request_register_and_validate_response(test_data)
    
    def user_login_by_API(self):
        self.registerationLoginAPIPage.post_request_login_and_validate_response(test_data)

    def add_user_and_verify_status_code(self,name,job):
        response = self.registerationLoginAPIPage.post_request_and_get_response(name,job)
        self.registerationLoginAPIPage.verify_response(response,name,job)
