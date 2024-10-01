import os
import json
import logging
from playwright.sync_api import expect,Page
from Utils.data_generator import *

# load_dotenv()
class HomePage():

    def __init__(self,page: Page) -> None:
        self.driver = page
    register_btn = "//a[@class='theme-btn register-btn']"
    login_btn = "//div[contains(@class,'login-btn')]//a[@class='theme-btn']"
    home_logo = "//div[@class='logo']"
    mobile_resolutions = [
    {"device": "iPhone X", "width": 375, "height": 812},
    {"device": "Samsung Galaxy S9", "width": 360, "height": 740},
]

    def click_on_register_btn(self):
        self.driver.click(self.register_btn)

    def click_on_login_btn(self):
        self.driver.click(self.login_btn)

    def change_mobile_resolution_and_verify_compatibility(self):
        for res in self.mobile_resolutions:
            self.driver.set_viewport_size({"width": res['width'], "height": res['height']})
            assert self.driver.is_visible(self.home_logo)
            assert self.driver.viewport_size == {"width": res['width'], "height": res['height']}