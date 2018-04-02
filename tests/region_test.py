import os, time

from tools.drivers import Drivers
from pages.All_functions import AllFunc
from locators.main_locators import MainLocators
from locators.choose_region_locators import ChoseRegion

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(AllFunc):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def _test_choose_region_page_open2(self, c_driver):
        time.sleep(2)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, MainLocators.MAIN_PAGE_TITLE) == 'Леруа Мерлен'
        AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.INFO_BUTTON)

    def _test_choose_region_page_open(self, c_driver):
        time.sleep(2)
        AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_BACK_BUTTON)

    def _test_change_region_to_piter(self, c_driver):
        AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ChoseRegion.REGION_PITER)
        AllFunc.clickOnPageElementByID(self, c_driver, ChoseRegion.CHANHE_REGION_CONFIRM_BUTTON)
        assert AllFunc.getTextFromPageElemenByID(self, c_driver, MainLocators.ACTUAL_REGION) == 'Санкт-Петербург'

    def _test_change_region_to_kursk(self, c_driver):
        AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ChoseRegion.REGION_KURSK)
        AllFunc.clickOnPageElementByID(self, c_driver, ChoseRegion.CHANHE_REGION_CONFIRM_BUTTON)
        assert AllFunc.getTextFromPageElemenByID(self, c_driver, MainLocators.ACTUAL_REGION) == 'Курск'

    def _test_change_region_to_ekaterinburg(self, c_driver):
        AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ChoseRegion.REGION_EKATERINBUGR)
        AllFunc.clickOnPageElementByID(self, c_driver, ChoseRegion.CHANHE_REGION_CONFIRM_BUTTON)
        assert AllFunc.getTextFromPageElemenByID(self, c_driver, MainLocators.ACTUAL_REGION) == 'Екатеринбург'

    def _test_change_region_to_krasnodar(self, c_driver):
        AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ChoseRegion.REGION_KRASNODAR)
        AllFunc.clickOnPageElementByID(self, c_driver, ChoseRegion.CHANHE_REGION_CONFIRM_BUTTON)
        assert AllFunc.getTextFromPageElemenByID(self, c_driver, MainLocators.ACTUAL_REGION) == 'Краснодар'

    def _test_change_region_to_moscow(self, c_driver):
        AllFunc.clickOnPageElementByID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert AllFunc.getTextFromPageElemenByXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        AllFunc.clickOnPageElementByXPATH(self, c_driver, ChoseRegion.REGION_MOSCOW)
        AllFunc.clickOnPageElementByID(self, c_driver, ChoseRegion.CHANHE_REGION_CONFIRM_BUTTON)
        assert AllFunc.getTextFromPageElemenByID(self, c_driver, MainLocators.ACTUAL_REGION) == 'Москва и область'
