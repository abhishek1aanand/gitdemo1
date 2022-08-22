from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # homePage.shopItems().click()

        # self.driver.find_element(By.LINK_TEXT, 'Shop').click()
        # phones_cart = self.driver.find_elements(By.XPATH, "//app-card-list/app-card/div")
        # checkOutPage = CheckOutPage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all phone elements")
        phones_cart = checkOutPage.getPhoneNames()
        for phones in phones_cart:

            product_name = checkOutPage.filterPhoneName(phones).text
            # product_name = phones.find_element(By.XPATH,
            #                                    "div/h4").text  # chaining - > note that there is no '/' before div
            log.info(product_name)
            if product_name == "Blackberry":
                # phones.find_element(By.XPATH, "div/button").click()
                checkOutPage.clickAddCart().click()
        confirmPage = checkOutPage.checkoutPrimary()
        # checkOutPage.checkoutPrimary().click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmPage.checkoutSecondary().click()
        # self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        log.info("entering country name as India")
        confirmPage.send_Keys().send_keys("indi")
        # self.driver.find_element(By.ID, "country").send_keys("ind")

        self.verifyLinkPresence("India")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        confirmPage.click_Text().click()
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.checkbox_Click().click()
        # self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        confirmPage.submit_Click().click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()
        message = confirmPage.success_message().text
        # message = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
        log.info(f"Text received from application is {message}")
        assert "Success! Thank you!" in message
        assert "Success" in message
        assert "Thank" in message
