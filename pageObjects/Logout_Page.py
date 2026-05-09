from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

class Logout(BaseClass):
    logoutButton = (By.ID,"logoutLink")

    def __init__(self,driver):
        self.driver = driver


    def click_on_Logout_Button(self):
        self.verify_element_clickable(By.ID,"logoutLink")
        return self.driver.find_element(*Logout.logoutButton).click()
