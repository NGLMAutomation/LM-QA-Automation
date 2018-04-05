import os
from pages.functions import *
from tools.drivers import Drivers
from locators.main_locators import MainLocators
from locators.bp_locators import BPLocators
from locators.product_locators import ProductLocators
from locators.shoppingList_locators import ShopListLocators
from locators.cart_locators import CartLocators


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


class TestWebViewAndroid(Click, GetText, Swipe, IsObjPresent):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def test_best_price_page_opened(self, c_driver):
        Swipe.toTop(self, c_driver) # Свайпить снизу вверх
        Click.byXPATH(self, c_driver, MainLocators.BP_LOOK_ALL_BUTTON) # Нажать на кнопку MainLocators.BP_LOOK_ALL_BUTTON
        assert GetText.byXPATH(self, c_driver, BPLocators.BP_PAGE_TITLE) == 'Лучшая цена'  # Проверить равен ли текст в BPLocators.BP_PAGE_TITLE заданному
        Click.byXPATH(self, c_driver, BPLocators.BP_BACK_BUTTON) # Нажать на кнопку BPLocators.BP_BACK_BUTTON
        assert GetText.byXPATH(self, c_driver, MainLocators.MAIN_PAGE_TITLE) == 'Леруа Мерлен' # Проверить равен ли текст в MainLocators.MAIN_PAGE_TITLE заданному