import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.mark.parametrize("name, surname, address, phone, date, rent_duration, comment", [
    ("Анна", "Иванова", "Москва, ул. Тестовая, 1", "89991234567", "12.06.2025", "двое суток", "Позвоните за 1 час"),
    ("Дмитрий", "Смирнов", "Питер, пр. Ленина, 10", "89001112233", "13.06.2025", "трое суток", "Без звонка")
])
def test_success_order_flow(driver, name, surname, address, phone, date, rent_duration, comment):
    main = MainPage(driver)
    main.accept_cookies_if_present()
    main.click_order_button("top")

    order = OrderPage(driver)
    order.fill_first_form(name, surname, address, phone)
    order.fill_second_form_and_submit(date, rent_duration, comment)
    order.confirm_order()
    order.wait_for_success_popup_and_click_view_status()

    # Можно добавить проверку успешного подтверждения заказа
    assert "Заказ оформлен" in driver.page_source or "Хотите оформить заказ?" not in driver.page_source
