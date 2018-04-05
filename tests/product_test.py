import os

from tools.drivers import Drivers
from pages.functions import *
from locators.main_locators import MainLocators
from locators.product_locators import ProductLocators

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(Click, GetText, Swipe, IsObjPresent):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def test_open_products(self, c_driver):
        Click.byXPATH(self, c_driver, MainLocators.PRODUCT_1_NAME)
        time.sleep(2)
        Click.byXPATH(self, c_driver, ProductLocators.PRODUCT_BACK_BUTTON)
        time.sleep(2)
        Click.byXPATH(self, c_driver, MainLocators.PRODUCT_2_NAME)
        time.sleep(2)
        Click.byXPATH(self, c_driver, ProductLocators.PRODUCT_BACK_BUTTON)
        time.sleep(2)
        Click.byXPATH(self, c_driver, MainLocators.PRODUCT_3_NAME)
        time.sleep(2)
        Click.byXPATH(self, c_driver, ProductLocators.PRODUCT_BACK_BUTTON)
        time.sleep(2)
        assert GetText.byXPATH(self, c_driver, MainLocators.MAIN_PAGE_TITLE) == 'Леруа Мерлен'

    def _test_addToCartIfAvailable(self, c_driver):
        # тест пока не работатет( проверка наличия елемента )
        prod_1_name = GetText.byXPATH(self, c_driver, MainLocators.PRODUCT_2_NAME)
        Click.byXPATH(self, c_driver, MainLocators.PRODUCT_2_NAME)
        if IsObjPresent(self, c_driver, ProductLocators.PRODUCT__CANT_BUY_WARNING):
            time.sleep(1)
            Click.byXPATH(self, c_driver, ProductLocators.PRODUCT_ADD_TO_SHOPPING_LIST)
            Click.byID(self, c_driver, MainLocators.SHOPPING_LIST_BUTTON)
        else:
            time.sleep(1)
