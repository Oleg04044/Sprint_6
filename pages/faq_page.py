from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class FAQPage(BasePage):

    def expand_question(self, index):
        question_locator = (By.ID, f"accordion__heading-{index}")
        question = self.wait_for_element_clickable(question_locator)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        self.execute_script("arguments[0].click();", question)

    def is_answer_visible(self, index):
        answer_locator = (By.ID, f"accordion__panel-{index}")
        answer = self.wait_for_element_visible(answer_locator)
        return answer.is_displayed()
