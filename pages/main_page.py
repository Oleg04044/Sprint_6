from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    def click_order_button(self, position='top'):
        if position == 'top':
            self.click(MainPageLocators.ORDER_TOP_BUTTON)
        elif position == 'bottom':
            self.click(MainPageLocators.ORDER_BOTTOM_BUTTON)
