import os
from pages.functions import *
from tools.drivers import Drivers
from locators.main_locators import MainLocators
from locators.cart_locators import CartLocators


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


class TestWebViewAndroid(Click, GetText, Swipe, IsObjPresent):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def test_cart_page_opened(self, c_driver):
        Click.byID(self, c_driver, MainLocators.CART_BUTTON)
        assert GetText.byID(self, c_driver, CartLocators.CART_PAGE_TITLE) == 'Корзина'
        Click.byXPATH(self, c_driver, CartLocators.CART_PAGE_CLOSE_BUTTON)
        assert GetText.byXPATH(self, c_driver, MainLocators.MAIN_PAGE_TITLE) == 'Леруа Мерлен'
