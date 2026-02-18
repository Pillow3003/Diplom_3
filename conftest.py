import pytest
from selenium import webdriver
import requests
from helper import RandomUserData
import urls
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    """
    Фикстура создания и закрытия веб-драйвера для разных браузеров.

    :param request: параметр для выбора браузера ('chrome' или 'firefox')
    :return: экземпляр selenium webdriver
    """
    driver = None
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def new_user():
    """
    Фикстура генерации случайных данных нового пользователя.

    :return: dict с данными пользователя (name, email, password)
    """
    user_data_generator = RandomUserData()
    user_data = user_data_generator.user_data_generation()
    return user_data


@pytest.fixture(scope='function')
def client(new_user):
    """
    Фикстура для регистрации пользователя через API и последующего удаления.

    :param new_user: данные для регистрации пользователя
    :yield: данные зарегистрированного пользователя
    """
    # Для API обычно лучше передавать json
    response = requests.post(
        urls.BASE_URL + urls.REGISTRATION_USER_ENDPOINT,
        json=new_user
    )
    response.raise_for_status()
    access_token = response.json().get('accessToken')

    yield new_user

    # Удаляем пользователя после теста
    headers = {'Authorization': access_token}
    del_response = requests.delete(urls.BASE_URL + urls.USER_DATA_ENDPOINT, headers=headers)
    del_response.raise_for_status()


@pytest.fixture(scope='function')
def login_user(driver, client):
    """
    Фикстура для авторизации пользователя на веб-странице.

    :param driver: selenium webdriver
    :param client: данные авторизованного пользователя
    """
    driver.get(urls.LOGIN_PAGE)

    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    home_page.wait_disappear_overlay_scroll()
    home_page.wait_disappear_overlay_modal()

    login_page.input_user_data(client['email'], client['password'])
    home_page.wait_load_home_page()
