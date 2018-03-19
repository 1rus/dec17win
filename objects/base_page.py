import os
import os.path
import time
from exceptions import WaitForElementTimeout, WaitForTextTimeout
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

class BasePage (object):

    timeout_seconds = 30
    sleep_interval = .25
    short_sleep = .002

    def __init__(self, driver):
        self.driver = driver

    def sleep(self, seconds=None):
        if seconds:
            time.sleep(seconds)
        else:
            time.sleep(self.sleep_interval)

    def find_element_by_locator(self, locator):
        print('finding locator: ', str(locator.split(':')))
        return self.driver.find_element_by_locator(locator)

    def find_elements_by_locator(self, locator):
        return self.driver.find_elements_by_locator(locator)

    def wait_for_available(self, locator):
        for i in range(self.timeout_seconds):
            print('waiting element {0} with interval {1} : i={2}'.format(locator, self.sleep_interval, str(i)).split(':'))
            try:
                if self.driver.is_element_available(locator):
                    break
            except:
                pass
            self.sleep()
        else:
            raise WaitForElementTimeout('%s availability timed out' % locator)

    def wait_for_element_change(self, element, text):
        for i in range(self.timeout_seconds):
            print('wait with interval {0} : i={1}'.format(self.short_sleep, str(i)).split(':'))
            try:
                if text not in element.__get__(self):
                    print('dynamic element loaded, proceeding ', int(i))
                    break
            except:
                pass
            finally:
                self.sleep(self.short_sleep)
        else:
            raise Exception('change value exception')

    def title(self):
        return self.driver.title

    def logout(self):
        pass

