import os, time

from tools.drivers import Drivers
from pages.functions import Click, GetText, Swipe, IsObjPresent
from locators.main_locators import MainLocators
from locators.region_locators import RegionLocators

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(Click, GetText, Swipe, IsObjPresent):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def test_change_region_to_SPB(self, c_driver):
        Click.byID(self, c_driver, MainLocators.MY_REGION)
        assert GetText.byXPATH(self, c_driver, RegionLocators.TITLE_REGION) == 'Выбор региона'
        Click.byXPATH(self, c_driver, RegionLocators.REGION_SPB)
        Click.byID(self, c_driver, RegionLocators.CHANGE_CONFIRM_BUTTON)
        assert GetText.byID(self, c_driver, MainLocators.MY_REGION) == 'Санкт-Петербург'

    def test_change_region_to_KURSK(self, c_driver):
        Click.byID(self, c_driver, MainLocators.MY_REGION)
        assert GetText.byXPATH(self, c_driver, RegionLocators.TITLE_REGION) == 'Выбор региона'
        Click.byXPATH(self, c_driver, RegionLocators.REGION_KURSK)
        Click.byID(self, c_driver, RegionLocators.CHANGE_CONFIRM_BUTTON)
        assert GetText.byID(self, c_driver, MainLocators.MY_REGION) == 'Курск'