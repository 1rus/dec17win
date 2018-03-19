from exceptions import *
from config import Config
import browser
from assertions import Assertions

if 2 == 2:
    a = InvalidLocatorString('invalid locator string')

# some comments here
# another comment here
# next comment line 

c = Config()
cf = c.prepare()
def print_keys():
    for key in cf.__dict__.keys():
        print(cf.__dict__.get(key).keys())
        if 'grid' in cf.__dict__.get(key).items():
            print('grid in cf')

if 'screenshots' in cf['sframe']:
    if cf['sframe']['screenshots']:
        print("has screenshots option")

print(cf)

default_browser = cf["browser"]
print(default_browser)
browser = browser.Browser(default_browser, cf)
driver = browser.driver
verification_errors = []
assertions = Assertions(driver, verification_errors)

print('browser is dict')
print(dir(browser))

if hasattr(browser, 'config'):
    print('has attr config')

if hasattr(browser, 'proxy'):
    print('browser hasattr proxy')
    proxy = browser.proxy
    print('closing proxy')
    proxy.close()

if hasattr(browser, "driver"):
    print('browser hasattr driver')
    driver.quit()

