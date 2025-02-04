from core.general import *

from selenium import webdriver
from selenium.webdriver.common.by import By as by

import json

def get_driver():
    #Simple assignment
    from selenium.webdriver import Chrome

    from selenium.webdriver import ChromeOptions
    pre = ChromeOptions()
    pre.headless = True

    driver = Chrome(options = pre)

    return driver

def get_login_page(driver):
    url = 'https://testcloud.joy.com.tw/index.php?option=user_login'
    driver.get(url)
    return