import os
from pages.All_functions import AllFunc
from tools.drivers import Drivers
from locators.main_locators import MainLocators
from locators.bp_locators import BPLocators
from locators.product_locators import ProductLocators
from locators.shoppingList_locators import ShopListLocators
from locators.cart_locators import CartLocators


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


class TestWebViewAndroid(AllFunc):
    driver = Drivers.driver
    c_driver = Drivers.c_driver


    # def test_cart_page_opened(self, c_driver):
    #     MainPage.swipeToTop(self, c_driver)
    #     MainPage.clickBPLookAllButton(self, c_driver)
    #     assert BPPage.getBPTitle(self, c_driver) == 'Лучшая цена'
    #     BPPage.clickBPPageBackButton(self, c_driver, BPLocators.BP_BACK_BUTTON)
    #     assert MainPage.getMainPageTitle(self, c_driver) == 'Леруа Мерлен'

    def test_best_price_page_opened(self, c_driver):
        AllFunc.swipeToTop(self, c_driver) # Свайпить снизу вверх
        AllFunc.clickOnPageElementByXPATH(self, c_driver, MainLocators.BP_LOOK_ALL_BUTTON) # Нажать на кнопку MainLocators.BP_LOOK_ALL_BUTTON
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, BPLocators.BP_PAGE_TITLE) == 'Лучшая цена'  # Проверить равен ли текст в BPLocators.BP_PAGE_TITLE заданному
        AllFunc.clickOnPageElementByXPATH(self, c_driver, BPLocators.BP_BACK_BUTTON) # Нажать на кнопку BPLocators.BP_BACK_BUTTON
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, MainLocators.MAIN_PAGE_TITLE) == 'Леруа Мерлен' # Проверить равен ли текст в MainLocators.MAIN_PAGE_TITLE заданному