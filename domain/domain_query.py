#! encoding: utf-8
'''
Created on 2017年11月30日

@author: niushuai
'''
import urllib2
from urllib2 import URLError
query_url = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={domain}'

if __name__ == '__main__':
    # 从文件中读取要查询的域名
    with open('domain.txt') as f:
        lines = f.readlines()
    for line in lines:
        print(line.strip('\n'))
    url = query_url.format(domain="niushuai.com")
    # 从接口中查询指定的域名
    try:
        response = urllib2.urlopen(url)
        if response.code == 200:
            data = response.read()
            if '<original>210' in data:
                print('可以注册！')
            else:
                print('不能注册')
    except URLError, e:
        print('We failed to reach a server.')  
        print('Reason: ', e.reason)
    
    print("end")