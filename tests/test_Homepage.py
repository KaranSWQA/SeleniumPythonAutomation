from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["name"])
        homepage.getEmail().send_keys(getData["email"])

        homepage.addpassword().send_keys(getData["password"])

        homepage.getCheckBox().click()

        homepage.submitForm().click()

        message = homepage.getSuccessMessage().text
        assert "Success" in message

        time.sleep(4)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePageData)
    def getData(self, request):
        return request.param
