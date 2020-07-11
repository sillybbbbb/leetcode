#!/usr/bin/env python3
'''
    根据chrome浏览器2017年发布的新特性,
    需要unix版本的chrome版本高于57,
    windows版本的chrome版本高于58,
    才能使用无界面运行.
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest

chrome_opt = Options()      # 创建参数设置对象.
chrome_opt.add_argument('--headless')   # 无界面化.
chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.

# 创建Chrome对象并传入设置信息.
driver = webdriver.Chrome(chrome_options=chrome_opt)        
# 操作这个对象.
driver.get('https://www.baidu.com')     # get方式访问百度.
time.sleep(2)
print(driver.page_source)       # 打印加载的page code, 证明(prove) program is right.
driver.quit()   # 使用完, 记得关闭浏览器, 不然chromedriver.exe进程为一直在内存中.
