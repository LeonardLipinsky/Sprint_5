from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators

class TestBurgerExit:
    def test_burger_exit(self, driver, login): #выход из аккаунта
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.implicitly_wait(5)
        driver.find_element(*Locators.EXIT_BUTTON).click()
        enter_text = driver.find_element(*Locators.LOGIN_HEADER).text
        assert enter_text == 'Вход'
        driver.quit()