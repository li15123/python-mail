#教程https://blog.csdn.net/ITBigGod/article/details/103349626
#coding=UTF-8
import time
from selenium import webdriver

browser = webdriver.Chrome()   # 或填入chromedriver.exe的绝对路径
normal_window = browser.get("https://mail.163.com/")
time.sleep(5)      # 加延迟，为了加载元素，避免太快出现异常

# //*[@id="switchAccountLogin"]
#browser.find_element_by_id('switchAccountLogin').click()  #点一下账号密码登录选项

# 切换到iframe表单，这是网易邮箱通用的一个框架-x-URS-iframe1574869494571.3655,
browser.switch_to.frame(0)
# 自动填入
browser.find_element_by_name("email").clear()
browser.find_element_by_name("email").send_keys("xxxx@163.com")
browser.find_element_by_name("password").clear()
browser.find_element_by_name("password").send_keys("xxx")
browser.find_element_by_css_selector("#dologin").click()  # 登录按钮