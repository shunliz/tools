﻿#!/usr/bin/python  
# -*- coding:utf-8 -*-  
import httplib  
import urllib  
import json  
import urllib2  
import re  
import os
import pdb
  
class BaiduImage(object):  
    def __init__(self):  
        super(BaiduImage,self).__init__()  
        print u'图片获取中,CTRL+C 退出程序...'  
        self.page = 60
        #当前页数  
        if not os.path.exists(r'./image'):  
            os.mkdir(r'./image')                      
      
    def request(self):  
        try:  
            while 1:	
                #pdb.set_trace()			
                conn = httplib.HTTPConnection('image.baidu.com')  
                #request_url ='/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&cg=girl&rn=60&pn='+str(self.page)
                request_url ='/data/imgs?col=%E7%BE%8E%E5%A5%B3&tag=%E5%B0%8F%E6%B8%85%E6%96%B0&sort=0&rn=60&p=channel&from=1&pn='+str(self.page)  
                #headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0','Content-type': 'text/html'}  
                headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36','Content-type': 'text/html'}  
                #body = urllib.urlencode({'tn':'resultjsonavatarnew','ie':'utf-8','word':'%E7%BE%8E%E5%A5%B3','cg':'girl','pn':self.page,'rn':'60'})  
                conn.request('GET',request_url,headers = headers)  
                r= conn.getresponse()  
                #print r.status  
                if r.status == 200:  
                    data = r.read()  
                      
                    data = unicode(data, errors='ignore')  
                    decode = json.loads(data)
                    for i in range(len(decode['imgs'])-1):
                        self.download(decode['imgs'][i]['downloadUrl'])  
              
                self.page += 60  
        except Exception,e:  
            print e  
        finally:  
            conn.close()  
              
    def download(self,url):   
		data = urllib2.urlopen(url).read()  
		  
		pattern = re.compile(r'.*/(.*?)\.jpg',re.S)  
		item = re.findall(pattern,url)  
		FileName = str('image/')+item[0]+str('.jpg')  
		  
		with open(FileName,'wb') as f:  
			f.write(data)  
      
if  __name__ == '__main__':  
    bi = BaiduImage()  
    bi.request()  