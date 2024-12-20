from faker import Faker
from locators import Locators

faker = Faker()

class TestBurgerRegistration:
    def test_registration_success(self, driver):
        email = faker.email()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.NAME_FIELD).click()
        driver.find_element(*Locators.FIELD_FOCUSED).send_keys('Name')
        driver.find_element(*Locators.EMAIL_FIELD).click()
        driver.find_element(*Locators.FIELD_FOCUSED).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.implicitly_wait(5)
        reg_text = driver.find_element(*Locators.LOGIN_HEADER).text
        assert reg_text == 'Вход'

    def test_registration_failure(self, driver):
        email = faker.email()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.NAME_FIELD).click()
        driver.find_element(*Locators.FIELD_FOCUSED).send_keys('Name')
        driver.find_element(*Locators.EMAIL_FIELD).click()
        driver.find_element(*Locators.FIELD_FOCUSED).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.implicitly_wait(5)
        reg_failure_text = driver.find_element(*Locators.REG_FAILURE_TEXT).text
        assert reg_failure_text == 'Некорректный пароль'