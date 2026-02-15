import urls
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.login_page import LoginPage
import allure
from selenium.webdriver.remote.webdriver import WebDriver


class TestResetPassword:
    """
    Набор тестов для проверки восстановления пароля на сайте:
    переходы между страницами и взаимодействие с элементами формы.
    """

    @allure.title('Проверяем переход на страницу восстановления пароля по ссылке «Восстановить пароль»')
    def test_pass_into_forgot_password_page(self, driver: WebDriver):
        """
        Проверяет, что при нажатии на ссылку "Восстановить пароль" на странице логина
        происходит переход на страницу восстановления пароля.
        """
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        driver.get(urls.LOGIN_PAGE)
        forgot_password_page.wait_disappear_overlay_scroll()
        login_page.click_restore_password()
        forgot_password_page.wait_load_forgot_password_page()

        current_url = forgot_password_page.get_url_page()
        assert current_url == urls.FORGOT_PASSWORD_PAGE, \
            f"Ожидался URL {urls.FORGOT_PASSWORD_PAGE}, но получен {current_url}"

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить»')
    def test_open_reset_page(self, driver: WebDriver):
        """
        Проверяет, что после ввода email и нажатия кнопки "Восстановить"
        происходит переход на страницу сброса пароля.
        """
        email_for_reset = 'abracadabra@gmail.ru'
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        driver.get(urls.FORGOT_PASSWORD_PAGE)
        forgot_password_page.fill_email_field(email_for_reset)
        forgot_password_page.wait_disappear_overlay_scroll()

        forgot_password_page.click_restore_password_button()
        reset_password_page.wait_load_reset_password_page()

        current_url = forgot_password_page.get_url_page()
        assert current_url == urls.RESET_PASSWORD_PAGE, \
            f"Ожидался URL {urls.RESET_PASSWORD_PAGE}, но получен {current_url}"

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_password(self, driver: WebDriver):
        """
        Проверяет, что при клике по кнопке "показать пароль"
        поле для ввода пароля становится активным (подсвечивается).
        """
        email_for_reset = 'abracadabra@gmail.ru'
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        driver.get(urls.FORGOT_PASSWORD_PAGE)
        forgot_password_page.fill_email_field(email_for_reset)
        forgot_password_page.wait_disappear_overlay_scroll()

        forgot_password_page.click_restore_password_button()

        reset_password_page.wait_load_reset_password_page()
        forgot_password_page.wait_disappear_overlay_scroll()

        reset_password_page.click_show_password()

        password_input_class = reset_password_page.get_password_input_class_name()
        assert 'input_status_active' in password_input_class, \
            f"Ожидался класс 'input_status_active' в '{password_input_class}'"