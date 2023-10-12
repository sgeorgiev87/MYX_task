# -*- coding: utf-8 -*-

# START IMPORTS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
import traceback
# END IMPORTS

"""
A Base Page to be inherited by all page objects
"""


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def find_element(self, *selector):
        return self.driver.find_element(*selector)

    def find_elements(self, *selector):
        return self.driver.find_elements(*selector)

    def presence_of_element(self, selector):
        return self.wait.until(ec.presence_of_element_located(selector))

    def presence_of_elements(self, selector):
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def visibility_of_element(self, selector):
        return self.wait.until(ec.visibility_of_element_located(selector))

    def visibility_of_elements(self, selector):
        return self.wait.until(ec.visibility_of_any_elements_located(selector))

    def clickable_element(self, selector):
        return self.wait.until(ec.element_to_be_clickable(selector))

    def is_alert_present(self):
        return self.wait.until(ec.alert_is_present)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def get_alert_text(self):
        return self.driver.switch_to.alert.text

    def click_on_element(self, element_name, selector):
        try:
            self.clickable_element(selector=selector).click()
            print("--> {} clicked.".format(element_name))
        except WebDriverException:
            print("# {} not clicked! ".format(element_name) + str(selector) + "\n" + traceback.format_exc())
            raise

    def select_element(self, select_locator, option_to_select):
        select = Select(self.visibility_of_element(select_locator))
        select.select_by_value(option_to_select)

    def is_element_displayed(self, selector, timeout=None):
        try:
            if timeout is None:
                timeout = self.timeout
            WebDriverWait(self.driver, int(timeout)).until(ec.visibility_of_element_located(selector))
        except WebDriverException:
            return False
        return True

