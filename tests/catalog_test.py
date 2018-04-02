import os

from pages.intro import IntroPage
from pages.main import MainPage
from tools.drivers import Drivers

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestCatalogclass(IntroPage, MainPage, Drivers):
    driver = Drivers.xiaomi_driver
    c_driver = Drivers.xiaomi_c_driver
