from selenium.webdriver.common.by import By



class LoginPage:
    username_input = (By.XPATH, "//*[@id='use_name']",'用户名输入框')
    pwd_input = (By.XPATH, "//*[@id='use_pwd']",'密码输入框')
    login_button=(By.XPATH, "//input[@value='登录']",'登录按钮')


