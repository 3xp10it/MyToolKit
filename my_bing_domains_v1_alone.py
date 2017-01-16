# -*- coding: utf-8 -*-
#need python2(my system is py2.7 by default)
#
#
##/root/myenv2/bin/python3.5m is the normal python3
#/root/myenv/bin/python3.5 is the changed GoogleScraper script version python
#
import urllib
import urllib2
import json
import sys
import re
import socket
def main():    
    if len(sys.argv)!=2:
        usage()
        sys.exit(0)
    
    try:
        file=open(sys.argv[1],"r+")
        target_list=file.readlines()
        file.close()
        true_target_list=[]
        true_target_list=get_pure_list(target_list)
        for each in true_target_list:
            try:
                get_the_one_target_domains(each)
            except:
                print "getip or socket.gethostbyname_ex wrong,the site may break down,you can check it."
    except:
        sharedHost=sys.argv[1]
        get_the_one_target_domains(sharedHost)
        print "open file wrong coz this input is not a file but a domain or when you do put a file,then the script open file wrong"
    
        

    
    
    
def get_the_one_target_domains(sharedHost):
    domain_list=[]
    http_domain_list=[]
    origin_http_domain_url_list=[]
    ip=getIp(sharedHost)
    all_nics_ip=socket.gethostbyname_ex(sharedHost)[2]
    #whether sharedHost is hostname or ip appereance,
    #getIP function is ok to get "ip" appereance like x.x.x.x 
    query = "ip:%s" % ip

    #print "query is %s" % query


    
    for piece in bing_search(query, 'Web'):
        if "https://" in piece['Url']:
            
            domain=piece['Url'][8:-1].split('/')[0]
            #print '11111111111111111111111111111111111111:'+domain+'333333:'+getIp(domain)
            #if domain not in domain_list:# and getIp(domain)==ip
            if domain not in domain_list and getIp(domain) in all_nics_ip:
                domain_list.append(domain)     
                http_domain_list.append("https://"+domain)
                origin_http_domain_url_list.append(piece['Url'])
              
            
        else:
            domain=piece['Url'][7:-1].split('/')[0]
            #print '222222222222222222222222222222222222222:'+domain+'333333:'+getIp(domain)
            #if domain not in domain_list:# and getIp(domain)==ip
            if domain not in domain_list and getIp(domain) in all_nics_ip:                
                domain_list.append(domain)
                http_domain_list.append("http://"+domain)
                origin_http_domain_url_list.append(piece['Url'])
    #in the upon for circle,function getIp is ok ,but sometimes we will get two diffirent address
    #when ping some domain,eg.ping defendmainstreet.com  !sometimes we get ip:104.25.209.15
    #sometimes we get 104.25.208.15,this is a strange thing ,may be there exists two NICs on the 
    #same domain,so here ,without check"and getIp(domain)==ip" is better to gain more results
    #although this will get little useless domain.eg. when we try to find the domains of www.baidu.com
    #we will find there would be a domain named "msh.baidu.com",both "k8" and this script will get it,
    #but actually,we can get msh.baidu.com is not the same ip than www.baidu.com by pinging them.
    #if here we don't use check"and getIp(domain)==ip",however,the better and best result chioce is,
    #don't use check"getIp(domain)==ip",finally,this tool is better than k8 from experiment.
    

    #later i found those comments upon are right ,and there exists a better solution,
    #that is use function "gethostbyname_ex",
    #more info see http://walkerqt.blog.51cto.com/1310630/1686735

    #print "getip(192.168.0.1)is :%s" % getIp("192.168.0.1")
    print "domain list is:" 
    for pie in domain_list:
        print pie
    print "http_domain_list is:"
    for pie in http_domain_list:
        print pie
    save_url_to_file(domain_list,"bing_domain_list.txt")
    save_url_to_file(http_domain_list,"bing_http_domain_list.txt")
    save_url_to_file(origin_http_domain_url_list,"bing_origin_http_domain_url_list.txt")


    #now we get the domain_list,https'url's domain included,
    #and saved the urls to file
    

    #print bing_search(query, 'Image')



#this is a function to get a ip from a domain

def getIp(domain):
    import socket   
    try:
        myaddr=socket.getaddrinfo(domain,'http')[0][4][0]
        return myaddr
    except:
        print "getip wrong5555555555555555"


#this is a function to remove \r\n or \n from one sting
def get_pure_list(list):
    pure_list=[]
    for each in list:
        each=re.sub(r'(https://)|(http://)|(\s)|(/.*)|(:.*)',"",each)
        pure_list.append(each)
        #re.sub(r'\r\n',"",each)
        #re.sub(r'\n',"",each)
    return pure_list

#this is my write url to file function:
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
            print ur
            file.write(ur+"\r\n")
            file.flush()
            file.close()





#blew is the main function to search use bing api


def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    query = urllib.quote(query)
    #print "bing_search s query is %s" % query
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    print auth
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=100&$format=json' #&$top=5&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request.add_header('User-Agent', user_agent)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request) 
    response_data = response.read()
    json_result = json.loads(response_data)
    result_list = json_result['d']['results']
    
    return result_list
 



def usage():
    print "-----------------------------------------------------------"
    print "this is a py script to gain domains from the same ip\nusage:"
    print "example:python %s xxx.xxx.xxx" % sys.argv[0]
    print "example:python %s file.txt" % sys.argv[0]
    print "-----------------------------------------------------------"
if __name__ == "__main__":
    main()
