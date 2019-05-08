from selenium.webdriver.common.by import By



class LoginPage:
    username_input = (By.XPATH, "//*[@id='use_name']")
    pwd_input = (By.XPATH, "//*[@id='use_pwd']")
    login_button=(By.XPATH, "//*[contains(text(),'登录')]")


