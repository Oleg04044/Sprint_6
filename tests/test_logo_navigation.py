import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.logo_page import LogoPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

def test_scooter_logo_navigates_to_main(driver):
    page = LogoPage(driver)
    driver.execute_script("window.scrollTo(0, 0);")
    page.click_scooter_logo()
    assert "scooter" in driver.current_url.lower()

def test_yandex_logo_opens_dzen(driver):
    page = LogoPage(driver)
    driver.execute_script("window.scrollTo(0, 0);")

    main_window = driver.current_window_handle
    page.click_yandex_logo()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    new_window = [w for w in driver.window_handles if w != main_window][0]
    driver.switch_to.window(new_window)

    WebDriverWait(driver, 10).until(lambda d: "dzen" in d.current_url or "yandex" in d.current_url)
    assert "dzen" in driver.current_url or "yandex" in driver.current_url
