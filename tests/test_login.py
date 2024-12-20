from faker import Faker
from locators import Locators

faker = Faker()

class TestBurgerLogin:
    def test_login_enter_account_button(self, driver):
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).click()
        driver.find_element(*Locators.FIELD_FOCUSED).send_keys('name2@name.com')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.ENTER_ACCOUNT_LOGIN_BUTTON).click()
        driver.implicitly_wait(5)
        order_button_text = driver.find_element(*Locators.ORDER_BUTTON_TEXT).text
        assert order_button_text == 'Оформить заказ'

    def test_login_personal_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).click()
        driver.find_element(*Locators.FIELD_FOCUSED).send_keys('name2@name.com')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.ENTER_ACCOUNT_LOGIN_BUTTON).click()
        driver.implicitly_wait(5)
        order_button_text = driver.find_element(*Locators.ORDER_BUTTON_TEXT).text
        assert order_button_text == 'Оформить заказ'

    def test_login_registration_screen(self, driver):
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).click()
        driver.find_element(*Locators.FIELD_FOCUSED).send_keys('name2@name.com')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.ENTER_ACCOUNT_LOGIN_BUTTON).click()
        driver.implicitly_wait(5)
        order_button_text = driver.find_element(*Locators.ORDER_BUTTON_TEXT).text
        assert order_button_text == 'Оформить заказ'

    def test_login_repair_password(self, driver):
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.REG_ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).click()
        driver.find_element(*Locators.FIELD_FOCUSED).send_keys('name2@name.com')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.ENTER_ACCOUNT_LOGIN_BUTTON).click()
        driver.implicitly_wait(5)
        order_button_text = driver.find_element(*Locators.ORDER_BUTTON_TEXT).text
        assert order_button_text == 'Оформить заказ'






