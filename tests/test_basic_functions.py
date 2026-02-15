import urls
from pages.home_page import HomePage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
import allure

class TestBasicFunctions:
    """
    Набор базовых тестов для проверки основных функций переходов, модальных окон и оформления заказа.
    """

    @allure.title('Проверяем переход на главную страницу по кнопке "Конструктор"')
    def test_pass_into_constructor(self, driver):
        """
        Проверяет, что при клике на кнопку "Конструктор" с страницы логина происходит переход на главную страницу.

        Шаги:
        - Открыть страницу логина.
        - Нажать кнопку "Конструктор".
        - Дождаться загрузки главной страницы.
        - Проверить URL страницы.

        Ожидаемый результат:
        - URL главной страницы соответствует базовому URL.
        """
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        driver.get(urls.LOGIN_PAGE)
        home_page.wait_disappear_overlay_scroll()

        login_page.click_constructor_button()
        home_page.wait_load_home_page()

        assert home_page.get_url_page() == urls.BASE_URL, "Не произошёл переход на главную страницу по кнопке 'Конструктор'"

    @allure.title('Проверяем переход в ленту заказов')
    def test_pass_into_feed_orders_list(self, driver):
        """
        Проверяет переход на страницу ленты заказов при нажатии на кнопку "Лента заказов".

        Шаги:
        - Открыть главную страницу.
        - Нажать кнопку "Лента заказов".
        - Дождаться загрузки страницы ленты заказов.
        - Проверить URL страницы.

        Ожидаемый результат:
        - URL страницы соответствует адресу ленты заказов.
        """
        home_page = HomePage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()

        assert feed_page.get_url_page() == urls.FEED_ORDERS_LIST_PAGE, "Переход в ленту заказов не произошёл"

    @allure.title('Проверяем открытие модального окна с информацией об ингредиенте')
    def test_open_ingredient_modal_window(self, driver):
        """
        Проверяет, что при нажатии на картинку ингредиента открывается модальное окно с информацией.

        Шаги:
        - Открыть главную страницу.
        - Кликнуть по изображению ингредиента.
        - Проверить открытие модального окна.

        Ожидаемый результат:
        - Модальное окно с информацией об ингредиенте появляется.
        """
        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        home_page.click_ingredient()

        assert home_page.get_ingredient_modal_window(), "Модальное окно с информацией об ингредиенте не открылось"

    @allure.title('Проверяем закрытие модального окна информации об ингредиенте')
    def test_close_ingredient_modal(self, driver):
        """
        Проверяет, что при нажатии на крестик модальное окно информации об ингредиенте закрывается.

        Шаги:
        - Открыть главную страницу.
        - Открыть модальное окно ингредиента.
        - Нажать на крестик закрытия окна.
        - Проверить, что окно закрыто.

        Ожидаемый результат:
        - Модальное окно закрыто после нажатия крестика.
        """
        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.click_ingredient()

        # Проверяем, что окно открылось
        assert home_page.get_ingredient_modal_window(), "Модальное окно не открылось"

        home_page.close_ingredient_modal_window()

        assert not home_page.check_ingredient_modal_window(), "Модальное окно не закрылось после нажатия крестика"

    @allure.title('Проверяем увеличение счётчика на 2 при добавлении булочной булки')
    def test_increasing_bun_ingredient_counter(self, driver):
        """
        Проверяет, что добавление булки увеличивает счётчик ингредиента на 2.

        Шаги:
        - Открыть главную страницу.
        - Выбрать булку.
        - Добавить булку в заказ.
        - Проверить значение счётчика для булки.

        Ожидаемый результат:
        - Счётчик булки увеличивается ровно на 2.
        """
        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        selected_ingredient = home_page.select_bun_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)

        assert home_page.get_actual_counter(selected_ingredient) == 2, \
            "Счётчик булки не увеличился на 2 после добавления"

    @allure.title('Проверяем увеличение счётчика на 1 при добавлении не булочной ингридиента')
    def test_increasing_non_bun_ingredient_counter(self, driver):
        """
        Проверяет, что добавление ингредиента, не являющегося булкой, увеличивает счетчик на 1.

        Шаги:
        - Открыть главную страницу.
        - Выбрать не булочный ингредиент.
        - Добавить его в заказ.
        - Проверить значение счётчика.

        Ожидаемый результат:
        - Счётчик выбранного ингредиента увеличивается на 1.
        """
        home_page = HomePage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        selected_ingredient = home_page.select_non_bun_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)

        assert home_page.get_actual_counter(selected_ingredient) == 1, \
            "Счётчик не булочного ингредиента не увеличился на 1 после добавления"

    @allure.title('Проверяем оформление заказа авторизованным пользователем')
    def test_make_order_user_authorized(self, driver, login_user):
        """
        Проверяет успешное оформление заказа авторизованным пользователем.

        Шаги:
        - Открыть страницу логина (пользователь уже авторизован).
        - Добавить булку в заказ.
        - Нажать кнопку оформления заказа.
        - Проверить появление модального окна с номером заказа.

        Ожидаемый результат:
        - Модальное окно с номером заказа появляется.
        """
        home_page = HomePage(driver)

        driver.get(urls.LOGIN_PAGE)
        home_page.wait_load_home_page()

        selected_ingredient = home_page.select_bun_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)
        home_page.click_order_button()

        assert home_page.get_order_modal_window(), "Модальное окно с номером заказа не открылось после оформления заказа"