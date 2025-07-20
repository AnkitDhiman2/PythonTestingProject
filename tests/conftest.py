"""
File containg the fixture being used throughout the framework
"""

import logging
import pytest
from selenium import webdriver
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as co
import configparser

config = configparser.ConfigParser()
mylogger = logging.getLogger()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def driver(request):
    """
    Fixture to return browser driver
    """
    browser_name = request.config.getoption("--browser")
    driver = None
    config.read("pytest.ini")

    match browser_name:
        case "chrome":
            chrome_options = co()
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-third-party-cookies")
            chrome_service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        case "firefox":
            raise NotImplementedError("Firefox driver not available")
        case "edge":
            raise NotImplementedError("Edge driver not available")
        case _:
            err_msg = f"Unknown browser type '{browser_name}'"
            mylogger.error(err_msg)
            raise NoSuchDriverException(err_msg)

    page_load_out_time = config["DEFAULT"]["page_load_out_time"]
    driver.set_page_load_timeout(page_load_out_time)

    yield driver

    driver.quit()
