from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tools.drivers import Drivers
import time


class Click(Drivers):
    driver = Drivers.driver

    # Функции для нажатия кнопки (по XPATH и ID)
    def byXPATH(self, driver, page_element):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, page_element)))
        driver.find_element_by_xpath(page_element).click()

    def byID(self, driver, page_element):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, page_element)))
        driver.find_element_by_id(page_element).click()


class GetText(Drivers):
    driver = Drivers.driver

    # Функции для взятия текста (по XPATH и ID)
    def byXPATH(self, driver, page_element):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, page_element)))
        return driver.find_element_by_xpath(page_element).text

    def byID(self, driver, page_element):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, page_element)))
        return driver.find_element_by_id(page_element).text


class Swipe(Drivers):
    driver = Drivers.driver

    # Функции для свайпа
    def toTop(self, driver):
        time.sleep(3)
        driver.swipe(500, 1100, 500, 200, 1200)

    def toTop2(self, driver):
        time.sleep(3)
        driver.swipe(500, 1000, 500, 500, 500)


class IsObjPresent(Drivers):
    driver = Drivers.driver

    # Функции для проверки наличия объекта (по XPATH и ID)
    def byXPATH(self, driver, image):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, image)))
        if driver.find_element_by_xpath(image).is_displayed():
            return True
        else:
            return False

    def byID(self, driver, image):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, image)))
        if driver.find_element_by_id(image).is_displayed():
            return True
        else:
            return False

class InputText(Drivers):
    driver = Drivers.driver

    def byXPATH(self, driver, input_field, input_text):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_field)))
        driver.find_element_by_xpath(input_field)
        input_field.send_keys(input_text)

    def byID(self, driver, input_field):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, input_field)))
        driver.find_element_by_id(input_field)
        input_field.sendKeys("123456")