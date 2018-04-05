import os, time

from tools.drivers import Drivers
from pages.functions import Click, GetText, Swipe, IsObjPresent
from locators.main_locators import MainLocators
from locators.product_locators import ProductLocators
from locators.shoppingList_locators import ShopListLocators
from locators.cart_locators import CartLocators

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(Click, GetText, Swipe, IsObjPresent):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def test_new_productAddedToCartAndList(self, c_driver):
        prod_name = GetText.byXPATH(self, c_driver, MainLocators.PRODUCT_2_NAME)
        Click.byXPATH(self, c_driver, MainLocators.PRODUCT_2_NAME)
        assert GetText.byID(self, c_driver, ProductLocators.PRODUCT_NAME) == prod_name
        Click.byXPATH(self, c_driver, ProductLocators.PRODUCT_ADD_TO_SHOPPING_LIST)
        Click.byXPATH(self, c_driver, ProductLocators.PRODUCT_ADD_TO_CART)
        Click.byID(self, c_driver, MainLocators.SHOPPING_LIST_BUTTON)
        assert GetText.byXPATH(self, c_driver, ShopListLocators.SHOPPING_LIST_PAGE_TITLE) == 'Мои списки'
        assert GetText.byXPATH(self, c_driver, ShopListLocators.SHOPPING_LIST_1_PRODUCT_NAME) == prod_name
        Click.byID(self, c_driver, ShopListLocators.SHOPPING_LIST_CART_BUTTON)
        assert GetText.byID(self, c_driver, CartLocators.CART_PAGE_TITLE) == 'Корзина'
        assert GetText.byID(self, c_driver, CartLocators.CART_1_PRODUCT_NAME) == prod_name

    def test_new_clearCartAndList(self, c_driver):
        Click.byID(self, c_driver, MainLocators.SHOPPING_LIST_BUTTON)
        assert GetText.byXPATH(self, c_driver, ShopListLocators.SHOPPING_LIST_PAGE_TITLE) == 'Мои списки'
        Click.byXPATH(self, c_driver, ShopListLocators.SHOPPING_LIST_CLEAR_BUTTON)
        Click.byID(self, c_driver, ShopListLocators.SHOPPING_LIST_CLEAR_CONFIRM_BUTTON)
        assert IsObjPresent.byXPATH(self, c_driver, ShopListLocators.SHOPPING_LIST_EMPTY_IMAGE) == True
        Click.byID(self, c_driver, ShopListLocators.SHOPPING_LIST_CART_BUTTON)
        assert GetText.byID(self, c_driver, CartLocators.CART_PAGE_TITLE) == 'Корзина'
        Click.byXPATH(self, c_driver, CartLocators.CART_CLEAR_BUTTON)
        Click.byID(self, c_driver, CartLocators.CART_CLEAR_CONFIRM_BUTTON)
        assert IsObjPresent.byID(self, c_driver, CartLocators.CART_EMPTY_IMAGE) == True





