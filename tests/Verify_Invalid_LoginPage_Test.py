from utilities.BaseClass import BaseClass

from pageObjects.Login_Page import LoginPage

from pageObjects.Invalid_LoginPage import Invalid_LoginPage


class Test_Invalid_LoginPage(BaseClass):

    def test_verify_invalid_loginpge(self):
        invalidloginpage = LoginPage(self.driver)
        self.waitforthreeSecond()
        invalidloginpage.setusername("admin")
        invalidloginpage.setpassword("manager")
        self.waitforthreeSecond()
        invalidloginpage.clickonloginbutton()
        self.waitforthreeSecond()
        invalidloginpageerrormsg = Invalid_LoginPage(self.driver)
        self.waitforthreeSecond()
        invalidloginpageerrormsg.verify_error_msg()
        self.waitforthreeSecond()