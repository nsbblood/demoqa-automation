from selenium.webdriver.common.by import By
from core.base_page import BasePage

class ElementsPage(BasePage):
    check_box_btn = (By.ID, "item-1")
    home_checkbox = (By.CLASS_NAME, "rct-checkbox")
    result_text = (By.ID, "result")

    def go_to_check_box(self):
        self.click(*self.check_box_btn)

    def click_home_checkbox(self):
        self.click(*self.home_checkbox)

    def get_result_text(self):
        return self.get_text(*self.result_text)
