import os, time

from tools.drivers import Drivers
from pages.All_functions import AllFunc
from locators.main_locators import MainLocators
from locators.product_locators import ProductLocators

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(AllFunc):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def _test_open_products(self, c_driver):
        AllFunc.clickOnPageElementByXPATH(self, c_driver, MainLocators.PRODUCT_1_NAME)
        time.sleep(2)
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ProductLocators.PRODUCT_BACK_BUTTON)
        time.sleep(2)
        AllFunc.clickOnPageElementByXPATH(self, c_driver, MainLocators.PRODUCT_2_NAME)
        time.sleep(2)
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ProductLocators.PRODUCT_BACK_BUTTON)
        time.sleep(2)
        AllFunc.clickOnPageElementByXPATH(self, c_driver, MainLocators.PRODUCT_3_NAME)
        time.sleep(2)
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ProductLocators.PRODUCT_BACK_BUTTON)
        time.sleep(2)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, MainLocators.MAIN_PAGE_TITLE) == 'Леруа Мерлен'

    def _test_addToCartIfAvailable(self, c_driver):
        # тест пока не работатет( проверка наличия елемента )
        prod_1_name = AllFunc.getTextFromPageElemenByXPATH(self, c_driver, MainLocators.PRODUCT_2_NAME)
        AllFunc.clickOnPageElementByXPATH(self, c_driver, MainLocators.PRODUCT_2_NAME)
        if AllFunc.isPicturePresentByID(self, c_driver, ProductLocators.PRODUCT__CANT_BUY_WARNING):
            time.sleep(1)
            AllFunc.clickOnPageElementByXPATH(self, c_driver, ProductLocators.PRODUCT_ADD_TO_SHOPPING_LIST)
            AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.SHOPPING_LIST_BUTTON)
        else:
            time.sleep(1)
