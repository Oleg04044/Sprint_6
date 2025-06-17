from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import LogoPageLocators
from pages.base_page import BasePage  # Не забудь импортировать BasePage!
import allure

class LogoPage(BasePage):

    @allure.step("Прокрутить страницу наверх")
    def scroll_to_top(self):
        self.execute_script("window.scrollTo(0, 0);")

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click(LogoPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(LogoPageLocators.YANDEX_LOGO)

    @allure.step("Проверить, что пользователь на главной странице Самоката")
    def is_on_main_page(self):
        return "scooter" in self.driver.current_url.lower()

    @allure.step("Проверить, что пользователь перешел в Дзен")
    def is_on_dzen_page(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: "dzen" in d.current_url
        )
        return "dzen" in self.driver.current_url

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self, main_window):
        windows = self.driver.window_handles
        for window in windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break
