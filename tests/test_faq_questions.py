import pytest
import allure
from pages.faq_page import FAQPage


@allure.epic("FAQ")
@allure.feature("Развернуть вопросы и ответы")
class TestFAQQuestions:

    @allure.title("Развернуть и проверить вопрос #{index}")
    @pytest.mark.parametrize("index", range(8))
    def test_faq_question_expands(self, driver, index):
        page = FAQPage(driver)

        with allure.step(f"Развернуть вопрос №{index}"):
            page.expand_question(index)

        with allure.step(f"Проверить, что ответ виден для вопроса №{index}"):
            assert page.is_answer_visible(index)
