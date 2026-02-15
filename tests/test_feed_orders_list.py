import urls
from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
import allure
from selenium.webdriver.remote.webdriver import WebDriver


class TestOrderFeed:
    """
    Набор тестов для проверки создания, отображения и подсчёта заказов в приложении.
    """

    @allure.title('Отображение созданного заказа "В работе"')
    def test_new_order_in_process_orders_list(self, driver: WebDriver, login_user):
        """
        Проверяет, что созданный заказ появляется в списке заказов со статусом "В работе".
        
        Шаги:
        - Открыть главную страницу.
        - Создать заказ с выбранным булочным ингредиентом.
        - Получить номер созданного заказа.
        - Перейти в ленту заказов.
        - Проверить, что заказ с этим номером отображается как "В работе".
        """
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        login_page.click_constructor_button()
        home_page.wait_load_home_page()

        ingredient = home_page.select_bun_ingredient()
        home_page.add_basket_ingredient(ingredient)
        home_page.click_order_button()
        home_page.wait_order_created()
        new_order = home_page.get_order_number()
        home_page.wait_disappear_overlay_scroll()
        home_page.close_order_modal_window()
        home_page.wait_disappear_overlay_scroll()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        order_in_work = feed_page.get_orders_in_process()

        assert int(new_order) == int(order_in_work), \
            f"Созданный заказ #{new_order} отсутствует в списке заказов 'В работе' (найден заказ #{order_in_work})"

    @allure.title('Проверяем отображение в ленте заказов заказа пользователя из истории его заказов')
    def test_user_order_in_feed(self, driver: WebDriver, login_user):
        """
        Проверяет, что заказ пользователя из истории заказов отображается в общем списке заказов.
        
        Шаги:
        - Открыть главную страницу.
        - Создать заказ.
        - Перейти в кабинет пользователя.
        - Получить номер последнего заказа из истории.
        - Перейти в ленту заказов.
        - Проверить, что заказ отображается в ленте.
        """
        home_page = HomePage(driver)
        feed_page = FeedPage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()

        selected_ingredient = home_page.select_bun_ingredient()
        home_page.add_basket_ingredient(selected_ingredient)
        home_page.wait_disappear_overlay_scroll()
        home_page.click_order_button()
        home_page.wait_order_created()
        home_page.close_order_modal_window()

        home_page.click_account_cabinet_button()        
        account_page.pass_into_order_history()
        user_order_history = account_page.get_user_order()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        user_order_feed = feed_page.get_order()

        assert user_order_history == user_order_feed, \
            f"Заказ из истории пользователя ({user_order_history}) не совпадает с заказом в ленте ({user_order_feed})"

    @allure.title('Увеличение счетчика заказов за все время')
    def test_increasing_counter_orders_all_time(self, driver: WebDriver, login_user):
        """
        Проверяет, что после создания заказа общий счетчик заказов увеличивается на 1.
        
        Шаги:
        - Перейти в ленту заказов и получить текущий счетчик заказов за все время.
        - Создать новый заказ.
        - Снова перейти в ленту заказов.
        - Проверить, что счетчик увеличился на 1.
        """
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.wait_disappear_overlay_scroll()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()

        count_before = feed_page.get_count_orders_all_time()

        login_page.click_constructor_button()
        home_page.wait_load_home_page()

        ingredient = home_page.select_bun_ingredient()
        home_page.add_basket_ingredient(ingredient)
        home_page.click_order_button()
        home_page.wait_order_created()
        home_page.close_order_modal_window()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()

        count_after = feed_page.get_count_orders_all_time()

        assert count_after == count_before + 1, \
            f"Счетчик заказов за все время не увеличился после создания заказа. Было {count_before}, стало {count_after}"

    @allure.title('Проверяем открытие окна с инфо о заказе в ленте заказов')
    def test_open_order_modal_window(self, driver: WebDriver):
        """
        Проверяет, что модальное окно с информацией о заказе открывается при клике по первому заказу в ленте.
        """
        feed_page = FeedPage(driver)

        driver.get(urls.FEED_ORDERS_LIST_PAGE)
        feed_page.wait_load_feed_page()

        feed_page.click_first_order_feed()
        modal_opened = feed_page.get_order_modal_window()

        assert modal_opened, "Модальное окно с информацией о заказе не открылось"

    @allure.title('Увеличение счетчика заказов за день')
    def test_increasing_counter_orders_today(self, driver: WebDriver, login_user):
        """
        Проверяет, что после создания заказа счетчик заказов за текущий день увеличивается на 1.
        
        Шаги:
        - Получить текущий счетчик заказов за день.
        - Создать новый заказ.
        - Обновить счетчик заказов за день.
        - Проверить, что счетчик увеличился на 1.
        """
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        driver.get(urls.BASE_URL)
        home_page.wait_load_home_page()
        home_page.wait_disappear_overlay_scroll()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        count_before = feed_page.get_count_orders_today()

        login_page.click_constructor_button()
        home_page.wait_load_home_page()

        ingredient = home_page.select_bun_ingredient()
        home_page.add_basket_ingredient(ingredient)

        home_page.click_order_button()
        home_page.wait_order_created()
        home_page.close_order_modal_window()

        home_page.click_feed_button()
        feed_page.wait_load_feed_page()
        count_after = feed_page.get_count_orders_today()

        assert count_after == count_before + 1, \
            f"Счетчик заказов за день не увеличился после создания заказа. Было {count_before}, стало {count_after}"