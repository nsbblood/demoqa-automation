from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def click(self, by, locator):
        self.find(by, locator).click()

    def type(self, by, locator, value):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, by, locator):
        return self.find(by, locator).text

    def is_visible(self, by, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except:
            return False

    def scroll_to(self, by, locator):
        element = self.find(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
