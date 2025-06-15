from pages.base_page import BasePage
from pages.locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class OrderPage(BasePage):
    def fill_first_form(self, name, surname, address, phone):
        self.enter_text(OrderPageLocators.NAME_INPUT, name)
        self.enter_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station("Комсомольская")
        self.enter_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form_and_submit(self, date, rent_duration, comment):
        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.send_keys(Keys.CONTROL + "a")
        date_input.send_keys(date)

        # Клик по нужному дню в календаре
        self.click((By.CLASS_NAME, "react-datepicker__day--012"))

        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.rent_option(rent_duration))

        self.click(OrderPageLocators.COLOR_CHECKBOX)
        self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)
        self.click(OrderPageLocators.SUBMIT_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def select_metro_station(self, name):
        self.enter_text(OrderPageLocators.METRO_INPUT, name)
        self.click(OrderPageLocators.station_option(name))

    def wait_for_success_popup_and_click_view_status(self):
        # Ожидаем появление окна с сообщением об успешном заказе
        self.find_element((By.XPATH, "//div[contains(text(),'Заказ оформлен')]"))
        self.click(OrderPageLocators.VIEW_STATUS_BUTTON)
