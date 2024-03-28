from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest

class Test_Odev2:
      def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

      def teardown_method(self):
        self.driver.quit()

      def test_blank_login(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"")
        actions.send_keys_to_element(passwordInput,"")
        actions.click(loginButton)
        actions.perform() 
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text=="Epic sadface: Username is required"
    
      def test_blank_password_login(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"Ahmet Suat Tanis")
        actions.send_keys_to_element(passwordInput,"")
        actions.click(loginButton)
        actions.perform() 
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text=="Epic sadface: Password is required" 
        

      def test_lockedUser_login(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"locked_out_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.click(loginButton)
        actions.perform() 
        errorMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."

      def test_valid_login(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.click(loginButton)
        actions.perform()
        baslik=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//div[@class='app_logo']")))
        assert baslik.text=="Swag Labs"
        listOfProducts=self.driver.find_elements(By.CSS_SELECTOR,"div[class='inventory_item']")
        print(len(listOfProducts))
        assert len(listOfProducts)==6

      def getData():
        return [("ahmet","12345"),("naber","5341231"),("Ahmet Suat Tanis","secret_sauce")]

    
      @pytest.mark.parametrize("username,password",getData())  
      def test_invalid_login(self,username,password):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.click(loginButton)
        actions.perform()
        errorMesssage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMesssage.text=="Epic sadface: Username and password do not match any user in this service"

    
      def test_addToCartProduct(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.click(loginButton)
        actions.perform()
        item=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"add-to-cart-sauce-labs-bike-light")))
        item.click()
        cartButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,".shopping_cart_badge")))
        cart_button_text=cartButton.text
        print("Cart Button Text:", cart_button_text)
        assert cartButton.text=="1"

      def test_removeProductFromCart(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.click(loginButton)
        actions.perform()
        item1=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"add-to-cart-sauce-labs-bike-light")))
        item1.click()
        item2=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack")))
        item2.click()
        cartButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//span[@class='shopping_cart_badge']")))
        cartButton.click()
        removeButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#remove-sauce-labs-bike-light")))
        removeButton.click()
        cartButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//span[@class='shopping_cart_badge']")))
        assert cartButton.text=="1"

      def test_checkoutProduct(self):
        userNameInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        sleep(1)
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        sleep(1)
        actions.click(loginButton)
        actions.perform()
        item1=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,"add-to-cart-sauce-labs-bike-light")))
        item1.click()
        sleep(1)
        item2=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack")))
        item2.click()
        cartButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//span[@class='shopping_cart_badge']")))
        cartButton.click()
        sleep(1)
        checkoutButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutButton.click()
        firstName=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        lastName=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"last-name")))
        zipCode=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        continueButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"continue")))
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(firstName,"Yasemin")
        sleep(1)
        actions.send_keys_to_element(lastName,"Beyaz")
        sleep(1)
        actions.send_keys_to_element(zipCode,"34212")
        sleep(1)
        actions.perform()
        continueButton.click()
        finishButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"finish")))
        sleep(1)
        actions.click(finishButton)
        actions.perform()
        orderConfirmMessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//h2[@class='complete-header']")))
        assert orderConfirmMessage.text=="Thank you for your order!"
    

      
        

     
         

       