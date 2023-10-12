import unittest
from Configuration.drivers_setup import *


class BaseTest(unittest.TestCase):
    driver = None
    browser = 'Chrome'

    @classmethod
    def setUp(cls):
        cls.driver = driver_init(browser=cls.browser)
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
