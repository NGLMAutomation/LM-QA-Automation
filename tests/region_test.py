import os, time

from tools.drivers import Drivers
from pages.functions import *
from locators.main_locators import MainLocators
from locators.choose_region_locators import ChoseRegion

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(Click, GetText, Swipe, IsObjPresent):
    driver = Drivers.driver
    c_driver = Drivers.c_driver


    def test_choose_region_page_open(self, c_driver):
        time.sleep(2)
        Click.byID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert GetText.byXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        Click.byXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_BACK_BUTTON)

    def test_change_region_to_piter(self, c_driver):
        Click.byID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert GetText.byXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        Click.byXPATH(self, c_driver, ChoseRegion.REGION_PITER)
        Click.byID(self, c_driver, ChoseRegion.CHANHE_REGION_CONFIRM_BUTTON)
        assert GetText.byID(self, c_driver, MainLocators.ACTUAL_REGION) == 'Санкт-Петербург'

    def test_change_region_to_kursk(self, c_driver):
        Click.byID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert GetText.byXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        Click.byXPATH(self, c_driver, ChoseRegion.REGION_KURSK)
        Click.byID(self, c_driver, ChoseRegion.CHANHE_REGION_CONFIRM_BUTTON)
        assert GetText.byID(self, c_driver, MainLocators.ACTUAL_REGION) == 'Курск'

    def test_change_region_to_ekaterinburg(self, c_driver):
        Click.byID(self, c_driver, MainLocators.ACTUAL_REGION)
        assert GetText.byXPATH(self, c_driver, ChoseRegion.CHOOSE_REGION_TITLE) == 'Выбор региона'
        Click.byXPATH(self, c_driver, ChoseRegion.REGION_EKATERINBUGR)
        Click.byID(self, c_driver, ChoseRegion.CHANHE_REGION_CONFIRM_BUTTON)
        assert GetText.byID(self, c_driver, MainLocators.ACTUAL_REGION) == 'Екатеринбург'
