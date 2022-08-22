import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info(f"Full name is: {getData['fullName']}")
        homePage.pass_Name().send_keys(getData["fullName"])
        # self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Abhishek Anand")
        homePage.pass_Email().send_keys(getData["email"])
        homePage.pass_Password().send_keys("12345")
        homePage.checkBox().click()

        # self.driver.find_element(By.NAME, "email").send_keys("abhishek1aanand@gmail.com")
        # self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
        # self.driver.find_element(By.ID, "exampleCheck1").click()
        # # dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        self.selectOptionByText(homePage.dropDown(), getData["gender"])
        # dropdown = Select(homePage.dropDown())
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)
        homePage.Submit().click()
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        message = homePage.Message().text
        # message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
