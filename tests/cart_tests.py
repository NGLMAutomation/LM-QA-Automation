import os
from pages.All_functions import AllFunc
from tools.drivers import Drivers
from locators.main_locators import MainLocators
from locators.cart_locators import CartLocators


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


class TestWebViewAndroid(AllFunc):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def test_cart_page_opened(self, c_driver):
        AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.CART_BUTTON)
        assert AllFunc.getTextFromPageElemenByID(self, c_driver, CartLocators.CART_PAGE_TITLE) == 'Корзина'
        AllFunc.clickOnPageElementByXPATH(self, c_driver, CartLocators.CART_PAGE_CLOSE_BUTTON)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, MainLocators.MAIN_PAGE_TITLE) == 'Леруа Мерлен'
