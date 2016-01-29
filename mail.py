# -*- coding: utf-8 -*-
# make sure your MyToolKit folder has only target file,and make its
# ext 'targets.txt',otherwise you should change the source code to make it 
# good to use.
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import re
import socket

#下面一行要设置成你自己的邮件服务器的地址以及用户名密码发件人信息



def sendMail(mailto,subject,body,format='plain'):

    #host,user,password,fromMail = smtpInfo
    host='smtp.163.com'
    user='xxxxx'
    password='xxxxx'
    fromMail='xxxx'

    if isinstance(body,unicode) is True:
        body=str(body)
    me= ("%s<"+fromMail+">") % (Header('naruto','utf-8'),)
    msg = MIMEText(body,format,'utf-8')
    if not isinstance(subject,unicode):
        subject = unicode(subject)
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = mailto
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
    try:
        s = smtplib.SMTP()
        s.connect(host)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.set_debuglevel(3)
        s.login(user,password)
        s.sendmail(me, mailto, msg.as_string())
        s.quit()
        return True
    except Exception, e:
        print str(e)
        return False



def read_save_msg_from_csv(csv_file):
	f=open(csv_file,"r+")
	list=f.readlines()
	f.close()
	return_list=[]
	import re
	for each in list:
		matchobj=re.match(r'http',each)
		if matchobj:
			#print each
			each=re.sub(r'(\s)',"",each)
			return_list.append(each)      
        #print return_list
        return return_list
def get_result_from_folder(folder):	
	os.system("ls %s/*.csv > csv_file_list.txt" % folder)
	f=open("csv_file_list.txt","r+")
	list=f.readlines()
	os.system("rm csv_file_list.txt")
	final_list=[]
	for each in list:
		each=re.sub(r'(\s)',"",each)
		#print each
		list_from_single_file=read_save_msg_from_csv(each)
		if len(list_from_single_file)>0:
			final_list.append(list_from_single_file)
	#print final_list
	return final_list



def getIp(domain):    
    #the below function getaddrinfo may not be good as function gethostbyname
    try:
    	myaddr=socket.getaddrinfo(domain,'http')[0][4][0]
    	return myaddr
    except:
    	pass

#all_nics_ip=socket.gethostbyname_ex(sharedHost)[2]



def get_source_domain_of_target_sqli_urls(url):
	import socket
	import re
	sqli_url_domain=re.sub(r'(https://)|(http://)|(\s)|(/.*)|(:.*)',"",url)
	#print sqli_url_domain

	f=open("targets.txt","r+")
	targets_list=f.readlines()
	f.close()
	all_list=[]
	for each in targets_list:
		each=re.sub(r'(https://)|(http://)|(\s)|(/.*)|(:.*)',"",each)
		domain=[]
		domain.append(each)
		try:
			all_nics_ip=socket.gethostbyname_ex(each)[2]
			each_list=all_nics_ip+domain
			all_list.append(each_list)
		except:
			pass
	#print all_list
	for single_list in all_list:
		try:			
			sqli_url_ip=socket.gethostbyname_ex(sqli_url_domain)[2]
			#print sqli_url_ip
			#print 55555555
			#print single_list
			if sqli_url_ip[0] in single_list:				
				#print 66666666
				#print single_list[-1]
				return single_list[-1]	
		except:
			pass
		

def get_msg_to_send():
	msg_list=get_result_from_folder("~/.sqlmap/output")                
	msg_to_send="Good News!!! below are the results of sqli output:\r\n-----------------------------------------------------------------------------\r\n"
	for each in msg_list:
		for one in each:
			main_target_domain=get_source_domain_of_target_sqli_urls(one)
			msg_to_send+=(one+'\r\n')
			msg_to_send+='---->>>>>this domain belongs to the main target domain:>>>%s<<<---\r\n' % main_target_domain
			msg_to_send+='-----------------------------------------------------------------------------\r\n'		
	msg_to_send+='enjoy your sqli:D'
	return msg_to_send

def main():
	msg=get_msg_to_send()
	#print 66666666666666666666666666666666666
	sendMail('xxxxx1','annoymous',msg)
	sendMail('xxxxxx2','annoymous',msg)
	sendMail('xxxxxxxxx3','annoymous',msg)


if __name__ == '__main__':
	main()
