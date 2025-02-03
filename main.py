from core.general import *

from selenium import webdriver
from selenium.webdriver.common.by import By as by

import lib.driver
import lib.scraper as scraper
import lib.problem as problem
import lib.store as store

import json
import time

DELAY = 2

driver = lib.driver.get_driver()

def auto_login():
    username, password = read_from_file('.env').split('\n')[:2]

    # Goto homepage

    lib.driver.get_login_page(driver)

    time.sleep(DELAY)

    scraper.login(driver, username, password)

    return

def auto():
    auto_login()
    solution = store.load_solution()
    for i in range(int(input('Enter Repeat times:'))):
        scraper.goto_exam(driver)
        time.sleep(DELAY)
        scraper.start_exam(driver)
        time.sleep(DELAY)
        ans = problem.init(driver)
        # write_solution()

        while problem.last_page(driver):
            pass

        n = len(ans)
        debug(ans)
        for i in range(n):
            _id = ans[i][0]
            choice = problem.get_choice(driver)
            now = solution.get(_id, -1)
            # debug(ans[i][1])
            while now == -1:
                sel = input('Input the answer: ')
                try:
                    sel = int(sel)
                    assert(1 <= sel <= 3)
                    now = sel
                    break
                except:
                    warning('Invalid selection.')
                    continue
            solution[_id] = now
            choice[now - 1].click()
            info(f'Selecting option {ans[i][1][now - 1]}')
            if i == n - 1:
                break
            problem.next_page(driver)
            store.write_solution(solution)

def main():
    auto()
    # ouob

if __name__ == '__main__':
    main()