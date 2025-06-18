import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.epic("Оформление заказа")
@allure.feature("Флоу заказа через кнопки")
class TestOrderButton:

    @pytest.mark.parametrize('button_position', ['upper', 'lower'])
    @pytest.mark.parametrize('name, surname, address, phone, date, rent_duration, comment', [
        ("Анна", "Иванова", "Москва, ул. Тестовая, 1", "89991234567", "12.06.2025", "двое суток", "Позвоните за час"),
        ("Дмитрий", "Смирнов", "Питер, пр. Ленина, 10", "89001112233", "13.06.2025", "трое суток", "Без звонка")
    ])
    def test_success_order_flow(self, driver, name, surname, address, phone, date, rent_duration, comment, button_position):
        main = MainPage(driver)
        order = OrderPage(driver)

        with allure.step(f"Принять cookies и нажать кнопку Заказать ({button_position})"):
            main.accept_cookies_if_present()
            if button_position == 'upper':
                main.click_upper_order_button()
            else:
                main.click_lower_order_button()

        with allure.step("Заполнить первую форму заказа"):
            order.fill_first_form(name, surname, address, phone)

        with allure.step("Заполнить вторую форму и отправить заказ"):
            order.fill_second_form_and_submit(date, rent_duration, comment)

        with allure.step("Проверить, что заказ оформлен успешно"):
            order.wait_for_success_popup()
