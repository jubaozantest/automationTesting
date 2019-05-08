# 环境安装

### 1. 安装python版本 3

### 2. git 拉取本项目 `git clone https://github.com/jubaozantest/automationTesting.git`

### 3. 安装相关包 `pip install -r requirements.txt`

### 4. 运行 python run.py


# 框架介绍： 
###            语言：python，
###            UI自动化测试框架：selenium；
###            接口测试框架：requests
###            用例组织框架：unittest
###            测试报告：HTMLTestRunner

### config
:基础数据存放，例如:被测系统URL，接口URL

#driver 
:浏览器驱动，谷歌，火狐，ie

# interface 
:接口自动化用例

# lib  
公用模块：第三方测试报告库，初始化浏览器类

# log 
储存日志文件

# pages 
页面对象元素管理，采用POM设计(page object model)

# reports 
接口和UI测试报告，

# testcases 
UI自动化测试用例管理

# util 
公共方法和装饰器

# run.py
所有UI自动化用例执行入口




