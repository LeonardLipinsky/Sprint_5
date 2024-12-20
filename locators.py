from selenium.webdriver.common.by import By


class Locators:
    REG_LINK = (By.LINK_TEXT, "Зарегистрироваться") #кнопка "зарегистрироваться"
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # кнопка "войти в аккаунт" на главной
    NAME_FIELD = (By.XPATH, "//label[contains(text(),'Имя')]") #поле имени
    FIELD_FOCUSED = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']//input[@name='name']")# поле авторизации/регистрации в фокусе
    EMAIL_FIELD = (By.XPATH, "//label[contains(text(),'Email')]") # поле эмейла
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']") # поле пароля
    REG_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # кнопка регистрации на странице регистрации
    LOGIN_HEADER = (By.XPATH,"//h2[contains(text(),'Вход')]") # заголовок страницы входа
    REG_FAILURE_TEXT = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]") # текст ошибки пароля на странице регистрации
    ENTER_ACCOUNT_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка входа на странице входа
    ORDER_BUTTON_TEXT = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # кнопка оформления заказа на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # кнопка личного кабинета
    REG_ENTER_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]") # кнопка войти на экране регистрации
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # кнопка восстановления пароля на странице входа
    PERSONAL_ACCOUNT_TEXT = (By.XPATH, "//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]") # текст подсказка в личном кабинете
    CONSTRUCT_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]") # кнопка перехода в конструктор
    EXIT_BUTTON = (By.XPATH, " //button[contains(text(),'Выход')]") # кнопка выхода из личного кабинета
    SAUCE_TAB = (By.XPATH,"//span[contains(text(),'Соусы')]") # выбор таба Соусы
    SAUCE_TAB_TEXT = (By.XPATH, "//h2[contains(text(),'Соусы')]") # текст таба Соусы
    BUNS_TAB = (By.XPATH,"//span[contains(text(),'Булки')]") # выбор таба Булки
    BUNS_TAB_TEXT = (By.XPATH, "//h2[contains(text(),'Булки')]") # текст таба Булки
    FILLINGS_TAB = (By.XPATH, "//span[contains(text(),'Начинки')]") # выбор таба Начинки
    FILLINGS_TAB_TEXT = (By.XPATH, "//h2[contains(text(),'Начинки')]") # текст таба Начинки