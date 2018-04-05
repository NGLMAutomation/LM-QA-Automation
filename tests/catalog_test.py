import os
from pages.functions import *
from tools.drivers import Drivers
from locators.Catalog_Locators import CatalogLocators
from locators.main_locators import MainLocators
from locators.product_locators import ProductLocators

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestCatalogclass(Click, GetText, Swipe, IsObjPresent):
    driver = Drivers.driver
    c_driver = Drivers.c_driver

    def test_catalog_add_wish_list(self, c_driver):
        Click.byID(self, c_driver, MainLocators.CATALOG_BUTTON)
        time.sleep(2)
        assert GetText.byXPATH(self, c_driver, CatalogLocators.CATALOG_TITLE) ==\
               'Каталог товаров'


        Click.byXPATH(self, c_driver, CatalogLocators.CATALOG_1lvl_1_CATEGORY)
        time.sleep(2)
        assert GetText.byXPATH(self, c_driver, CatalogLocators.CATALOG_TITLE_2LVL) == \
                'Стройматериалы'


        Click.byXPATH(self, c_driver, CatalogLocators.CATALOG_2LVL_1_CATEGORY)
        time.sleep(2)
        assert GetText.byXPATH(self, c_driver, CatalogLocators.CATALOG_3LVL_1_CATEGORY) == \
               'Штукатурки'


        Click.byXPATH(self, c_driver, CatalogLocators.CATALOG_3LVL_1_CATEGORY)
        time.sleep(2)
        assert GetText.byXPATH(self, c_driver, CatalogLocators.PRODUCT_SHTYCATYRCA) == \
               'Штукатурка гипсовая Лучшая цена, 30 кг'


        Click.byXPATH(self, c_driver, CatalogLocators.PRODUCT_SHTYCATYRCA)
        time.sleep(2)
        assert IsObjPresent.byID(self, c_driver, ProductLocators.PRODUCT_SHARING_BUTTON) == True
        assert GetText.byXPATH(self, c_driver, CatalogLocators.PRODUCT_SHTYCATYRCA) == \
               'Штукатурка гипсовая Лучшая цена, 30 кг'


        Click.byID(self, c_driver, ProductLocators.PRODUCT_ADD_TO_WISH_LIST_BUTTON)
        assert GetText.byXPATH(self, c_driver, ProductLocators.PRODUCT_ADDED_IN_WISH_LIST_BUTTON) == 'В списке'



