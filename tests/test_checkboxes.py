import pytest
from pages.elements_page import ElementsPage
import time

@pytest.mark.usefixtures("setup")
class TestCheckboxes:
    def test_check_home_checkbox(self):
        time.sleep(2)
        self.driver.get("https://demoqa.com/checkbox")
        time.sleep(2)
        page = ElementsPage(self.driver)
        page.click_home_checkbox()
        time.sleep(2)
        result = page.get_result_text()

        assert "home" in result.lower()
