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


class PinTuTest(unittest.TestCase):

    __config = {}
    __driver = ();

    def setUp(self):
        try:
            self.__driver = AppiumInit.getDriver()
        except Exception as err:
            self.assertEquals(1,0,"appium server init failed")


   
    #test 拼图--模板
    def test002(self):
        eles = self.__driver.find_elements_by_tag_name("ImageView")
        eles[4].click()
        sleep(1)
        self.__driver.find_element_by_name("Camera(6)").click()
        pintu = self.__driver.find_elements_by_tag_name("ImageView")
        pintu[0].click()
        pintu[1].click()
        sleep(1)
        self.__driver.find_element_by_name("开始拼图").click()
        sleep(2)
        self.__driver.find_element_by_name("保存/分享").click()
        sleep(5)
        self.__driver.find_element_by_name("返回").click()
        print '拼图--模板 pass'
        self.__driver.back()
        self.__driver.back()
        self.__driver.back()


    #test 拼图--自由
    def test003(self):
        eles = self.__driver.find_elements_by_tag_name("ImageView")
        eles[4].click()
        sleep(1)
        self.__driver.find_element_by_name("Camera(6)").click()
        pintu = self.__driver.find_elements_by_tag_name("ImageView")
        pintu[0].click()
        pintu[1].click()
        pintu[2].click()
        sleep(1)
        self.__driver.find_element_by_name("开始拼图").click()
        sleep(2)
        self.__driver.find_element_by_name("自由").click()
        sleep(2)
        self.__driver.find_element_by_name("保存/分享").click()
        sleep(5)
        self.__driver.find_element_by_name("返回").click()
        print '拼图--自由 pass'
        self.__driver.back()
        self.__driver.back()
        self.__driver.back()
        


    #test 拼图--影楼
    def test004(self):
        eles = self.__driver.find_elements_by_tag_name("ImageView")
        eles[4].click()
        sleep(1)
        self.__driver.find_element_by_name("Camera(6)").click()
        pintu = self.__driver.find_elements_by_tag_name("ImageView")
        pintu[0].click()
        pintu[1].click()
        pintu[2].click()
        sleep(1)
        self.__driver.find_element_by_name("开始拼图").click()
        sleep(2)
        self.__driver.find_element_by_name("影楼").click()
        sleep(2)
        self.__driver.find_element_by_name("保存/分享").click()
        sleep(5)
        self.__driver.find_element_by_name("返回").click()
        print '拼图--影楼 pass'
        self.__driver.back()
        self.__driver.back()
        self.__driver.back()
       
    #test 拼图--拼接
    def test005(self):
        eles = self.__driver.find_elements_by_tag_name("ImageView")
        eles[4].click()
        sleep(1)
        self.__driver.find_element_by_name("Camera(6)").click()
        pintu = self.__driver.find_elements_by_tag_name("ImageView")
        pintu[0].click()
        pintu[1].click()
        sleep(1)
        self.__driver.find_element_by_name("开始拼图").click()
        sleep(2)
        self.__driver.find_element_by_name("拼接").click()
        sleep(2)
        self.__driver.find_element_by_name("保存/分享").click()
        sleep(5)
        self.__driver.find_element_by_name("返回").click()
        print '拼图--拼接 pass'
        self.__driver.back()
        self.__driver.back()
        self.__driver.back()
       

    
if __name__ == '__main__':
    unittest.main()
    driver.quit()
