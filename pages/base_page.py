import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Найти элемент и кликнуть по локатору: {locator}")
    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        self.scroll_to_element(element)
        element.click()

    @allure.step("Очистить и ввести текст: '{text}' в элемент по локатору: {locator}")
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        self.scroll_to_element(element)
        element.clear()
        element.send_keys(text)

    @allure.step("Подтвердить cookies, если кнопка отображается")
    def accept_cookies_if_present(self):
        try:
            cookie_button = self.driver.find_element(By.ID, "rcc-confirm-button")
            self.scroll_to_element(cookie_button)
            cookie_button.click()
        except NoSuchElementException:
            pass

    @allure.step("Выполнить JavaScript скрипт")
    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    @allure.step("Переключиться на новое окно браузера")
    def switch_to_new_window(self, main_window):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        new_window = [w for w in self.driver.window_handles if w != main_window][0]
        self.driver.switch_to.window(new_window)

    @allure.step("Ожидать, что элемент станет кликабельным: {locator}")
    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидать, что элемент станет видимым: {locator}")
    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Прокрутить элемент в центр экрана")
    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    @allure.step("Получить идентификатор текущего окна браузера")
    def get_current_window(self):
        return self.driver.current_window_handle
