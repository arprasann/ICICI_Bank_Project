from utilities.BaseClass import BaseClass

from pageObjects.Login_Page import LoginPage

from pageObjects.Logout_Page import Logout


class Test_Logout_Test(BaseClass):

    def test_verify_logout(self):
        loginpage = LoginPage(self.driver)
        self.waitforthreeSecond()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforthreeSecond()
        loginpage.clickonloginbutton()
        self.waitforthreeSecond()
        self.waitforthreeSecond()

        logout = Logout(self.driver)
        self.waitforthreeSecond()
        logout.click_on_Logout_Button()
        self.waitforthreeSecond()
