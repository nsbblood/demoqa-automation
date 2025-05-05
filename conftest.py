import pytest
from core.webdriver_factory import WebDriverFactory
from utils.logger import setup_logger

@pytest.fixture(scope="class")
def setup(request):
    browser = "chrome"  # could be dynamic later
    driver = WebDriverFactory().get_driver_instance(browser)
    driver.maximize_window()
    request.cls.driver = driver

    logger = setup_logger("TestLogger")
    request.cls.logger = logger
    yield
    driver.quit()

# Capture screenshot on failure
def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.instance.driver
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        filepath = os.path.join(screenshot_dir, f"{node.name}_failure.png")
        driver.save_screenshot(filepath)
