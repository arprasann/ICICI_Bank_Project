from pageObjects.Login_Page import LoginPage

from utilities.BaseClass import BaseClass

class Test_LoginPage(BaseClass):

    def test_loginpage(self):
        log = self.getLogger()

        log.info("Valid Login Page Script started...")
        loginpage = LoginPage(self.driver)
        self.waitforthreeSecond()
        log.info("Enter the valid Username")
        loginpage.setusername("admin")

        log.info("Succssfully fetched data from dataload")
        self.waitforthreeSecond()
        log.info("Enter The Valid Password")
        loginpage.setpassword("manager")
        self.waitforthreeSecond()
        log.info("Click On Login Button")
        loginpage.clickonloginbutton()
        self.waitforthreeSecond()
        log.info("Login Page scrip successfully Executed")
        self.waitforthreeSecond()