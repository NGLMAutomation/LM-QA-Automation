import os, time

from tools.drivers import Drivers
from pages.functions import Click, GetText, Swipe, IsObjPresent, InputText
from locators.main_locators import MainLocators
from locators.profile_locators import ProfileLocators


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(Click, GetText, Swipe, IsObjPresent):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def test_input_email(self, c_driver):
        Click.byXPATH(self, c_driver, MainLocators.PROFILE_BUTTON)
        time.sleep(5)
        Click.byID(self, c_driver, ProfileLocators.EMAIL_INPUT_FIELD)
        time.sleep(3)
        InputText.byID(self, c_driver, ProfileLocators.EMAIL_INPUT_FIELD)
