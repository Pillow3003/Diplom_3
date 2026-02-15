import allure
import urls
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.home_page import HomePage

class TestAccountPage:
    """
    Тесты для проверки функционала аккаунта пользователя,
    включая переходы, историю заказов и выход из аккаунта.
    """

    @allure.title('Проверяем переход по кнопке "Личный кабинет" в аккаунт пользователя')
    def test_pass_into_account(self, driver, client):
        """
        Проверяет, что при клике на кнопку "Личный кабинет" происходит переход в личный кабинет пользователя,
        а имя пользователя отображается корректно.

        Шаги:
        - Открыть страницу логина.
        - Ввести данные пользователя (почта и пароль).
        - Дождаться исчезновения оверлея.
        - Нажать кнопку "Личный кабинет".
        - Проверить, что имя в поле совпадает с переданным в клиента.

        Ожидаемый результат:
        - Имя пользователя отображается правильно.
        """
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.LOGIN_PAGE)
        home_page.wait_disappear_overlay_scroll()

        login_page.input_user_data(client['email'], client['password'])
        home_page.wait_disappear_overlay_scroll()

        home_page.click_account_cabinet_button()
        user_name = account_page.get_text_name_field()

        assert user_name == client['name'], f"Ожидалось имя '{client['name']}', получили '{user_name}'"

    @allure.title('Проверяем переход в историю заказов пользователя')
    def test_pass_into_order_history(self, driver, login_user):
        """
        Проверяет переход в раздел истории заказов пользователя.

        Шаги:
        - Открыть главную страницу.
        - Дождаться исчезновения всех оверлеев.
        - Открыть личный кабинет.
        - Перейти в раздел "История заказов".
        - Проверить URL страницы.

        Ожидаемый результат:
        - URL совпадает с URL страницы истории заказов.
        """
        home_page = HomePage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.BASE_URL)

        home_page.wait_disappear_overlay_modal()
        home_page.click_account_cabinet_button()
        account_page.pass_into_order_history()

        home_page.wait_disappear_overlay_modal()

        assert account_page.get_url_page() == urls.ORDER_HISTORY, \
            f"Ожидался URL {urls.ORDER_HISTORY}, получен {account_page.get_url_page()}"

    @allure.title('Проверяем выход из аккаунта')
    def test_logout(self, driver, login_user):
        """
        Проверяет, что пользователь может выйти из аккаунта.

        Шаги:
        - Открыть главную страницу.
        - Открыть личный кабинет.
        - Нажать кнопку выхода.
        - Дождаться загрузки страницы входа.

        Ожидаемый результат:
        - URL страницы совпадает с URL страницы входа.
        """
        home_page = HomePage(driver)
        account_page = AccountPage(driver)

        driver.get(urls.BASE_URL)
        home_page.click_account_cabinet_button()
        account_page.logout_exit_button()
        account_page.wait_load_login_page()

        assert account_page.get_url_page() == urls.LOGIN_PAGE, \
            f"Ожидался URL {urls.LOGIN_PAGE}, получен {account_page.get_url_page()}"