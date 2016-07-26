# -*- coding: utf-8 -*-
# 对URL进行分割
# http://www.something.com

url = raw_input("Please enter the URL: ")
domain = url[11:-4]

print "Domain name: " + domain
