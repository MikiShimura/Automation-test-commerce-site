import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FfOptions
import os
import pytest_html

@pytest.fixture(scope="class") 
def init_driver(request):
    supported_browser = ["chrome", "ch", "headlesschrome", "firefox", "ff", "headlessfirefox"]

    browser = os.environ.get("BROWSER", None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")
    
    browser = browser.lower()
    if browser not in (supported_browser):
        raise Exception(f"Provided browser: '{browser}' is not one of the supported."
                        f"Supported are {supported_browser}.")
    
    if browser in ("chrome", "ch"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser in ("firefox", "ff"):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser in ("headlesschrome"):
        chrome_options = ChOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser in ("headlessfirefox"):
        firefox_options = FfOptions()
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    
    request.cls.driver = driver
    # set class variable, driver here is browser
    yield
    # driver.quit()

# Report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    # only add additional images on failure
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontednd_test = True if "init_driver" in item.fixturenames else False
            if is_frontednd_test :
                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")
                screen_shot_path = os.path.join(results_dir, item.name + ".png")
                driver_fixture = item.funcargs["request"]
                driver_fixture.cls.driver.save_screenshot(screen_shot_path)
                # import pdb; pdb.set_trace()
                extras.append(pytest_html.extras.image(screen_shot_path))
        report.extras = extras