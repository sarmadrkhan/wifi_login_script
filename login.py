from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

driver = webdriver.Chrome()

def is_logged_in():
    logout_button = driver.find_elements(By.CSS_SELECTOR, "body form [value='Logout']")
    return len(logout_button) > 0

def login(usernameId, passwordId, submit_buttonId):
    with open('loginDetails.yml') as file:
        conf = yaml.safe_load(file)
    username = conf['wifi_user']['userid']
    password = conf['wifi_user']['password']
    url = conf['url']

    driver.get(url)

    if not is_logged_in():
        driver.find_element(By.ID, usernameId).send_keys(username)
        driver.find_element(By.ID, passwordId).send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "body > form > p.submit > input[type=submit]").click()

login("auth_user", "auth_pass", "loginbutton")
