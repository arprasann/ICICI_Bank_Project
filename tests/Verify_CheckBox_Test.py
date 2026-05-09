from pageObjects.CheckBox import  CheckBox

from utilities.BaseClass import BaseClass

class Test_CheckBox(BaseClass):

    def test_verify_checkbox_selected_or_not(self):
        checkbox = CheckBox(self.driver)
        self.waitforthreeSecond()
        checkbox.clickoncheckbox()
        self.waitforthreeSecond()
