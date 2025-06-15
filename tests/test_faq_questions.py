import pytest
from selenium import webdriver
from pages.faq_page import FAQPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.mark.parametrize("index", list(range(8)))  # 8 вопросов
def test_faq_question_expands(driver, index):
    faq = FAQPage(driver)

    driver.execute_script("arguments[0].scrollIntoView();",
                          driver.find_element("id", f"accordion__heading-{index}"))

    faq.click_question(index)
    assert faq.is_answer_visible(index), f"Ответ на вопрос {index} не отобразился"
