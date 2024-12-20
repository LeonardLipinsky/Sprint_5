from locators import Locators

class TestTabs:
    def test_burger_constructor(self, driver):
        driver.find_element(*Locators.SAUCE_TAB).click()
        sauce = driver.find_element(*Locators.SAUCE_TAB_TEXT).text
        assert sauce == 'Соусы'
        driver.find_element(*Locators.FILLINGS_TAB).click()
        fillings = driver.find_element(*Locators.FILLINGS_TAB_TEXT).text
        assert fillings == 'Начинки'
        driver.find_element(*Locators.BUNS_TAB).click()
        buns = driver.find_element(*Locators.BUNS_TAB_TEXT).text
        assert buns == 'Булки'
