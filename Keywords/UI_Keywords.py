from Pages.registeration_page import RegisterationPage
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Utils.Browser_init import Browser_Init
import json
class UI_Keywords():
    def __init__(self):
        self.requests_data = []
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.driver = Browser_Init.get_instance()
        self.registerationPage = RegisterationPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.log_requests(self.driver,self.requests_data)
    def user_opens_application(self):
        """
            Initiate Browser and Open the application URL
        """
        self.registerationPage.open()
    
    def close_browser_and_application(self):
        with open("requests_data.json", "w") as file:
            json.dump(self.requests_data, file, indent=4)
        Browser_Init.close_browser()

    def user_clicks_on_register_button(self):
        """
            User Clicks On Register Button On Home Page
        """
        self.homePage.click_on_register_btn()
    
    def user_clicks_on_login_button(self):
        """
            User Clicks On Login Button On Home Page
        """
        self.homePage.click_on_login_btn()

    def user_register_with_random_generated_data(self):

        self.registerationPage.register_with_random_data()

    def user_register_with_existing_generated_data(self):
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.registerationPage.register_with_existing_random_data()
    def user_registered_successfully(self):
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        assert self.registerationPage.is_user_registered_successfully(), "Account Not Registered."

    def user_login_with_random_generated_data(self):
        self.loginPage.login_with_random_data()

    def user_logged_in_successfully(self):
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        assert self.registerationPage.is_user_registered_successfully(), "Account Not Registered."

    def verify_error_message_appears(self):
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        assert self.registerationPage.is_error_message_appeared() , "Existing account got registered again."

    def verify_compatibility_in_mobile_resolution(self):
        import sys,pdb;pdb;pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.homePage.change_mobile_resolution_and_verify_compatibility()