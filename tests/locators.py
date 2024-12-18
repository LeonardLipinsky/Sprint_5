from selenium.webdriver.common.by import By


class Locators:
    REG_LINK = (By.LINK_TEXT, "Зарегистрироваться") #кнопка "зарегистрироваться"
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # кнопка "войти в аккаунт" на главной
    REG_NAME_FIELD = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]") # поле имени на странице регистрации
    REG_EMAIL_FIELD = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]") # поле эмейла на странице регистрации
    REG_PASSWORD_FIELD = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]") # поле пароля на странице регистрации
    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # кнопка регистрации на странице регистрации
    LOGIN_HEADER = (By.XPATH,"//h2[contains(text(),'Вход')]") # заголовок страницы входа
    REG_FAILURE_TEXT = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]") # текст ошибки пароля на странице регистрации
    ENTER_EMAIL_FIELD = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]") # поле эмейла на странице входа
    ENTER_PASSWORD_FIELD = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]") # поле пароля на странице входа
    ENTER_ACCOUNT_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка входа на странице входа
    ORDER_BUTTON_TEXT = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # кнопка оформления заказа на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//header/nav[1]/a[1]") # кнопка личного кабинета
    REG_ENTER_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]") # кнопка войти на экране регистрации
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # кнопка восстановления пароля на странице входа
    PERSONAL_ACCOUNT_TEXT = (By.XPATH, "//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]") # текст подсказка в личном кабинете
    CONSTRUCT_BUTTON = (By.XPATH, "//header/nav[1]/ul[1]/li[1]/a[1]") # кнопка перехода в конструктор
    EXIT_BUTTON = (By.XPATH, " //button[contains(text(),'Выход')]") # кнопка выхода из личного кабинета
    SAUCE_TAB = (By.CSS_SELECTOR,"div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) section.BurgerIngredients_ingredients__1N8v2 div:nth-child(2) > div.tab_tab__1SPyG.pt-4.pr-10.pb-4.pl-10.noselect:nth-child(2)") # выбор таба Соусы
    SAUCE_TAB_TEXT = (By.XPATH, "//h2[contains(text(),'Соусы')]") # текст таба Соусы
    BUNS_TAB = (By.CSS_SELECTOR,"div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) section.BurgerIngredients_ingredients__1N8v2 div:nth-child(2) > div.tab_tab__1SPyG.pt-4.pr-10.pb-4.pl-10.noselect:nth-child(1)") # выбор таба Булки
    BUNS_TAB_TEXT = (By.XPATH, "//h2[contains(text(),'Булки')]") # текст таба Булки
    FILLINGS_TAB = (By.CSS_SELECTOR, "div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) section.BurgerIngredients_ingredients__1N8v2 div:nth-child(2) > div.tab_tab__1SPyG.pt-4.pr-10.pb-4.pl-10.noselect:nth-child(3)") # выбор таба Начинки
    FILLINGS_TAB_TEXT = (By.XPATH, "//h2[contains(text(),'Начинки')]") # текст таба Начинки