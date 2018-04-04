import pytest

from appium import webdriver


class Drivers:
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            #'deviceName': '69ab9a73', # Xiomi Redmi note 3 pro (My)
            # 'deviceName': 'ce051715c550d01d03', # Samsung S8
            # 'deviceName': 'emulator-5554',  # Emulator
            'appPackage': 'ru.leroymerlin.mobile',
            'deviceName': 'UKRWGALZQCWO6TYL' # Xiomi Note 4
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value

    @pytest.fixture(scope="function")
    def c_driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '6.0',
            #'deviceName': '69ab9a73',  # Xiomi Redmi note 3 pro (My)
            # 'deviceName': 'ce051715c550d01d03', # Samsung S8
            # 'deviceName': 'emulator-5554',  # Emulator
            'deviceName': 'UKRWGALZQCWO6TYL', #Xiomi Note 4
            'appPackage': 'ru.leroymerlin.mobile',
            'noReset': 'true'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value
