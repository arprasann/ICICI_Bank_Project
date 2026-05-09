from utilities.BaseClass import BaseClass

from pageObjects.Login_Page import LoginPage
from pageObjects.Logout_Page import Logout
from pageObjects.Reports import Reports


class Test_Verify_Export_CSV_Reports(BaseClass):

    def test_verify_reports(self):
        loginpage = LoginPage(self.driver)
        self.waitforthreeSecond()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforthreeSecond()
        loginpage.clickonloginbutton()
        self.waitforthreeSecond()


        reports = Reports(self.driver)
        self.waitforthreeSecond()
        reports.clcikonreport()
        self.waitforthreeSecond()
        reports.clcikonNewreport()
        self.waitforthreeSecond()
        reports.clcikonconfigurereport()
        self.waitforthreeSecond()
        reports.clcikongeneratereport()
        self.waitforthreeSecond()
        reports.clcikonexportcsvreport()
        self.waitforthreeSecond()
        self.waitforthreeSecond()

        logout = Logout(self.driver)
        self.waitforthreeSecond()
        logout.click_on_Logout_Button()
        self.waitforthreeSecond()
        self.waitforthreeSecond()
