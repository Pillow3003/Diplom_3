from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    """
    Страница авторизации.
    Методы для взаимодействия с полями и элементами страницы логина.
    """

    @allure.step('Заполняем поле "email"')
    def fill_email_field(self, email: str):
        """
        Вводит электронную почту в поле "Email".

        :param email: строка с email пользователя.
        """
        self.send_data_into_field(LoginPageLocators.INPUT_EMAIL, email)

    @allure.step('Заполняем поле "Пароль"')
    def fill_password_field(self, password: str):
        """
        Вводит пароль в поле "Пароль".

        :param password: строка с паролем пользователя.
        """
        self.send_data_into_field(LoginPageLocators.INPUT_PASSWORD, password)

    @allure.step('Авторизуем пользователя')
    def input_user_data(self, email: str, password: str):
        """
        Заполняет поля email и пароль, затем нажимает кнопку входа.

        :param email: электронная почта пользователя.
        :param password: пароль пользователя.
        """
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Нажимаем кнопку "Восстановить пароль"')
    def click_restore_password(self):
        """
        Кликает по ссылке для перехода на страницу восстановления пароля.
        """
        self.wait_and_find_element(LoginPageLocators.RESTORE_PASSWORD_LINK)
        self.click_element(LoginPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step('Нажимаем кнопку "Конструктор"')
    def click_constructor_button(self):
        """
        Нажимает кнопку "Конструктор".
        """
        self.wait_and_find_element(LoginPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(LoginPageLocators.CONSTRUCTOR_BUTTON)