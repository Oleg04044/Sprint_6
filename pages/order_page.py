from pages.base_page import BasePage
from pages.locators import OrderPageLocators as Locators


class OrderPage(BasePage):

    def fill_first_form(self, name, surname, address, phone):
        self.wait_for_element_clickable(Locators.NAME_INPUT).send_keys(name)
        self.find_element(Locators.SURNAME_INPUT).send_keys(surname)
        self.find_element(Locators.ADDRESS_INPUT).send_keys(address)

        self.click(Locators.METRO_FIELD)
        self.wait_for_element_clickable(Locators.METRO_OPTION("Сокольники")).click()

        self.find_element(Locators.PHONE_INPUT).send_keys(phone)
        self.click(Locators.NEXT_BUTTON)

    def fill_second_form_and_submit(self, date, rent_duration, comment):
        date_input = self.find_element(Locators.DATE_INPUT)
        self.scroll_to_element(date_input)
        date_input.send_keys(date)

        page_header = self.find_element(Locators.PAGE_HEADER)
        self.scroll_to_element(page_header)
        page_header.click()

        rent_dropdown = self.find_element(Locators.RENT_DROPDOWN)
        self.scroll_to_element(rent_dropdown)
        rent_dropdown.click()

        rent_option = self.find_element(Locators.RENT_OPTION(rent_duration))
        self.scroll_to_element(rent_option)
        rent_option.click()

        comment_input = self.find_element(Locators.COMMENT_INPUT)
        self.scroll_to_element(comment_input)
        comment_input.send_keys(comment)

        order_button = self.find_element(Locators.ORDER_BUTTON)
        self.scroll_to_element(order_button)
        order_button.click()

        yes_button = self.find_element(Locators.YES_BUTTON)
        self.scroll_to_element(yes_button)
        yes_button.click()

    def wait_for_success_popup(self):
        self.wait_for_element_visible(Locators.SUCCESS_POPUP)
