from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_SauceDemo:
    def test_blank_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        userNameInput.send_keys("")
        passwordInput.clear()
        loginButton.click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        print(errorMessage.text)
        testResult=errorMessage.text=="Epic sadface: Username is required"
        print(f"Test Sonucu: {testResult}")
    
    def test_blank_password_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        userNameInput.send_keys("İrem Balci")
        sleep(1)
        passwordInput.clear()
        loginButton.click()
        sleep(1) 
        errorMessage=driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']")
        print(errorMessage.text)
        testResult=errorMessage.text=="Epic sadface: Password is required"
        print(f"Test Sonucu: {testResult}")

    def test_lockedUser_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        userNameInput.send_keys("locked_out_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        sleep(1) 
        errorMessage=driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']")
        print(errorMessage.text)
        testResult=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu: {testResult}")

    def test_valid_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginButton=driver.find_element(By.ID,"login-button")
        userNameInput.send_keys("standard_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        sleep(2) 
        listOfProducts=driver.find_elements(By.CSS_SELECTOR,"div[class='inventory_item']")
        print(len(listOfProducts))
        testResult=len(listOfProducts)==6
        print(f"Test Sonucu: {testResult}")

 
# testClass=Test_SauceDemo()
# testClass.test_blank_login()
# sleep(2)
# testClass.test_blank_password_login()
# sleep(2)
# testClass.test_lockedUser_login()
# sleep(2)
# testClass.test_valid_login()
# sleep(2)