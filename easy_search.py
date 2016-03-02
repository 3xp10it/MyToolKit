#need py3 coz GoogleScraper need py3 with selenium module changed to make it possible
#to supass yanzhengma
#easy_search.py is stronger than combineGoogleScraper_myurlhandle.py
#coz the latter can get the http_url only while easy_search.py can get 
#the three kinds of url_list and txt
#
#
##/root/myenv2/bin/python3.5m is the normal python3
#/root/myenv/bin/python3.5 is the changed GoogleScraper script version python
#
#function:
#this script get the GoogleScraper_origin_http_domain_url_list.txt 
#that is a file with urls which can be directly thrown into sqlmap to start
#dig sqli(s),and the urls are from google search,eg.
#when you run easy_search.py,you need supply keyword for google search,
#then the result is those urls from this google search,the result file is 
#GoogleScraper_origin_http_domain_url_list.txt. 
import sys
def save_url_to_file(url_list,name):
    file=open(name,"a+")
    file.close()   
    for ur in url_list:
        file=open(name,"r+")  
        all_lines=file.readlines()
        print(all_lines)
        print(len(all_lines))
        file.close()

        #if ur+"\r\n" not in all_lines:
        if ur+"\n" not in all_lines:          
            #print(type(ur))
            #print(type("\r\n"))
            #print(type(ur+"\r\n"))
            file=open(name,"a+")        
            #print 11112212
            print(ur)
            file.write(ur+"\r\n")
            file.flush()
            file.close()




def myGoogleScraper_get_urls_from_query(query,want):
	keyword=query
	num_page=50
	method='selenium'
	browser='firefox'
	from GoogleScraper import scrape_with_config, GoogleSearchError
	
	# See in the config.cfg file for possible values
	config = {
	    'use_own_ip': True,
	    'keyword': keyword,
	    'search_engines': ['google'],#google,yahoo,baidu,bing...is ok,see GoogleScraper source.
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
	GoogleScraper_domain_list=[]
	GoogleScraper_http_domain_list=[]
	GoogleScraper_origin_http_domain_url_list=[]
	all_three_list=[]

	for serp in search.serps:
		for link in serp.links:
			if "https://" in link.link:            
			    domain=(link.link)[8:-1].split('/')[0]
			    #print("domain=(link.link)[8:-1].split('/')[0] is:")
			    #print(domain)
			    if domain not in GoogleScraper_domain_list:   
			    	GoogleScraper_domain_list.append(domain)     
			    	GoogleScraper_http_domain_list.append("https://"+domain)
			    #attention!here is not the same from the bing_search_domin script,
			    #coz we need as much url as possible for sqlmap to try to exploit,
			    #so the origin_http_domain_url_list here will add all of the result,
			    #though the domain is the same,different url is needed.
			    GoogleScraper_origin_http_domain_url_list.append(link.link)
			else:
			    domain=(link.link)[7:-1].split('/')[0]
			    #print("domain=(link.link)[7:-1].split('/')[0] is:")
			    #print(domain)
			    if domain not in GoogleScraper_domain_list:                
			        GoogleScraper_domain_list.append(domain)
			        GoogleScraper_http_domain_list.append("http://"+domain)
			    #attention!here is not the same from the bing_search_domin script,
			    #coz we need as much url as possible for sqlmap to try to exploit,
			    #so the origin_http_domain_url_list here will add all of the result,
			    #though the domain is the same,different url is needed.
			    GoogleScraper_origin_http_domain_url_list.append(link.link)

	save_url_to_file(GoogleScraper_domain_list,"GoogleScraper_domain_list.txt")
	save_url_to_file(GoogleScraper_http_domain_list,"GoogleScraper_http_domain_list.txt")
	save_url_to_file(GoogleScraper_origin_http_domain_url_list,"GoogleScraper_origin_http_domain_url_list.txt")
	all_three_list.append(GoogleScraper_domain_list)
	all_three_list.append(GoogleScraper_http_domain_list)
	all_three_list.append(GoogleScraper_origin_http_domain_url_list)

	import os
	#although os.system("pkill firefox") maybe ok,
	#this is a good chance to learn awk&xargs,meanwhile,
	#os.system("pkill firefox") is not ok here,but below is ok enough
	#to kill all firefox when it lost into stuck.
	os.system('''ps -aux | grep firefox | awk '{print $2}' | xargs kill -9''')
	#os.system("pkill firefox")

	if want=='GoogleScraper_domain_list.txt':
		return all_three_list[0]
	elif want=='GoogleScraper_http_domain_list':
		return all_three_list[1]
	elif want=='GoogleScraper_origin_http_domain_url_list':
		return all_three_list[2]
	else:
		return all_three_list[2]

def usage():
	print('''input your keyword directly after the script,
		example:%s site:www.xxx.ooo inurl:php?id=''' % sys.argv[0])
	sys.exit(0)
def main():
	#print("sys.argv[1] is type:%s" % type(sys.argv[1]))
	para_num=len(sys.argv)
	keyword=""
	for i in range(para_num-1):
		keyword=keyword+sys.argv[i+1]
		if i+1<para_num-1:
			keyword+=" "
	#print keyword

	myGoogleScraper_get_urls_from_query(keyword,want='GoogleScraper_origin_http_domain_url_list')

if __name__ == '__main__':
	if len(sys.argv)==0:
		usage()
	main()








