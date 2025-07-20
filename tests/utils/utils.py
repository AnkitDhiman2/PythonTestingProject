import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

mylogger = logging.getLogger()


def navigate_to(driver: WebDriver, url: str):
    url = url.strip()
    prefix = "https://"
    if prefix not in url:
        url = prefix + url
    driver.get(url)


def get_title(driver: WebDriver):
    return driver.title


def find_element(driver: WebDriver, by: By, locator: str) -> WebElement:
    return driver.find_element((by, locator))


def find_elements(driver: WebDriver, by: By, locator: str):
    return driver.find_elements((by, locator))


def click(element: WebElement):
    return element.click()


def send_keys(element: WebElement, value: str):
    return element.send_keys(str)


def right_click(
    driver: WebDriver,
):
    action_chain = webdriver.ActionChains(driver=driver)

    action_chain.context_click()
