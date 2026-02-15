import urls
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
import allure

class ForgotPasswordPage(BasePage):
    """
    Страница восстановления пароля.
    Методы для взаимодействия с формой восстановления пароля.
    """

    @allure.step('Ожидаем загрузки страницы "Восстановление пароля"')
    def wait_load_forgot_password_page(self):
        """
        Ожидает загрузки страницы восстановления пароля по URL.
        """
        self.wait_for_url(urls.FORGOT_PASSWORD_PAGE)

    @allure.step('Заполняем поле "email"')
    def fill_email_field(self, email):
        """
        Заполняет поле ввода email для восстановления пароля.
        :param email: строка с адресом электронной почты.
        """
        self.wait_and_find_element(ForgotPasswordPageLocators.EMAIL_INPUT)
        self.send_data_into_field(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_restore_password_button(self):
        """
        Нажимает кнопку для восстановления пароля.
        """
        self.wait_and_find_element(ForgotPasswordPageLocators.RESTORE_PASSWORD_BUTTON)
        self.click_element(ForgotPasswordPageLocators.RESTORE_PASSWORD_BUTTON)