#coding=UTF-8
import json
from email163 import loginEmail163

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_emailType(myEmail):
    myEmail = myEmail.split(".")
    myEmail = myEmail[0].split("@")
    return myEmail[1]


#load serverName
with open('./serverNameConfig.json','r')as severJson:
    server_json = json.load(severJson)

#load email
with open('./email.json','r')as emailJson:
    email_json = json.load(emailJson)    

#print('This is a \033[1;35m %s \033[0m!' %user)
print('\033[1;35m ++++++++++++++++++++++++++开始+++++++++++++++++++++++++++++++ \033[0m')
for user in email_json:
    for password in email_json[user]:
        emailType = get_emailType(user)
        if emailType == "163":
            if loginEmail163(user, password) :
                break
print ""
print('\033[1;35m ++++++++++++++++++++++++++结束+++++++++++++++++++++++++++++++ \033[0m')