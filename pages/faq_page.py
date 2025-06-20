from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FAQPage(BasePage):
    def click_question_by_text(self, question_text):
        locator = (By.XPATH, f"//div[contains(text(), '{question_text}')]")
        question = self.wait_for_element_visible(locator)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)

        self.driver.execute_script("arguments[0].click();", question)

    def get_answer_text_by_question(self, question_text):
        answer_locator = (By.XPATH, f"//div[contains(text(), '{question_text}')]/parent::div/following-sibling::div")
        answer = self.wait_for_element_visible(answer_locator)
        return answer.text
