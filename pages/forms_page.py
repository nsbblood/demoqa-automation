from selenium.webdriver.common.by import By
from core.base_page import BasePage

class FormsPage(BasePage):
    forms_menu = (By.XPATH, "//h5[text()='Forms']")
    practice_form = (By.ID, "item-0")

    def navigate_to_forms(self):
        self.click(*self.forms_menu)

    def open_practice_form(self):
        self.click(*self.practice_form)
