import os
from pages.functions import *
from tools.drivers import Drivers
from locators.main_locators import MainLocators
from locators.product_locators import ProductLocators


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


class TestWebViewAndroid(AllFunc):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def _test_open_feedback_page(self, c_driver):
        Click.byXPATH(self, c_driver, MainLocators.PRODUCT_1_NAME)
        time.sleep(2)
        #assert IsObjPresent.byXPATH(self, c_driver, ProductLocators.PRODUCT_PAGE_TITLE)
        Click.byXPATH(self, c_driver,ProductLocators.PRODUCT_FEEDBACK_BUTTON)
        assert IsObjPresent.byID(self, c_driver, ProductLocators.PRODUCT_LEFT_FEEDBACK_BUTTON) == True
        assert IsObjPresent.byID(self, c_driver, ProductLocators.PRODUCT_QUESTION_BUTTON) == True