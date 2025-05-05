from selenium import webdriver

class WebDriverFactory:
    def get_driver_instance(self, browser):
        if browser == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        else:
            raise Exception(f"Unsupported browser: {browser}")
