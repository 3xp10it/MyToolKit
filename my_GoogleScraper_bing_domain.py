#need python3 coz GoogleScraper require it.
#and python3 with GoogleScraper unchanged selenium version python environment,
#coz bing does not need supass yanzhengma
#on this computer is "workon virtualenv2"
#/root/myenv2/bin/python3.5m
import socket
import re
import sys
import os 


def usage():
    print("-----------------------------------------------------------")
    print("this is a py script to gain domains from the same ip\nusage:")
    print("example:python %s xxx.xxx.xxx" % sys.argv[0])
    print("example:python %s -f file.txt" % sys.argv[0])
    print("-----------------------------------------------------------")


 #this is a function to remove \r\n or \n from one sting   
def get_pure_list(list):
    pure_list=[]
    for each in list:
        each=re.sub(r'(https://)|(http://)|(\s)|(/.*)',"",each)
        pure_list.append(each)
        #re.sub(r'\r\n',"",each)
        #re.sub(r'\n',"",each)
    return pure_list
#this is a function to save url_list to file
def save_url_to_file(url_list,name):
    file=open(name,"a+")
    file.close()   
    for ur in url_list:
        file=open(name,"r+")  
        '''
        python3下不可写成"ab+",although in linux,且"a+"不能支持readlines,读不出来数据,i chosed "a+" for file write,and close file,then "r+" for f.readlines(),
        于是python3下还得事先创建url.txt,因为上面的"r+"会发现没有urls.txt文件
        file=open("urls.txt","ab+")  python2 下可以"ab+" 
        '''
        all_lines=file.readlines()
        print(all_lines)
        print(len(all_lines))
        file.close()

        #if ur+"\r\n" not in all_lines:
        if ur+"\n" not in all_lines:
            '''
            python3下write(ur+"\r\n")也只能在字符串后加到"\n",不会加上"\r\n",python2下write(ur+"\r\n")是加上"\r\n"
            所以python2下的if ur+"\r\n" not in all_lines要写成if ur+"\n" not in all_lines
            '''
            #print(type(ur))
            #print(type("\r\n"))
            #print(type(ur+"\r\n"))
            file=open(name,"a+")
            '''
            file.write(ur+"\r\n"),python3下写成 ur+"\r\n" 或 ur+"\n" 效果一样
            写成+"\n"则产生的文件放到windows下看不到换行的效果(形如http://xxx.xxx.xxxhtt://xxx.xxx.xxx),实际处理起来(读文件)好像也是
            有"按换行读的效果的,file.write(ur+"\r\n")会写成'http://twitter.com\n', 'https://twitter.com\n', 'http://twitter.com/hashtag\n'的效果"

            '''
            #print 11112212
            print(ur)
            file.write(ur+"\r\n")
            file.flush()
            file.close()
#this is a function to get a ip from a domain
def getIp(domain):    
    #the below function getaddrinfo may not be good as function gethostbyname
    try:
    	myaddr=socket.getaddrinfo(domain,'http')[0][4][0]
    	return myaddr
    except:
    	pass





#start from here actually if there is a main entrance

def myGoogleScraperbingdomains():    
    if len(sys.argv)!=2 and sys.argv[1]!='-f':
        usage()
        sys.exit(0)
    if sys.argv[1]=='-f':
        try:
            print("444444444444success here")
            file=open(sys.argv[2],"r+")
            print("555555555555success here")
        except:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!sys.argv[2] is %s" % sys.argv[2])
            print("open file wrong")
            sys.exit(0)

        target_list=file.readlines()
        print("66666666666target_list is:%s" % target_list)
        file.close()
        true_target_list=[]
        true_target_list=get_pure_list(target_list)
        print("77777777777777pure_list is:%s" % true_target_list)
        for each_domain in true_target_list:
        	try:
        		keyword="ip:"+getIp(each_domain)
        		num_page=50
        		method='selenium'
        		browser='firefox'
        	except:
        		continue
        	print("33333333333333success here")
        	get_the_one_target_domains(each_domain,keyword,num_page,method,browser)
        	

    else:
        #print("please input the domain you want bing to search,eg.www.baidu.com:")#ip:111.111.111.111
        #sharedHost=input()
        sharedHost=sys.argv[1]
        keyword="ip:"+socket.gethostbyname(sharedHost)        
        print("please input the number of pages you want bing to search:")
        num_page=int(input())
        print("please input the method you want bing to search {http,selenium,http-async} :")
        method=input()
        print("please input the browser you want google to use,this take \
        	effects only in [selenium] method,[http] or [http-async] any \
        	is ok,coz take no effects,input one of {firefox,chrome,phantomjs} here:")
        browser=input()
        get_the_one_target_domains(sharedHost,keyword,num_page,method,browser)

