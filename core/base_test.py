import pytest
from core.webdriver_factory import WebDriverFactory

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        browser = "chrome"  # could be dynamic from config
        self.driver = WebDriverFactory().get_driver_instance(browser)
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()
