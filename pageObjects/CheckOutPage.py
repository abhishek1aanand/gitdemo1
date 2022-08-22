# Page Objects Mechanism
from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    phones_cart = (By.XPATH, "//app-card-list/app-card/div")
    # phones_cart = self.driver.find_elements(By.XPATH, "//app-card-list/app-card/div")

    filter_phones = (By.XPATH, "div/h4")  # chaining
    # product_name = phones.find_element(By.XPATH,
    #                                    "div/h4").text  # chaining - > note that there is no '/' before div

    add_Cart = (By.XPATH, "//app-card[4]/div/div[2]/button")
    # phones.find_element(By.XPATH, "div/button").click()

    check_Out = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

    def __init__(self, driver):
        self.driver = driver

    def getPhoneNames(self):
        return self.driver.find_elements(*CheckOutPage.phones_cart)

    @staticmethod
    def filterPhoneName(phones):
        return phones.find_element(*CheckOutPage.filter_phones)

    def clickAddCart(self):
        return self.driver.find_element(*CheckOutPage.add_Cart)

    def checkoutPrimary(self):
        # return self.driver.find_element(*CheckOutPage.check_Out)
        self.driver.find_element(*CheckOutPage.check_Out).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
