import urls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
import allure

class FeedPage(BasePage):
    """
    Страница ленты заказов.
    Методы для взаимодействия с лентой заказов и получения информации.
    """

    @allure.step('Ожидаем загрузки страницы с лентой заказов')
    def wait_load_feed_page(self):
        """
        Ожидает полной загрузки страницы ленты заказов по URL.
        """
        self.wait_for_url(urls.FEED_ORDERS_LIST_PAGE)

    @allure.step('Проверяем наличие номера заказа в списке ленты')
    def check_id_order_in_feed(self, order_id):
        locator = FeedPageLocators.id_order_card_in_feed_with_substitutions
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.wait_and_find_element(locator_with_order_id)
        return self.check_element_visibility(locator_with_order_id)

    @allure.step('Получаем всплывающее окно с информацией о заказе')
    def get_order_modal_window(self):
        """
        Возвращает элемент всплывающего окна с деталями заказа.
        :return: веб-элемент окна.
        """
        return self.wait_and_find_element(FeedPageLocators.MODAL_WINDOW_HEAD)

    @allure.step('Получаем номер заказа')
    def get_order(self):
        """
        Получает номер заказа из элемента.
        :return: строка с номером заказа.
        """
        element = self.wait_and_find_element(FeedPageLocators.ORDERS)
        return element.text

    @allure.step('Получаем число заказов за все время')
    def get_count_orders_all_time(self):
        """
        Получает общее количество заказов за все время.
        :return: целое число — количество заказов.
        """
        element = self.wait_and_find_element(FeedPageLocators.ORDER_COUNTER_ALL_TIME)
        return int(element.text)

    @allure.step('Получаем число заказов за сегодня')
    def get_count_orders_today(self):
        """
        Получает количество заказов за сегодняшний день.
        :return: целое число — количество заказов.
        """
        element = self.wait_and_find_element(FeedPageLocators.ORDER_COUNTER_TODAY)
        return int(element.text)

    @allure.step('Получаем список заказов в обработке')
    def get_orders_in_process(self):
        """
        Ожидает появления заказов в обработке и возвращает их номера.
        :return: строка с номерами заказов, очищенная от символов '#'.
        """
        self.wait_and_find_element(FeedPageLocators.NO_ORDERS_IN_PROCESS)
        self.wait_element_disappearing(FeedPageLocators.NO_ORDERS_IN_PROCESS)
        element = self.wait_and_find_element(FeedPageLocators.ORDER_IN_PROCESS)
        return element.text.lstrip('#')