def get_the_one_target_domains(sharedHost,keyword,num_page,method,browser):
	sharedHost=sharedHost
	keyword=keyword
	num_page=num_page
	method=method
	browser=browser

	all_nics_ip=socket.gethostbyname_ex(sharedHost)[2]	
	all_urls=[]
	
	from GoogleScraper import scrape_with_config, GoogleSearchError
	
	# See in the config.cfg file for possible values
	config = {
	    'use_own_ip': True,
	    'keyword': keyword,
	    'search_engines': ['bing'],#google,yahoo,baidu,bing...is ok,see GoogleScraper source.
	    'num_pages_for_keyword': num_page,
	    'scrape_method': method,
	    'sel_browser': browser,
	    'do_caching': False
	}
	
	try:
	    search = scrape_with_config(config)
	    #print(11)
	except GoogleSearchError as e:
	    print(e)
	
	# let's inspect what we got
	'''
	for serp in search.serps:    
	    print(serp)
	    print(serp.search_engine_name)
	    print(serp.scrape_method)
	    print(serp.page_number)
	    print(serp.requested_at)
	    print(serp.num_results)
	    
	    # ... more attributes ...
	
	    for link in serp.links:
	        #link=link.split(">")[]
	        #print(type(link))
	        print(link.link)
	        all_urls.append(link.link)
	'''  
	

	GoogleScraper_bing_domain_list=[]
	GoogleScraper_bing_http_domain_list=[]
	GoogleScraper_bing_origin_http_domain_url_list=[]
	
	for serp in search.serps:
	    #print(11)
	    #print(serp)
	    for link in serp.links:        
	        if "https://" in link.link:            
	            domain=(link.link)[8:-1].split('/')[0]
	            #print("domain=(link.link)[8:-1].split('/')[0] is:")
	            #print(domain)
	            try:
	            	ip=getIp(domain)
	            except:
	            	continue
	            if domain not in GoogleScraper_bing_domain_list and ip in all_nics_ip:
	                GoogleScraper_bing_domain_list.append(domain)     
	                GoogleScraper_bing_http_domain_list.append("https://"+domain)
	                GoogleScraper_bing_origin_http_domain_url_list.append(link.link)
	        else:
	            domain=(link.link)[7:-1].split('/')[0]
	            #print("domain=(link.link)[7:-1].split('/')[0] is:")
	            #print(domain)
	            try:
	            	ip=getIp(domain)
	            except:
	            	continue

	            if domain not in GoogleScraper_bing_domain_list and ip in all_nics_ip:                
	                GoogleScraper_bing_domain_list.append(domain)
	                GoogleScraper_bing_http_domain_list.append("http://"+domain)
	                GoogleScraper_bing_origin_http_domain_url_list.append(link.link)


	print("GoogleScraper_bing_domain list is:")
	for pie in GoogleScraper_bing_domain_list:
	    print(pie)
	print("GoogleScraper_bing_http_domain_list is:")
	for pie in GoogleScraper_bing_http_domain_list:
	    print(pie)
	print("GoogleScraper_bing_origin_http_domain_url_list is:")
	for pie in GoogleScraper_bing_origin_http_domain_url_list:
	    print(pie)

	print(555555)
	#sometimes when there are only one page result in the browser,the GoogleScraper 
	#does not work well,so blew we can import "my_bing_domains_v1" module to use
	#normal bing_api to get the domain with only one page result in the browser when
	#we used GoogleScraper's bing_domain search
	if len(GoogleScraper_bing_domain_list)==0:
		#print(6666666666)
		os.system("/usr/bin/python2.7 my_bing_domains_v1_alone.py %s" % sharedHost)
		print(6666666666)
		'''
		import my_bing_domains_v1		
		GoogleScraper_bing_domain_list=((my_bing_domains_v1.get_the_one_target_domains)(sharedHost))[0]
		print(6666666666)
		GoogleScraper_bing_http_domain_list=((my_bing_domains_v1.get_the_one_target_domains)(sharedHost))[1]
		GoogleScraper_bing_origin_http_domain_url_list=((my_bing_domains_v1.get_the_one_target_domains)(sharedHost))[2]
		'''
	save_url_to_file(GoogleScraper_bing_domain_list,"GoogleScraper_bing_domain_list.txt")
	save_url_to_file(GoogleScraper_bing_http_domain_list,"GoogleScraper_bing_http_domain_list.txt")
	save_url_to_file(GoogleScraper_bing_origin_http_domain_url_list,"GoogleScraper_bing_origin_http_domain_url_list.txt")




if __name__ == "__main__":
    myGoogleScraperbingdomains()
