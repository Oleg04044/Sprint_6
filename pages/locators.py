from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_TOP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[@class='Button_Button__ra12g'])[last()]")

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COLOR_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal__')]//button[text()='Да']")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    @staticmethod
    def rent_option(duration):
        return (By.XPATH, f"//div[@class='Dropdown-menu']//div[text()='{duration}']")

    @staticmethod
    def station_option(name):
        return (By.XPATH, f"//button[contains(@class, 'select-search__option')]//div[text()='{name}']")
