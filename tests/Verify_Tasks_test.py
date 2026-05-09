from utilities.BaseClass import BaseClass
from pageObjects.Tasks import Tasks
from pageObjects.Login_Page import LoginPage
from pageObjects.Logout_Page import Logout


class Test_Verify_TaskName(BaseClass):

    def test_verify_tasks(self):
        log = self.getLogger()
        log.info("Task Scrip Statrted")
        loginpage = LoginPage(self.driver)
        self.waitforthreeSecond()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.waitforthreeSecond()
        loginpage.clickonloginbutton()

        task = Tasks(self.driver)
        task.clickonTask()
        self.waitforthreeSecond()
        log.info(task.sendtextfiltertaskbyName("DongaSinga"))

        self.waitforthreeSecond()
        task.clcikonapplyfilter()
        self.waitforthreeSecond()

        logout = Logout(self.driver)
        self.waitforthreeSecond()
        logout.click_on_Logout_Button()
        self.waitforthreeSecond()
        log.info("Tasks scrip Executed Successfully..")
