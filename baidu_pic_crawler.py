#!/usr/bin/python  
# -*- coding:utf-8 -*-  
"""
- 百度图片分类图片api



以GET形式提交，返回JSON

URL：http://image.baidu.com/data/imgs?col=&tag=&sort=&pn=&rn=&p=channel&from=1

参数：col=大类&tag=分类&sort=0&pn=开始条数&rn=显示数量&p=channel&from=1

PS：sort可以为0和1，作用。。未知

例子：http://image.baidu.com/data/imgs?col=美女&tag=小清新&sort=0&pn=10&rn=10&p=channel&from=1

- 百度图片搜索图片api

以GET形式提交，返回JSON

URL：http://image.baidu.com/i?tn=baiduimagejson&word=&pn=&rn=&ie=utf8

参数：word=关键字&pn=开始条数&rn=显示数量

PS：ie=utf8 是字符编码，但是！有时候是gb18030，所以看情况而定转码

例子：http://image.baidu.com/i?tn=baiduimagejson&word=周杰伦&pn=10&rn=10&ie=utf8
"""

import httplib  
import urllib  
import json  
import urllib2  
import re  
import os  
  
class BaiduImage(object):  
    def __init__(self):  
        super(BaiduImage,self).__init__()  
        print u'图片获取中,CTRL+C 退出程序...'  
        self.page = 60                    #当前页数  
        if not os.path.exists(r'./image'):  
            os.mkdir(r'./image')                      
      
    def request(self):  
        try:  
            while 1:  
                conn = httplib.HTTPConnection('image.baidu.com')  
                request_url ='/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&cg=girl&rn=60&pn='+str(self.page)  
                headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0','Content-type': 'test/html'}  
                #body = urllib.urlencode({'tn':'resultjsonavatarnew','ie':'utf-8','word':'%E7%BE%8E%E5%A5%B3','cg':'girl','pn':self.page,'rn':'60'})  
                conn.request('GET',request_url,headers = headers)  
                r= conn.getresponse()  
                #print r.status  
                if r.status == 200:  
                    data = r.read()  
                      
                    data = unicode(data, errors='ignore')  
                    decode = json.loads(data)  
                    self.download(decode['imgs'])  
              
                self.page += 60  
        except Exception,e:  
            print e  
        finally:  
            conn.close()  
              
    def download(self,data):  
      
        for d in data:    
            #url = d['thumbURL']   缩略图  尺寸200  
            #url = d['hoverURL']           尺寸360  
            url = d['objURL']  
            data = urllib2.urlopen(url).read()  
              
            pattern = re.compile(r'.*/(.*?)\.jpg',re.S)  
            item = re.findall(pattern,url)  
            FileName = str('image/')+item[0]+str('.jpg')  
              
            with open(FileName,'wb') as f:  
                f.write(data)  
      
if  __name__ == '__main__':  
    bi = BaiduImage()  
    bi.request()  