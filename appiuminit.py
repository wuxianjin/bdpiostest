import os
import time
from appium import webdriver


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppiumInit(object):

    driver=None

    @staticmethod
    def getDriver():

        if AppiumInit.driver is None:
            config = {}
            config['platformName'] = 'ios'
            config['browserName'] = ''
            
            config['platformVersion'] = '8.3'
            config['deviceName'] = 'iPhone Simulator'
           
            config['app'] = PATH('./MCompass.app')
            
            AppiumInit.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)
        return AppiumInit.driver
    
    def releaseDriver():
        AppiumInit.driver.quit()









