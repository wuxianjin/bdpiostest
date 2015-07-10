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


class SetingUiTest(unittest.TestCase):

    def setUp(self):
        try:
            self.__driver = AppiumInit.getDriver()
        except Exception as err:
            
            self.assertEquals(1,0,"appium server init failed")


   
  

    def test_SetingUi1(self):
        els = self.__driver.find_elements_by_class_name('UIAButton')
        els[7].click()
        sleep(1)
        self.__driver.find_element_by_accessibility_id("Sign In").click()
        sleep(1) 
        zhuce = self.__driver.find_elements_by_class_name('UIATextField')
        zhuce[0].send_keys('baidu123')
        self.__driver.find_element_by_accessibility_id("Back").click()
        print 'Sign UI Pass'
        


   
    
    def test_SetingUi2(self):
        self.__driver.find_element_by_accessibility_id("Materials management").click()
        sleep(1)
        self.__driver.find_element_by_accessibility_id("Back").click()
        print 'Materials managemen UI Pass'

        


   
  
    
    def test_SetingUi3(self):
        self.__driver.find_element_by_accessibility_id("Sharing settings").click()
        sleep(1)
        self.__driver.find_element_by_accessibility_id("Back").click()
        print 'Sharing settings UI Pass'

        


   
  
    
    def test_SetingUi4(self):
        self.__driver.find_element_by_accessibility_id("Feedback").click()
        sleep(1)
        zhuce = self.__driver.find_elements_by_class_name('UIATextField')
        zhuce[0].send_keys('beautefall')
        self.__driver.find_element_by_accessibility_id("Back").click()
        print 'Feedback settings UI Pass'

        


   
  
    
    def test_SetingUi5(self):
        self.__driver.find_element_by_accessibility_id("About").click()
        sleep(1)
        self.__driver.find_element_by_accessibility_id("Back").click()
        print 'About settings UI Pass'

   
  
    '''
    def test_SetingUi3(self):
        sleep(1)
        self.__driver.find_element_by_accessibility_id("Saved As   Large").click()
        sleep(1)
        self.__driver.find_element_by_accessibility_id("Mid(720").click()
        self.__driver.find_element_by_accessibility_id("Back").click()
        print 'Saved As UI Pass'
        

    def test_MoTuUi5(self):
        els = self.__driver.find_elements_by_class_name('UIAButton')
        els[7].click()
        self.__driver.find_element_by_accessibility_id("Back").click()
        print 'Seting UI Pass' '''
        
        
              
if __name__ == '__main__':
   
    unittest.main()
    driver.quit()
