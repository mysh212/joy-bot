from core.general import *

from selenium import webdriver
from selenium.webdriver.common.by import By as by

import json

def login(driver, username: str, password: str):
    # driver.find_element_by_css_selector('.username').text
    driver.find_elements(by = by.ID, value = 'username')[0].send_keys(username)
    driver.find_elements(by = by.ID, value = 'password-field')[0].send_keys(password)
    driver.find_elements(by = by.CLASS_NAME, value = 'btn-green-joy')[0].click()
    return

def goto_exam(driver):
    url = 'https://testcloud.joy.com.tw/index.php?option=list_exam_level'
    driver.get(url)

def start_exam(driver):
    driver.find_elements(by = by.CLASS_NAME, value = 'btn-primary')[0].click()

def get_choice_name(driver):
    return [i.text for i in driver.find_elements(by = by.TAG_NAME, value = 'label')]

def get_choice(driver):
    return driver.find_elements(by = by.TAG_NAME, value = 'label')

def init(driver):
    while last_page(driver):
        pass

    ans = [[read_id(driver), get_choice_name(driver)]]
    while next_page(driver):
        ans.append([read_id(driver), get_choice_name(driver)])
        get_choice(driver)[0].click()

    # debug(ans)
    return ans