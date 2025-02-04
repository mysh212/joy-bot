from core.general import *

from selenium import webdriver
from selenium.webdriver.common.by import By as by

import json

def read_id(driver):
    return driver.find_element(by = by.CLASS_NAME, value = 'question-id').text.replace('ID: ', '')

def next_page(driver) -> bool:
    if len(driver.find_elements(by = by.ID, value = 'bt_next')) == 0:
        warning('No page left. Ignoring.')
        return False
    driver.find_element(by = by.ID, value = 'bt_next').click()
    return True
    
def last_page(driver) -> bool:
    if len(driver.find_elements(by = by.CLASS_NAME, value = 'btn-primary')) < 2 and len(driver.find_elements(by = by.ID, value = 'bt_next')) != 0:
        warning('No page left. Ignoring.')
        return False
    driver.find_element(by = by.CLASS_NAME, value = 'btn-primary').click()
    return True

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

def try_play(driver):
    try:
        driver.execute_script("document.querySelector('audio').play();");
        return True
    except:
        return False