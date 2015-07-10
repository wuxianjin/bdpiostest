#-*- coding: UTF-8 -*-
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
import os  
import unittest
from time import sleep
import string
from appiuminit import AppiumInit
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class xianjin(unittest.TestCase):

    def setUp(self):
        try:
            self.__driver = AppiumInit.getDriver()
        except Exception as err:
            
            self.assertEquals(1,0,"appium server init failed")


   
  

    def test_SetingUi1(self):
        
        self.__driver.PushFile("./123.jpg", "some data for the file");
        els = self.__driver.find_elements_by_class_name('UIAButton')
        els[7].click()
        sleep(1)
        self.__driver.find_element_by_accessibility_id("Sign In").click()
        sleep(1) 
        zhuce = self.__driver.find_elements_by_class_name('UIATextField')
        zhuce[0].send_keys('baidu123')
        # make screenshot and get is as base64
        screenshot = self.__driver.get_screenshot_as_base64()
        self.assertTrue(screenshot)

        # make screenshot and save it to the local filesystem
        success = self.__driver.get_screenshot_as_file("foo1.png")
        self.assertTrue(success)
        self.assertTrue(os.path.isfile("foo1.png"))
        self.__driver.find_element_by_accessibility_id("Back").click()
        print 'Sign UI Pass'
        #os.remove("foo.png")
                
        
        
              
if __name__ == '__main__':
   
    unittest.main()
    driver.quit()
