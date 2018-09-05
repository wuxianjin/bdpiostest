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


class BdpUiTest(unittest.TestCase):

    def setUp(self):
        try:
            self.__driver = AppiumInit.getDriver()
        except Exception as err:
            
            self.assertEquals(1,0,"appium server init failed")
  

    def test_BdpUi1(self):
        els = self.__driver.find_elements_by_class_name('UIATextField')
        els[0].send_keys("haizhi")
        els[1].send_keys("wuxianjin")
        print '=================='
        print len(els)
        mima = self.__driver.find_elements_by_class_name('UIASecureTextField').send_keys("")
        self.__driver.find_element_by_accessibility_id("登录").click()
        #self.__driver.find_element_by_name("登录").click()
        print 'Recommended UI Pass'


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':

    unittest.main()

