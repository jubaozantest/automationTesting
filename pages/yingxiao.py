from selenium.webdriver.common.by import By

class ManJianManSong:
    manjianmansong_link = (By.XPATH, "//li/p[text()='满减满送']",'满减满送链接入口')
    add_button = (By.XPATH, '//*[@id="add"]','添加按钮')
    huodongmingcheng_input=(By.XPATH, "//input[@placeholder='请输入活动名称']",'活动名称输入框')
    shengxiaoshijian_input =(By.XPATH,'//*[@id="startTime"]','生效时间')

