import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait


from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        log.info("getting all the card titles")
        checkOutPage = CheckoutPage(self.driver)
        itemslist = checkOutPage.getItemsLists()
        for product in itemslist:
            # productName = product.find_element(By.XPATH, "div/h4/a").text
            if product == "Blackberry":
                checkOutPage.getCardFooter().click()

        checkOutPage.getAddCartButton().click()
        checkOutPage.get_ClickCheckout().click()
        log.info("Entering country name as ind")
        checkOutPage.get_EnterCountry().send_keys("ind")
        self.verifyLinkPresence("India")

        checkOutPage.getAddIndCount().click()
        checkOutPage.getClickCheckBox().click()
        confirmpage = checkOutPage.getClickPurchaseButton()

        successText = confirmpage.getSucessmsgtext().text
        assert "Success! Thankk you!" in successText
        log.info("Text received from application is "+successText)
        self.driver.close()
