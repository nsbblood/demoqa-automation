import pytest
from pages.text_box_page import TextBoxPage
import time

@pytest.mark.usefixtures("setup")
class TestTextBox:
    def test_fill_text_box_form(self):
        time.sleep(2)
        self.driver.get("https://demoqa.com/text-box")
        time.sleep(2)
        page = TextBoxPage(self.driver)
        time.sleep(2)
        page.fill_form("Enes Arikan", "enes@test.com", "İstanbul", "Ankara")
        time.sleep(2)
        page.submit_form()

        assert "Enes Arikan" in page.get_output_name()
        assert "enes@test.com" in page.get_output_email()
