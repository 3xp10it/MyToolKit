<p>MyToolKit</p>

<p>1.本工具包括6个模块：
  easy_search.py,
  my_bing_domains_v1_alone.py,
  my_GoogleScraper_bing_domain.py,
  mysqlmap.py,
  MyToolKit.py,
  mail.py</p>

<p>2.各模块介绍：</p>

<p>1&gt;easy_search.py： 
  google关键字搜索相关网页结果，并对结果通过sqlmap注入，类似啊D里的搜索注入功能，但
  比啊D里强大，因为这里用sqlmap检测注入并注入,其中google搜索的功能采用完全模仿浏览
  器方式，可得到所有通过浏览器Google搜索的结果，通过GoogleScraper模块实现，其中Goog
  leScraper利用Selenium模块模拟浏览器人工访问功能。</p>

<p>2&gt;my_bing_domains_v1_alone.py：<br>
  通过bing的api接口原理实现，需要注册bing的api_key，每个月免费5000次。</p>

<p>3&gt;my_GoogleScraper_bing_domain.py:
  通过GoogleScraper的浏览器模拟人工访问bing，关键字ip：111.111.111.111,
  获取所有结果,当只有一页结果 时，GoogleScraper不能得到该查询结果，调用上面的
  my_bing_domains_v1_alone.py模块继续查询。</p>

<p>4&gt;mysqlmap.py：
  sqlmap自动化sqli模块，详情见代码。</p>

<p>5&gt;MyToolKit.py：
  综合入口模块，选择不同需求，实现不同功能。共包括8个功能，分别为：
  --exp:
   批量使用exp功能 
  --mygoogle 
            --sqlmap-crawl：
              使用my_GoogleScraper_bing_domain.py模块和sqlmap的crawl功能实现批量
              自动化sqli
            --sqlmap-g-nohuman：
              使用my_GoogleScraper_bing_domain.py模块和sqlmap的-g选项功能实现批量
              自动化sqli。
            --sqlmap-g-human：
              使用my_GoogleScraper_bing_domain.py模块和可绕过验证码的GoogleScrape
              r,人工输入验 证码，获取所有url,用sqlmap的-m选项功能实现批量自动化sql
              i.
  --mybing
            --sqlmap-crawl：
              使用my_bing_domains_v1_alone.py模块和sqlmap的crawl功能实现批量自动化sqli。
            --sqlmap-g-nohuman：
              使用my_bing_domains_v1_alone.py模块和sqlmap的-g选项功能实现批量自动
              化sqli。
            --sqlmap-g-human：
              使用my_bing_domains_v1_alone.py模块 和可绕过验证码的 GoogleScraper,
              人工输入验证码，获取所有url,用sqlmap的-m选项功能实现批量自动化sqli.
  --easy_search：
    相当于--mygoogle下的--sqlmap-g-uman功能的子功能,但灵活性更强,可任意关键字googl
    e搜索并利用sqlmap注入。 最常用功能应该是--mygoogle下的--sqlmap-g-human及--easy
    _search这两个。
6&gt;mail.py:
  自动发送邮件，内嵌在MytoolKit.py中.</p>

<p>3.环境要求： 
  安装GoogleScraper（python3下），并修改部分GoogleScraper中第三方模块selenium中代
  码(绕过验证码)可参考以前一篇写的关于google search api for python的文章.90sec链接
  <a href="https://forum.90sec.org/forum.php?mod=viewthread&amp;tid=9024">https://forum.90sec.org/forum.php?mod=viewthread&amp;tid=9024</a> 度网盘链接：
  <a href="http://pan.baidu.com/s/1kUklzZD">http://pan.baidu.com/s/1kUklzZD</a> 密码: 4cpn</p>

<p>2016.1.26部分代码更新</p>

<p>2016.1.28部分代码更新
1.添加tor匿名功能，可自由选择tor或不用tor</p>

<p>2016.1.28部分代码更新，增加功能：
1.绕过“多次错误访问后屏蔽所有请求”
2.请求延时
3.尝试绕过waf
4.支持post注入</p>

<p>2016.1.29部分代码更新，增加功能：
1.定位旁站的sqli所在主站
2.发送邮件通知功能，将可用sqli的url发送邮件通知（smtp用163）</p>

<p>2016.3.2部分代码更新：
1.easy_search.py line:116 添加自动结束冗余firefox进程功能 
2.修改mysqlmap.py中line:131-161的逻辑错误 
3.修改其它py中fp=open()以后没有fp.close()的错误 
4.修改MyToolKit.py中对easy_search.py调用的逻辑错误 
5.关键字由php|asp变成php|asp|aspx|jsp 
6.修改my_bing_domains_v1_alone.py中get_the_one_targe_domains函数使用遇到不工作的
  域名解析异常使全局出错的错误 line:21-22 
7.自动处理output目录移动，使得运行前不必清空output目录
8.修改my_bing_domains_v1_alone.py中get_the_one_targe_domains函数</p>
</article></body></html>
