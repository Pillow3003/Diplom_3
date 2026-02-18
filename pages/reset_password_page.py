import urls
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
import allure

class ResetPasswordPage(BasePage):
    """
    Страница сброса пароля.
    Методы для взаимодействия с элементами страницы обновления пароля.
    """

    @allure.step('Ожидаем загрузки страницы обновления пароля')
    def wait_load_reset_password_page(self):
        """
        Ожидает, что текущий URL совпадает с URL страницы сброса пароля.
        Используется для проверки, что страница загрузилась.
        """
        self.wait_for_url(urls.RESET_PASSWORD_PAGE)

    @allure.step('Нажимаем на кнопку демонстрации пароля')
    def click_show_password(self):
        """
        Ищет и кликает на кнопку, позволяющую показать введённый пароль.
        Обычно переключает поле ввода пароля между типами 'password' и 'text'.
        """
        self.wait_and_find_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        self.click_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Получаем класс поля для ввода нового пароля')
    def get_password_input_class_name(self):
        """
        Возвращает значение атрибута 'class' у поля ввода нового пароля.
        Это полезно для определения состояния поля, например, подсветки ошибки.
        
        :return: str — класс(ы) элемента поля ввода пароля.
        """
        element_class = self.wait_and_find_element(ResetPasswordPageLocators.NEW_PASSWORD_INPUT).get_attribute('class')
        return element_class