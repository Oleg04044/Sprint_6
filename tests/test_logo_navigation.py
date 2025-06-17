import allure
from pages.logo_page import LogoPage

@allure.epic("Логотипы")
@allure.feature("Навигация по логотипам")
def test_scooter_logo_navigates_to_main(driver):
    page = LogoPage(driver)

    with allure.step("Прокрутить страницу наверх"):
        page.scroll_to_top()

    with allure.step("Кликнуть на логотип Самоката"):
        page.click_scooter_logo()

    with allure.step("Проверить, что открыта главная страница Самоката"):
        assert page.is_on_main_page()


@allure.epic("Логотипы")
@allure.feature("Навигация по логотипам")
def test_yandex_logo_opens_dzen(driver):
    page = LogoPage(driver)

    with allure.step("Прокрутить страницу наверх"):
        page.scroll_to_top()

    with allure.step("Кликнуть на логотип Яндекса"):
        main_window = page.get_current_window()
        page.click_yandex_logo()
        page.switch_to_new_window(main_window)

    with allure.step("Проверить, что открыт Дзен"):
        assert page.is_on_dzen_page()
