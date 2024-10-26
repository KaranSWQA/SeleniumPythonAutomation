from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.CLASS_NAME, "alert-success")
    grabText = (By.CLASS_NAME, "alert-success")

    def getSucessmsgtext(self):
        return self.driver.find_element(*ConfirmPage.grabText)
