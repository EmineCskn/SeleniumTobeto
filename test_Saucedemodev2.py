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

    
      #Sepete başarılı bir şekilde ürün eklenmesinin testi.
      def test_addToCartProduct(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))  
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        product = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")))
        actions =ActionChains(self.driver)
        actions.click(product)
        actions.perform()
        shoppingCartBadge = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        assert shoppingCartBadge.text=="1"
      #Sepete eklenen ürünün başarıyla silinmesi testi
      def test_removeProduct(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))  
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        product1 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")))
        actions =ActionChains(self.driver)
        actions.click(product1)
        actions.perform()
        shoppingCartBadge = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        shoppingCartBadge.click()
        productRemove = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "remove-test.allthethings()-t-shirt-(red)")))
        productRemove.click()
        shoppingCartBadge = WebDriverWait(self.driver,5).until(ec.invisibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        assert shoppingCartBadge
      #Satın alma işlemini başarılı bir şekilde tamamlayıp, teşekkür mesajının görüntülenmesi testi.
      def test_checkoutProduct(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))  
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton.click()
        product1 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")))
        actions =ActionChains(self.driver)
        actions.click(product1)
        actions.perform()
        shoppingCartBadge = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        shoppingCartBadge.click()
        checkoutButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutButton.click()
        firstNameBox = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        lasttNameBox = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"last-name")))
        postaCodeBox = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        firstNameBox.send_keys("Emine")
        lasttNameBox.send_keys("Coskun")
        postaCodeBox.send_keys("34854")
        continueButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"continue")))
        continueButton.click()
        finishButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"finish")))
        finishButton.click()
        messageSuccesfull = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='checkout_complete_container']/h2")))
        assert messageSuccesfull.text == "Thank you for your order!"

      
        

     
         

       