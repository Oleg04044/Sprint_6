from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FAQPage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def click_question(self, index):
        question = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.ID, f"accordion__heading-{index}"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, -100);", question)
        time.sleep(1)

        ActionChains(self.driver).move_to_element(question).click().perform()
    def is_answer_visible(self, index):
        answer_locator = (By.ID, f"accordion__panel-{index}")
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(answer_locator)
        )
