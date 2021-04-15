#coding=UTF-8
import time
from selenium import webdriver

browser = webdriver.Chrome()   # 或填入chromedriver.exe的绝对路径
normal_window = browser.get("https://mail.qq.com/")
time.sleep(5)      # 加延迟，为了加载元素，避免太快出现异常

# //*[@id="switchAccountLogin"]
#browser.find_element_by_id('switchAccountLogin').click()  #点一下账号密码登录选项

frame1=browser.find_element_by_id('login_frame')
browser.switch_to.frame(frame1) #把iframe赋值给frame1，然后传递给方法
# 自动填入
browser.find_element_by_name("u").clear()
browser.find_element_by_name("u").send_keys("xxxx@qq.com")
browser.find_element_by_name("p").clear()
browser.find_element_by_name("p").send_keys("xxxx")
browser.find_element_by_css_selector("#login_button").click()  # 登录按钮