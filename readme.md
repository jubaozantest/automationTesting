# 自研接口和UI一体化的自动化测试框架:jubaozantest Version:1.0

## 环境安装

######  1. 安装python版本3,安装IDE-pycharm，谷歌浏览器

######  2. git 拉取本项目 `git clone https://github.com/jubaozantest/automationTesting.git`

######  3. 安装相关依赖包 `pip install -r requirements.txt`

######  4. 运行 python run.py运行所有UI自动化测试用例；python run_interfaceCase.py运行所有的接口自动化测试用例


##  框架介绍： 
######           语言：python，
######            UI自动化测试框架：selenium；
######            接口测试框架：requests
######            用例组织框架：unittest
######            测试报告：HTMLTestRunner
######            日志模块：logging
######            数据驱动：ddt
######            UI页面对象管理模式：POM

##  实现功能
###   接口自动化用例
######   封装requests请求方法
######   请求logging日志文件记录
######   单接口测试
######   多接口关联实现串场景接口测试
######   unittest+ddt数据驱动模式，批量执行用例
######   参数可数据驱动
######   支持数据库校验
######   生成excel报告和HTMLTestRunner可视化的html报告


###  功能UI自动化用例
######  封装selenium常用方法
######  页面对象管理采用POM设计，页面元素可重复使用
######  用例批量执行
######  HTMLTestRunner生成可视化的html报告


##  项目结构
### config
######   1.基础数据存放，例如:被测系统URL，接口URL前缀，
######   2.接口用例提取变量存放
######   3.接口测试用例excel表和excel报告

### driver 
######   1.UI自动化的浏览器驱动，例如：谷歌，火狐，ie


### lib  
######  1.读取congif模块数据方法；
######  2.第三方测试报告库；
######  3.UI自动化初始化浏览器方法;

### log 
###### 1.日志记录方法
###### 2.储存logging日志文件

### pages 
######  UI自动化页面对象元素管理，采用POM设计(page object model)

### reports 
######  存放接口和UI可视化html测试报告，

### testcases 
######  所有UI自动化测试用例管理

### testcasesInterface 
######  组装所有接口自动化用例(config中的excel文件)

### util 
###### 1.default_path:相关文件默认的相对路径
###### 2.HTTPClient:封装requests请求
###### 3.query_mysql:查询数据库，用于用例结果校验
###### 4.operation_excel:读写excel方法
###### 5.tool:接口测试结果校验方法等
###### 6.wrappers:装饰器

### run.py
###### 所有UI自动化用例执行入口

### run_interfaceCase.py
###### 所有接口自动化用例执行入口

### requirement.txt
######  所有依赖安装包


#  待优化完善功能
###  1.优化用例结果校验方式
###  2.UI自动化分布式执行
###  3.Jenkins/Docker 自动化用例可持续集成



## 编写测试用例规范
###接口用例
#####  1.excel文件每一行代表一个接口测试用例:字段说明
#####         接口用例名称(必填，例如：1.登录-验证码登录)
#####         接口请求方式（必填,例如：post,put）
#####         接口url(必填,例如：https://u.jubaozan.cn/auth/login)
#####         请求头信息(非必填,例如:{"x-c3-site": "1123","x-c3-token": "{{token}}",})
#####         请求入参(非必填,例如{"numIid": 10086})
#####         提取变量（非必填,例如：token,提取token,其它接口使用该变量:{{token}}）
#####         请求响应值(用例运行完自动生成)
#####        检查点（必填,例如{"success":True}）
#####        用例运行结果(用例运行完自动生成)
#####  2.运行run_interfaceCases会运行所有用例，生成excel报告和html报告   


###  测试报告效果图展示
![Image text](https://github.com/jubaozantest/automationTesting/blob/master/picture/111.png)
![Image text](https://github.com/jubaozantest/automationTesting/blob/master/picture/222.png)
![Image text](https://github.com/jubaozantest/automationTesting/blob/master/picture/333.png)
###### 接下来就能编写接口/UI自动化测试用例！！！


