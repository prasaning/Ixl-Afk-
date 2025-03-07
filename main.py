import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from colorama import Fore
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.ixl.com/signin')

accountn = driver.find_element(By.ID, "siusername")
accountn.send_keys("YOUR USERNAME")

username = driver.find_element(By.ID, "sipassword")
username.send_keys("YOUR PASSWORD")

driver.find_element(By.ID, "signin-button").click()

time.sleep(3)


def solve_math_problem(problem):
    problem = problem.replace('–', '-').replace('−', '-')
    
    problem = problem.replace('=', '').strip()
    
    try:
        solution = eval(problem)
        return solution
    except Exception as e:
        print(f"Error solving problem: {e}")
        return None

if driver.current_url == "https://www.ixl.com/dashboard":
    login = True
    print("Logged in")
    driver.get("https://www.ixl.com/math/grade-7/add-and-subtract-integers")
    while True:
        time.sleep(3)
        variable = driver.find_element(By.CLASS_NAME,'old-space-indent').text
        print(variable)
        answer = solve_math_problem(variable)
    
        if answer is not None:
            print(f"Answer: {answer}")
        else:
            print("Couldn't solve the problem.")
            
        print('Waiting | 1 Minute 50 Seconds | Afk Timer')
        time.sleep(150)
        
        a = (answer)
        driver.find_element(By.CLASS_NAME,'fillIn').click()
        driver.find_element(By.CLASS_NAME,'fillIn').send_keys(a)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME,'fillIn').send_keys(Keys.ENTER)
        driver.refresh()
        

time.sleep(1999)
