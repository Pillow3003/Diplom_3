from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from locators.home_page_locators import HomePageLocators
import allure

class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы для взаимодействия с элементами страницы.
    """

    def __init__(self, driver):
        """
        Инициализация страницы.
        :param driver: WebDriver — драйвер браузера.
        """
        self.driver = driver

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        """
        Кликает по элементу, указанному локатором.
        :param locator: кортеж локатора (By.X, значение)
        """
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Заполняем поле данными')
    def send_data_into_field(self, locator, text):
        """
        Вводит текст в поле, указанное локатором.
        :param locator: кортеж локатора (By.X, значение)
        :param text: строка с текстом для ввода
        """
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем элемент страницы')
    def wait_and_find_element(self, locator):
        """
        Ожидает видимость элемента и возвращает его.
        :param locator: кортеж локатора (By.X, значение)
        :return: веб-элемент, найденный по локатору
        """
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверяем отображение элемента на странице')
    def check_element_visibility(self, locator):
        """
        Проверяет наличие элемента на странице.
        :param locator: кортеж локатора (By.X, значение)
        :return: True, если элемент найден, иначе False
        """
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    @allure.step('Ожидание удаления элемента со страницы')
    def wait_element_disappearing(self, locator):
        """
        Ожидает исчезновения элемента со страницы.
        :param locator: кортеж локатора (By.X, значение)
        """
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    @allure.step('Получаем URL страницы')
    def get_url_page(self):
        """
        Возвращает текущий URL страницы.
        :return: строка с URL
        """
        return self.driver.current_url

    @allure.step('Ожидание смены URL страницы')
    def wait_for_url(self, url):
        """
        Ожидает, что URL страницы изменится на указанный.
        :param url: строка с ожидаемым URL
        """
        WebDriverWait(self.driver, 20).until(EC.url_to_be(url))

    @allure.step('Переносим drag&drop элемент с одного места на другое')
    def drag_and_drop(self, source, target):
        """
        Выполняет drag-and-drop элемента source на элемент target.
        :param source: локатор исходного элемента (кортеж)
        :param target: локатор целевого элемента (кортеж)
        """
        action_chains = ActionChains(self.driver)
        drag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(target))
        action_chains.drag_and_drop(drag, drop).perform()

    @allure.step('Ждем исчезновения оверлея прокрутки')
    def wait_disappear_overlay_scroll(self):
        """
        Ожидает исчезновения оверлейного элемента прокрутки.
        """
        self.wait_element_disappearing(HomePageLocators.OVERLAY_SCROLL)

    @allure.step('Ждем исчезновения оверлея модального окна')
    def wait_disappear_overlay_modal(self):
        """
        Ожидает исчезновения оверлейного элемента модального окна.
        """
        self.wait_element_disappearing(HomePageLocators.OVERLAY_MODAL)