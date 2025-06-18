import allure
import pytest
from pages.faq_page import FAQPage
from data import FAQ_QUESTIONS  # ✅ правильно!

@allure.epic("FAQ")
@allure.feature("Проверка вопросов и ответов")
class TestFAQQuestions:

    @pytest.mark.parametrize("question, expected_answer", FAQ_QUESTIONS)
    def test_faq_answer(self, driver, question, expected_answer):
        page = FAQPage(driver)

        with allure.step(f"Нажать на вопрос: '{question}'"):
            page.click_question_by_text(question)

        with allure.step(f"Проверить, что ответ совпадает для вопроса: '{question}'"):
            actual_text = page.get_answer_text_by_question(question)
            assert actual_text == expected_answer, f"Ожидалось: '{expected_answer}', получено: '{actual_text}'"
