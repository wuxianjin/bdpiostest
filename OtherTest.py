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
from selenium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OtherTest(unittest.TestCase):

    __config = {}
    __driver = ();

    def setUp(self):
        try:
            self.__driver = AppiumInit.getDriver()
        except Exception as err:
            self.assertEquals(1,0,"appium server init failed")


    #test  
    def test001(self):
        sleep(1)
        eles = self.__driver.find_elements_by_tag_name("ImageView")
        eles[4].click()
        self.__driver.back()


    #test 拼图  
    def test002(self):
        eles = self.__driver.find_elements_by_tag_name("ImageView")
        eles[6].click()
        sleep(1)
        self.__driver.find_element_by_name("Camera(6)").click()
        pintu = self.__driver.find_elements_by_tag_name("ImageView")
        pintu[0].click()
        pintu[1].click()
        pintu[2].click()
        sleep(1)
        self.__driver.find_element_by_name("开始拼图").click()
        sleep(2)
        '''self.__driver.find_element_by_name("保存/分享").click()
        sleep(5)
        self.__driver.find_element_by_name("返回").click()'''
        save = self.__driver.find_elements_by_tag_name("TextView")
        save[2].click()
        sleep(4)
        #保存/分享
        '''back = self.__driver.find_elements_by_tag_name("TextView")
        back[6].click()
        sleep(2)'''
        #self.assertEquals('首页',back[2].text)
        self.__driver.back()
        self.__driver.back()

    
if __name__ == '__main__':
    unittest.main()
    driver.quit()
