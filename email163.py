#coding=UTF-8
import time
from selenium import webdriver


#输入验证码等待时间/秒
wait_time = 30


def loginEmail163(user,password):
    global g_user
    global g_password
    g_user = user
    g_password = password
    browser = webdriver.Chrome()   # 或填入chromedriver.exe的绝对路径
    normal_window = browser.get("https://mail.163.com/")
    #print browser.page_source  
    time.sleep(5)      # 加延迟，为了加载元素，避免太快出现异常

    # //*[@id="switchAccountLogin"]
    #browser.find_element_by_id('switchAccountLogin').click()  #点一下账号密码登录选项

    # 切换到iframe表单，这是网易邮箱通用的一个框架-x-URS-iframe1574869494571.3655,
    browser.switch_to.frame(0)
    # 自动填入
    browser.find_element_by_name("email").clear()
    browser.find_element_by_name("email").send_keys(user)
    browser.find_element_by_name("password").clear()
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_css_selector("#dologin").click()  # 登录按钮   
    time.sleep(10)  

    try:
       ferrorhead = browser.find_element_by_class_name("ferrorhead")
    except Exception as msg:
        print ""
    else:
        if ferrorhead.text == "请先进行验证":
            print "需要验证码"
            time.sleep(wait_time)
        elif ferrorhead.text =="帐号或密码错误":  
            printFail()
            return False
    return verifLogin(browser)

def quitBrowser(br):
    #br.find_element_by_link_text('退出').click()
    br.close()
    br.quit()

def verifLogin(browser):
    global g_user
    browser.switch_to.default_content()
    try:
        spnUid = browser.find_element_by_id("spnUid")
    except Exception as msg:
        printFail()
        quitBrowser(browser)
        return False
    else:
        name = spnUid.text
        if name == g_user:
            printSuccess()
            quitBrowser(browser)
            return True   

def printFail():
    global g_user,g_password
    print('\033[1;31m ************* 登录失败 ************* \033[0m')
    print('\033[1;31m ************* %s %s ************* \033[0m' %(g_user,g_password))


def printSuccess():
    global g_user,g_password
    print('\033[1;32m ------------- 登录成功 ------------- \033[0m')
    print('\033[1;32m ------------- %s %s ------------- \033[0m' %(g_user,g_password))

def read_email(browser):
    # 读邮件
    # class="gWel-mailInfo-ico"
    browser.find_element_by_class_name('gWel-mailInfo-ico').click() # 点未读

    time.sleep(2)
    #class="tv0"  获取内容列表
    readList = browser.find_elements_by_class_name('tv0')
    print(type(readList))
    for read in readList:
        print(read.text)   # 输出列表内容
    # 邮件标题
    readList2 = browser.find_element_by_class_name('rF0.kw0.nui-txt-flag0')
    print('邮件标题：',readList2.text,type(readList))
    readList2.click()

    # 切换到iframe架构中
    frame1 = browser.find_element_by_class_name('oD0')
    browser.switch_to.frame(frame1)                         # 把iframe赋值给frame1，然后传递给方法
    content=browser.find_element_by_class_name('FoxDiv20191010101211487871')   # 这是某个未读邮件的class
    print('邮件内容：',content.text)
    # 回到上一层架构：(多表单时，进入一个表单要切回上一层架构，在切入到另一个表单中)
    browser.switch_to.default_content()
    time.sleep(2)