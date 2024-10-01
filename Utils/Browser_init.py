# from config_data import browser_runner
from playwright.sync_api import sync_playwright
import logging
from dotenv import load_dotenv
import os
# Load .env file
load_dotenv()
class Browser_Init:

    _instance = None
    _playwright = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._playwright = sync_playwright().start()
            if os.getenv('BROWSER') == "chrome":
                browser = cls._playwright.chromium.launch(headless=False,args=["--start-maximized"]).new_context(no_viewport=True)
            elif os.getenv('BROWSER') == "firefox":
                browser = cls._playwright.firefox.launch(headless=False,args=["--start-maximized"]).new_context(no_viewport=True)
            elif os.getenv('BROWSER') == "webkit":
                browser = cls._playwright.webkit.launch(headless=False,args=["--start-maximized"]).new_context(no_viewport=True)
            else:
                raise ValueError(f"Invalid Browser Name {os.getenv('BROWSER')}")
            cls._instance = browser.new_page()
        return cls._instance
    
    @classmethod
    def close_browser(cls):
        if cls._instance:
            logging.info("Closing the browser")
            cls._instance.close()
            cls._instance = None
        if cls._playwright:
            cls._playwright.stop()
            cls._playwright = None