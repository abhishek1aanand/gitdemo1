import inspect
import logging

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # now logger object is responsible to log everything
        fileHandler = logging.FileHandler(
            'logfile.log')  # fileHandler is basically the file location where logs are to be saved
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # we have to pass filehandler object into addHandler

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, Text):
        # dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown = Select(locator)
        dropdown.select_by_visible_text(Text)
        # dropdown.select_by_index(0)
