from objects.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from objects import attribute as get_attr
from selenium.common.exceptions import StaleElementReferenceException
from webelement import WebElement


locators = {
            'menu_pim': 'id=menu_pim_viewPimModule',
            'search_name': 'id=empsearch_employee_name_empName',
            'searchbtn': 'id=searchBtn',
            'search_css': 'css=.input.empsearch_employee_name_empName',
            'loaded': 'class=panel_resizable panel-preview',
            'search_id': 'id=empsearch_id',
            'result_table': 'css=.table.hover',
            'footer': 'id=footer'

}

base_url = 'http://hrm.seleniumminutes.com'
page_url = '/symfony/web/index.php/pim/viewEmployeeList'


class PIM_page(BasePage):

    def open(self):
        self.driver.get(base_url+page_url)
        return self.wait_for_available(locators['footer'])

    def find_employee_by_name2(self, _name):
        e = (locators['search_name'])
        value = get_attr.Attribute(e, 'class')
        value = get_attr.Attribute(e, 'name')
        value = get_attr.Attribute(e, 'type')

        print(value)
        #self.wait_for_value_change_in()
        pass

    def find_employee_by_name(self, _name):
        self.wait_for_element_change(locators['search_name'], 'loading')
        e = self.driver.find_element_by_locator(locators['search_name'])
        e.click()
        e.clear()
        e.send_keys(_name + Keys.SPACE + Keys.ESCAPE)
        e = self.driver.find_element_by_locator(locators['searchbtn'])
        e.click()
        ee = [[]]
        self.driver.find_element_by_locator(locators['result_table'])
        num_of_columns = len(self.driver.find_elements_by_xpath("//th[@class='header']"))
        elements = self.driver.find_elements_by_xpath("//td[@class='left']")
        num_of_emp = 0
        iterator = 1
        for e in elements:
            if iterator != num_of_columns:
                ee[num_of_emp].append(e.text)
                iterator = iterator + 1
            elif iterator*(num_of_emp+1) == len(elements):
                break
            else:
                ee.append([])
                iterator = 1
                num_of_emp = num_of_emp + 1
        return [ee, num_of_emp]

