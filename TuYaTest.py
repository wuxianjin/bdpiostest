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


class TuYaTest(unittest.TestCase):

    def setUp(self):
        try:
            self.__driver = AppiumInit.getDriver()
        except Exception as err:
            
            self.assertEquals(1,0,"appium server init failed")


   
  

    def test_scroll(self):
        els = self.__driver.find_elements_by_class_name('UIAButton')
        els[5].click()
        #self.__driver.execute(Command.GO_BACK)
      
if __name__ == '__main__':
   
    unittest.main()
    driver.quit()
