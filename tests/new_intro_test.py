import os

from tools.drivers import Drivers

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWebViewAndroid(IntroPage, MainPage, Drivers):
    driver = Drivers.driver
    c_driver = Drivers.c_driver