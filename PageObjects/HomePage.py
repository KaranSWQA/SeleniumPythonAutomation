from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    addPassword = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def addpassword(self):
        return self.driver.find_element(*HomePage.addPassword)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
