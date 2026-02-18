import urls
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from random import choice
import allure

class HomePage(BasePage):
    """
    Страница Главная.
    Методы для взаимодействия с основными элементами домашней страницы.
    """

    @allure.step('Переходим в аккаунт пользователя по кнопке "Личный кабинет"')
    def click_account_cabinet_button(self):
        """
        Нажимает на кнопку "Личный кабинет".
        """
        self.wait_and_find_element(HomePageLocators.ENTER_CABINET_BUTTON)
        self.click_element(HomePageLocators.ENTER_CABINET_BUTTON)

    @allure.step('Переходим в аккаунт пользователя по кнопке "Войти в аккаунт"')
    def click_login_button(self):
        """
        Нажимает на кнопку "Войти в аккаунт".
        """
        self.wait_and_find_element(HomePageLocators.ENTER_ACCOUNT_BUTTON)
        self.click_element(HomePageLocators.ENTER_ACCOUNT_BUTTON)

    @allure.step('Ожидаем загрузки главной страницы')
    def wait_load_home_page(self):
        """
        Ожидает загрузки страницы: URL совпадает с базовым и загружены ключевые элементы.
        """
        self.wait_for_url(urls.BASE_URL)
        self.wait_and_find_element(HomePageLocators.BUN_INGREDIENTS_LIST)

    @allure.step('Переходим по кнопке "Лента заказов" в ленту заказов')
    def click_feed_button(self):
        """
        Нажимает на кнопку "Лента заказов" для перехода к заказам.
        """
        self.wait_and_find_element(HomePageLocators.FEED_BUTTON)
        self.click_element(HomePageLocators.FEED_BUTTON)

    @allure.step('Нажимаем на картинку ингридиента')
    def click_ingredient(self):
        """
        Нажимает на первый ингредиент в списке.
        """
        self.wait_and_find_element(HomePageLocators.FIRST_INGREDIENT)
        self.click_element(HomePageLocators.FIRST_INGREDIENT)

    @allure.step('Получаем всплывающее окно с инфо об ингридиенте')
    def get_ingredient_modal_window(self):
        """
        Возвращает элемент всплывающего окна с информацией об ингредиенте.
        """
        return self.wait_and_find_element(HomePageLocators.MODAL_INGREDIENT_HEAD)

    @allure.step('Проверяем отображение всплывающего окна с инфо об ингридиенте')
    def check_ingredient_modal_window(self):
        """
        Проверяет видимость окна с информацией о ингредиенте.
        :return: True, если окно видно, иначе False.
        """
        return self.check_element_visibility(HomePageLocators.MODAL_INGREDIENT_HEAD)

    @allure.step('Закрываем всплывающее окно с инфо об ингридиенте')
    def close_ingredient_modal_window(self):
        """
        Закрывает окно с информацией об ингредиенте.
        """
        self.wait_and_find_element(HomePageLocators.CLOSE_MODAL_INGREDIENT_BUTTON)
        self.click_element(HomePageLocators.CLOSE_MODAL_INGREDIENT_BUTTON)

    @allure.step('Выбираем ингридиент не булка из списка')
    def select_non_bun_ingredient(self):
        """
        Выбирает случайный ингредиент из списка НЕ булок.
        :return: элемент выбранного ингредиента.
        """
        ingredients = self.driver.find_elements(*HomePageLocators.NON_BUN_INGREDIENTS_LIST)
        print(f'Ingredients: {ingredients}')
        selected_ingredient = choice(ingredients)
        return selected_ingredient

    @allure.step('Выбираем ингридиент булка из списка')
    def select_bun_ingredient(self):
        """
        Выбирает случайный ингредиент из списка булок.
        :return: элемент выбранного булочного ингредиента.
        """
        ingredients = self.driver.find_elements(*HomePageLocators.BUN_INGREDIENTS_LIST)
        print(f'Ingredients: {ingredients}')
        selected_ingredient = choice(ingredients)
        return selected_ingredient

    @allure.step('Добавляем ингридиент в корзину')
    def add_basket_ingredient(self, ingredient):
        """
        Перетаскивает выбранный ингредиент в корзину.
        :param ingredient: веб-элемент ингредиента.
        """
        basket = self.wait_and_find_element(HomePageLocators.BASKET)
        self.drag_and_drop(ingredient, basket)

    @allure.step('Получаем счетчик выбранного ингридиента')
    def get_actual_counter(self, ingredient):
        """
        Получает текущий счетчик выбранного ингредиента.
        :param ingredient: веб-элемент ингредиента.
        :return: число — количество этого ингредиента в корзине.
        """
        return int(ingredient.text[0])

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_order_button(self):
        """
        Нажимает кнопку оформления заказа.
        """
        self.wait_and_find_element(HomePageLocators.MAKE_ORDER_BUTTON)
        self.click_element(HomePageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Получаем всплывающее окно вновь созданного заказа')
    def get_order_modal_window(self):
        """
        Возвращает элемент окна подтверждения нового заказа.
        """
        return self.wait_and_find_element(HomePageLocators.MODAL_NEW_ORDER_TEXT)

    @allure.step('Ожидаем обновления номера нового заказа')
    def wait_order_created(self):
        """
        Циклично ожидает появления номера нового заказа.
        :return: номер заказа.
        """
        order_number = "9999"
        while order_number == "9999":
            order_number = self.wait_and_find_element(HomePageLocators.MODAL_NEW_ORDER_NUMBER).text
        return order_number

    @allure.step('Получаем номер нового заказа')
    def get_order_number(self):
        """
        Получает номер последнего созданного заказа.
        :return: номер заказа в виде строки.
        """
        element = self.wait_and_find_element(HomePageLocators.MODAL_NEW_ORDER_NUMBER)
        return element.text

    @allure.step('Закрываем окно вновь созданного заказа')
    def close_order_modal_window(self):
        """
        Закрывает окно с информацией о новом заказе.
        """
        self.wait_and_find_element(HomePageLocators.CLOSE_MODAL_NEW_ORDER_BUTTON)
        self.click_element(HomePageLocators.CLOSE_MODAL_NEW_ORDER_BUTTON)