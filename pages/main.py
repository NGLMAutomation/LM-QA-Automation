from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.main_locators import MainLocators
from tools.drivers import Drivers


class MainPage(Drivers):
    driver = Drivers.driver

    # OLD CODE__________________________________________________________________________________________________

    def getActualRegion(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, MainLocators.ACTUAL_REGION)))
        actual_region = driver.find_element_by_id(MainLocators.ACTUAL_REGION)
        actual_region_text = actual_region.text

        return actual_region_text

    def clickInfoButton(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, MainLocators.INFO_BUTTON)))
        info_button = driver.find_element_by_id(MainLocators.INFO_BUTTON)
        info_button.click()

    def getDeliveryTitle(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, MainLocators.TITLE_DELIVERY)))
        delivery_title_text = driver.find_element_by_id(MainLocators.TITLE_DELIVERY).text

        return delivery_title_text

    def clickCartButton(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, MainLocators.MAIN_PAGE_CART_BUTTON)))
        info_button = driver.find_element_by_id(MainLocators.INFO_BUTTON)
        info_button.click()

    def clickBPLookAllButton(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, MainLocators.BP_LOOK_ALL_BUTTON)))
        bpLookAll_button = driver.find_element_by_xpath(MainLocators.BP_LOOK_ALL_BUTTON)
        bpLookAll_button.click()

    # OLD CODE__________________________________________________________________________________________________
