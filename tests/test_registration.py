from faker import Faker
from tests.locators import Locators

faker = Faker()

class TestBurgerRegistration:
    def test_registration_success(self, driver): #успешная регистрация
        email = faker.email()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME_FIELD).send_keys('Name')
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.implicitly_wait(5)
        reg_text = driver.find_element(*Locators.LOGIN_HEADER).text
        assert reg_text == 'Вход'
        driver.quit()

    def test_registration_failure(self, driver): #ошибка пароля
        email = faker.email()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.REG_NAME_FIELD).send_keys('Name')
        driver.find_element(*Locators.REG_EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.implicitly_wait(5)
        reg_failure_text = driver.find_element(*Locators.REG_FAILURE_TEXT).text
        assert reg_failure_text == 'Некорректный пароль'
        driver.quit()