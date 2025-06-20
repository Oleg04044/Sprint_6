from selenium.webdriver.common.by import By


class MainPageLocators:
    # Верхняя кнопка «Заказать»
    ORDER_TOP_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")

    # Нижняя кнопка «Заказать»
    ORDER_BOTTOM_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Home_FinishButton') or contains(@class,'Home_ThirdPart')]//button[text()='Заказать']"
    )


class OrderPageLocators:
    # Первая форма заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")

    @staticmethod
    def METRO_OPTION(metro):
        return (By.XPATH, f"//div[@class='select-search__select']//button[contains(.,'{metro}')]")

    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PAGE_HEADER = (By.XPATH, "//div[contains(@class,'Order_Header')]")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")

    @staticmethod
    def RENT_OPTION(duration):
        return (By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{duration}']")

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_POPUP = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

class LogoPageLocators:
    SCOOTER_LOGO = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI")
