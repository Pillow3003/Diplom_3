import urls
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
import allure

class AccountPage(BasePage):
    """
    Страница аккаунта пользователя.
    Содержит методы для получения информации и взаимодействия с аккаунтом.
    """

    @allure.step('Получаем имя клиента из поля "Имя"')
    def get_text_name_field(self):
        """
        Возвращает значение текста в поле с именем клиента.
        :return: строка с именем клиента
        """
        client_name = self.wait_and_find_element(AccountPageLocators.CLIENT_NAME).get_property('value')
        return client_name

    @allure.step('Переходим на страницу "История заказов"')
    def go_to_order_history(self):
        """
        Кликает по ссылке "История заказов" для перехода на страницу истории заказов.
        """
        self.wait_and_find_element(AccountPageLocators.ORDER_HISTORY_LINK).click()

    @allure.step('Получаем номер первого заказа пользователя из истории заказов')
    def get_user_order(self):
        """
        Возвращает текст номера первого заказа из истории заказов пользователя.
        :return: строка с номером заказа
        """
        element = self.wait_and_find_element(AccountPageLocators.ORDER_NUMBER)
        return element.text

    @allure.step('Выход из аккаунта')
    def logout(self):
        """
        Выполняет клик по кнопке выхода из аккаунта.
        """
        self.click_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Ожидаем загрузку страницы авторизации')
    def wait_load_login_page(self):
        """
        Ожидает, что текущий URL соответствует странице авторизации.
        """
        self.wait_for_url(urls.LOGIN_PAGE)