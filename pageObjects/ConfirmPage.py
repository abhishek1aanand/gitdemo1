from selenium.webdriver.common.by import By


class ConfirmPage:

    check_Out2 = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    # self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

    sendKey = (By.ID, "country")
    # self.driver.find_element(By.ID, "country").send_keys("ind")

    text_Select = (By.LINK_TEXT, "India")
    # self.driver.find_element(By.LINK_TEXT, "India").click()

    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    # self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()

    submit = (By.CSS_SELECTOR, "input[type = 'submit']")
    # self.driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()

    message = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    # message = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text

    def __init__(self,driver):
        self.driver = driver

    def checkoutSecondary(self):
        return self.driver.find_element(*ConfirmPage.check_Out2)

    def send_Keys(self):
        return self.driver.find_element(*ConfirmPage.sendKey)

    def click_Text(self):
        return self.driver.find_element(*ConfirmPage.text_Select)

    def checkbox_Click(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def submit_Click(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def success_message(self):
        return self.driver.find_element(*ConfirmPage.message)