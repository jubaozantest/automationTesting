from selenium.webdriver.common.by import By

class ManJianManSong:
    manjianmansong_link = (By.XPATH, "//li/p[text()='满减满送']",'满减满送链接入口')
    add_button = (By.XPATH, '//button[@id="add"]','添加按钮')
    huodongmingcheng_input=(By.XPATH, "//input[@placeholder='请输入活动名称']",'活动名称输入框')
    shengxiaoshijian_input =(By.XPATH,'//*[@id="startTime"]','生效时间')
    kaishishijian=(By.XPATH,'//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[2]/td[5]','开始时间')
    jiesushijian=(By.XPATH,'//*[@id="layui-laydate1"]/div[2]/div[2]/table/tbody/tr[2]/td[4]','结束时间')
    confirm=(By.XPATH,"//*[text()='确定' and @class='laydate-btns-confirm']",'确定时间')
    youhuishezhi_input=(By.XPATH,"//input[@name='conditionNum-0']","优惠设置")
    jianxianjin_radio=(By.XPATH,"//*[@title='减现金']/..//i","减现金")
    jianxianjin_input=(By.XPATH,"//*[@name='reductionMoney-0']","减现金输入框")
    baocun_button=(By.XPATH,"//button[text()='保存']","保存按钮")