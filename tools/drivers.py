import pytest

from appium import webdriver

# Xiomi Redmi Note 3 pro
class Drivers:
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'deviceName': '69ab9a73', # Xiomi Redmi note 3 pro
            'appPackage': 'ru.leroymerlin.mobile',
            # 'deviceName': 'UKRWGALZQCWO6TYL' # Xiomi Note 4
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
            'platformVersion': '6.0.1',
            'deviceName': '69ab9a73',  # Xiomi Redmi note 3 pro
            'appPackage': 'ru.leroymerlin.mobile',
            'noReset': 'true'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value


    # Xiomi Mi Max
    @pytest.fixture(scope="function")
    def _c_driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'f327c0d3',
            'appPackage': 'ru.leroymerlin.mobile',
            'noReset': 'true'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value

    @pytest.fixture(scope="function")
    def _driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'f327c0d3',
            'appPackage': 'ru.leroymerlin.mobile',
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value



    # Samsung S8
    @pytest.fixture(scope="function")
    def _c_driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'ce051715c550d01d03', # Samsung S8,
            'appPackage': 'ru.leroymerlin.mobile',
            'noReset': 'true'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value

    @pytest.fixture(scope="function")
    def _driver(self, request):
        desired_caps = {
            'automationName': 'Appium',
            'appActivity': 'ru.leroymerlin.mobile.presentation.MainActivity',
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'ce051715c550d01d03', # Samsung S8
            'appPackage': 'ru.leroymerlin.mobile',
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value