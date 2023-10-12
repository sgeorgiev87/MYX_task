# this file is for initializing a driver in each test,
# giving opportunities for different environments, browsers, etc.

from selenium import webdriver
from random import randint
from selenium.common.exceptions import WebDriverException
from chromedriver_py import binary_path
import re
import traceback

chromedriver_path = binary_path
geckodriver_path = 'C:/drivers/geckodriver.exe'


def driver_init(browser='Chrome'):

    if browser == 'Chrome':
        svc = webdriver.ChromeService(executable_path=binary_path)
        driver = webdriver.Chrome(service=svc)
    elif browser == 'Firefox':
        driver = 'invoke Firefox driver'
    else:
        raise Exception('#### Please provide valid browser - Chrome or Firefox!')

    return driver


def handle_exception(driver,
                     custom_exception='',
                     raise_exception=True,
                     screenshot_name='Error_' + str(randint(1, 1000)).zfill(4) + '.png'):
    """
    A function to handle any exceptions during the test executions, create a screenshot,
    and raise custom exception message, if wanted
    :param driver: the WebDriver
    :param custom_exception: the custom exception message
    :param raise_exception: if to raise an exception, or just print a message
    :param screenshot_name: custom screenshot name, if needed - i.e. test name + timestamp
    """
    screenshot_pattern = "\w+.(jpg|JPG|png|PNG)$"

    exception = traceback.format_exc()

    if screenshot_name != '':
        scr_path = "./" + screenshot_name
        match = re.match(pattern=screenshot_pattern, string=screenshot_name)
        if match is None:
            raise Exception("Please specify a valid screenshot name --> ABC_Z_abc_z_012_9.(jpg|JPG|png|PNG)")
        try:
            driver.save_screenshot(scr_path)
            print("Screenshot taken: " + screenshot_name)
        except WebDriverException:
            print(screenshot_name + " could not be generated")

    full_exception = custom_exception + '\n' + exception

    if raise_exception:
        raise Exception(full_exception)
    else:
        print(full_exception)
