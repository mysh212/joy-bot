from core.general import *

from selenium import webdriver
from selenium.webdriver.common.by import By as by

import json

def load_solution() -> dict:
    solution = json.loads(read_from_file('solution.json')) if exist('solution.json') else {}
    return solution

def write_solution(solution):
    if len(json.loads(read_from_file('solution.json') if exist('solution.json') else {})) > len(solution):
        warning('Old file is larger than the new one, storing the old file into solution.bkp.json')
        write_to_file('solution.json', read_from_file('solution.json'))
    write_to_file('solution.json', json.dumps(solution))
    sig = len(json.loads(read_from_file('solution.json')))
    info(f'There are {sig} solution records in database.')