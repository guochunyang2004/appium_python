# -*- coding:utf-8 -*-
from appium import webdriver
import os
basePath = os.path.abspath('.')#获得当前工作目录



caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "5JPDU17826008316",
    #"appPackage": "com.xingin.xhs",    
    #"appActivity": ".activity.SplashActivity",
    "noReset": True, # 免登陆TRUE
    "codeKeyboard": True # 解决不能输入中文的问题
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
imgPath=basePath+u'/res/img'
driver.get_screenshot_as_file(imgPath+u'/test.png')