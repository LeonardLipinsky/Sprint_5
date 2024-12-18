from tests.locators import Locators

class TestBurgerCabinet:
    def test_burger_cabinet(self, driver, login): #вход в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.implicitly_wait(5)
        personal_account_text = driver.find_element(*Locators.PERSONAL_ACCOUNT_TEXT).text
        assert personal_account_text == 'В этом разделе вы можете изменить свои персональные данные'
        driver.quit()

    def test_burger_cabinet_to_construct(self, driver, login): #переход с личного кабинета в конструктор
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCT_BUTTON).click()
        driver.implicitly_wait(5)
        order_button_text = driver.find_element(*Locators.ORDER_BUTTON_TEXT).text
        assert order_button_text == 'Оформить заказ'
        driver.quit()