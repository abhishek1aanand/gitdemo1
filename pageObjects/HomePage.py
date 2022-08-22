from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    # self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Abhishek Anand")
    email = (By.NAME, "email")
    # self.driver.find_element(By.NAME, "email").send_keys("abhishek1aanand@gmail.com")
    password = (By.ID, "exampleInputPassword1")
    # self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
    check = (By.ID, "exampleCheck1")
    # self.driver.find_element(By.ID, "exampleCheck1").click()
    dropdown = (By.ID, "exampleFormControlSelect1")
    # self.driver.find_element(By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    message = (By.CLASS_NAME, "alert-success")

    # self.driver.find_element(By.CLASS_NAME, "alert-success").text

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        # return self.driver.find_element(*HomePage.shop)
        # driver.find_element(By.LINK_TEXT, 'Shop').click()
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def pass_Name(self):
        return self.driver.find_element(*HomePage.name)

    def pass_Email(self):
        return self.driver.find_element(*HomePage.email)

    def pass_Password(self):
        return self.driver.find_element(*HomePage.password)

    def checkBox(self):
        return self.driver.find_element(*HomePage.check)

    def dropDown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def Submit(self):
        return self.driver.find_element(*HomePage.submit)

    def Message(self):
        return self.driver.find_element(*HomePage.message)
