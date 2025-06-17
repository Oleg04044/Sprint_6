import allure
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from pages.locators import MainPageLocators as Locators


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.step("Принять cookies, если кнопка видна")
    def accept_cookies_if_present(self):
        try:
            cookie_button = self.find_element(("id", "rcc-confirm-button"))
            self.scroll_to_element(cookie_button)
            cookie_button.click()
        except NoSuchElementException:
            pass

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_upper_order_button(self):
        self.click(Locators.ORDER_TOP_BUTTON)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_lower_order_button(self):
        self.click(Locators.ORDER_BOTTOM_BUTTON)

    @allure.step("Нажать кнопку 'Заказать' ({position})")
    def click_order_button(self, position):
        self.accept_cookies_if_present()
        locator = Locators.ORDER_TOP_BUTTON if position == 'top' else Locators.ORDER_BOTTOM_BUTTON
        self.click(locator)
