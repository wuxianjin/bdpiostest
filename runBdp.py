#coding=utf-8

#-*- coding: UTF-8 -*-
import sys
import HTMLTestRunner
import unittest
from appiuminit import AppiumInit
from appium import webdriver
from BdpUiTest import BdpUiTest
from SetingUiTest import SetingUiTest


def suite_use_test_loader():
    test_cases = (BdpUiTest,SetingUiTest)
    suite = unittest.TestSuite()
    #循环添加单个用例类
    for test_case in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite

if __name__ == '__main__':

    testunit = suite_use_test_loader()
    filename="./bdpTestReport.html"
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='bdpTestReport',description='Testing UI exist by UI change')
    runner.run(testunit)
