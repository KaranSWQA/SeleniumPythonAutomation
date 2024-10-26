from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    itemslist = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    cardFooter = (By.XPATH,
                  "//body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[2]/app-card-list[1]/app-card[4]/div[1]/div[2]/button[1]")
    addCart = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutButton = (By.XPATH, "//button[@class='btn btn-success']")
    countryField = (By.ID, "country")
    addIndia = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "[type='submit']")

    def getItemsLists(self):
        return self.driver.find_elements(*CheckoutPage.itemslist)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def getAddCartButton(self):
        return self.driver.find_element(*CheckoutPage.addCart)

    def get_ClickCheckout(self):
        return self.driver.find_element(*CheckoutPage.checkOutButton)

    def get_EnterCountry(self):
        return self.driver.find_element(*CheckoutPage.countryField)

    def getAddIndCount(self):
        return self.driver.find_element(*CheckoutPage.addIndia)

    def getClickCheckBox(self):
        return self.driver.find_element(*CheckoutPage.checkBox)

    def getClickPurchaseButton(self):
        '''return self.driver.find_element(*CheckoutPage.purchaseButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage'''
        self.driver.find_element(*CheckoutPage.purchaseButton).click()
        return ConfirmPage(self.driver)
