from selenium.webdriver.common.by import By

class FeedPageLocators:

    # Номер заказа в ленте — заготовка, в которую нужно подставить id искомого заказа
    id_order_card_in_feed_with_substitutions = (By.XPATH, './/*[text()="{order_id}"]')
    
    # Номер заказа в карточке заказа
    ORDER_CARD_ID = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')
    # всплывающее окно деталей заказа в ленте заказов
    MODAL_WINDOW_HEAD = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")

    # заказы в списке заказов "Готовы:"
    ORDERS_READY = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderList")]/li')
    # номер заказа в списке заказов "В работе:"
    ORDER_IN_PROCESS = (By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady')]/li")
    # текст "Все текущие заказы готовы!" под заголовком "В работе:"
    NO_ORDERS_IN_PROCESS = (By.XPATH, ".//li[text()='Все текущие заказы готовы!']")

    # счетчик заказов "Выполнено за все время:"
    ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    # счетчик заказов "Выполнено за сегодня:"
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
