import pytest
from selenium import webdriver
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).click()
    driver.find_element(*Locators.FIELD_FOCUSED).send_keys('name2@name.com')
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
    driver.find_element(*Locators.ENTER_ACCOUNT_LOGIN_BUTTON).click()
    return driver