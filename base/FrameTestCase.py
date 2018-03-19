import browser
import os.path
from base.BaseTestCase import BaseTestCase
from config import Config
from assertions import Assertions


class FrameTest(BaseTestCase):

    def setup_method(self, method):
        self.current_method = method.__name__
        c = Config()
        self.config = c.prepare()
        browser_conf = self.config["browser"]
        self.browser = browser.Browser(browser_conf, self.config)
        self.driver = self.browser.driver
        self.verification_errors = []
        self.assertions = Assertions(self.driver, self.verification_errors)

        if hasattr(self.browser, "proxy"):
            self.proxy = self.browser.proxy

        self._screenshot_number = 1

    def teardown_method(self):
        if hasattr(self, "driver"):
            print("has attr driver")
            self.driver.quit()

        if hasattr(self.browser, "proxy"):
            print("has attr proxy")
            self.proxy.close()

    def take_numbered_screenshot(self):
        if "screenshots" in self.config['sframe']\
            and self.config.getboolean("sframe", "screenshots"):
            output_dir = self.prepare_screenshots_dir()
            self.driver.get_screenshot_as_file(os.path.join(output_dir, str(self._screenshot_number).zfill(3)+".png"))
            self._screenshot_number = self._screenshot_number+1

    def take_named_screenshot(self, name):
        method_dir = self.prepare_screenshots_dir()

        image_path = os.path.join(method_dir, str(name) + ".png")
        self.driver.get_screenshot_as_file(image_path)
