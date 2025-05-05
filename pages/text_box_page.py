from selenium.webdriver.common.by import By
from core.base_page import BasePage

class TextBoxPage(BasePage):
    full_name = (By.ID, "userName")
    email = (By.ID, "userEmail")
    current_address = (By.ID, "currentAddress")
    permanent_address = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")
    output_name = (By.ID, "name")
    output_email = (By.ID, "email")

    def fill_form(self, name, email, current, permanent):
        self.type(*self.full_name, value=name)
        self.type(*self.email, value=email)
        self.type(*self.current_address, value=current)
        self.type(*self.permanent_address, value=permanent)

    def submit_form(self):
        self.scroll_to(*self.submit_button)
        self.click(*self.submit_button)

    def get_output_name(self):
        return self.get_text(*self.output_name)

    def get_output_email(self):
        return self.get_text(*self.output_email)