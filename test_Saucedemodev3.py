from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.globalConstants import *

class Test_Odev3:
      def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

      def teardown_method(self):
        self.driver.quit()

      def test_blank_login(self):
        userNameInput=self.waitForElelemetVisible(By.ID,username_id)
        passwordInput=self.waitForElelemetVisible(By.ID,password_id)
        loginButton=self.waitForElelemetVisible(By.ID,login_button_id)
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,userNameBlank)
        actions.send_keys_to_element(passwordInput,passwordBlank)
        actions.click(loginButton)
        actions.perform() 
        errorMessage=self.waitForElelemetVisible(By.XPATH,errorMessage_blankXpath)
        assert errorMessage.text==errorMessage_blankXpath
    
      def test_blank_password_login(self):
        userNameInput=self.waitForElelemetVisible(By.ID,username_id)
        passwordInput=self.waitForElelemetVisible(By.ID,password_id)
        loginButton=self.waitForElelemetVisible(By.ID,login_button_id)
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,userName)
        actions.send_keys_to_element(passwordInput,passwordBlank)
        actions.click(loginButton)
        actions.perform() 
        errorMessage=self.waitForElelemetVisible(By.XPATH,errorMessage_blankPasswordXpath)
        assert errorMessage.text==errorMessage_blankPasswordtext
        
      def test_lockedUser_login(self):
        userNameInput=self.waitForElelemetVisible(By.ID,username_id)
        passwordInput=self.waitForElelemetVisible(By.ID,password_id)
        loginButton=self.waitForElelemetVisible(By.ID,login_button_id)
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,lokedUserName)
        actions.send_keys_to_element(passwordInput,validPassword)
        actions.click(loginButton)
        actions.perform() 
        errorMessage=self.waitForElelemetVisible(By.XPATH,errorMessage_lokedUserdXpath)
        assert errorMessage.text==errorMessage_lokedUsertext

      def test_valid_login(self):
        userNameInput=self.waitForElelemetVisible(By.ID,username_id)
        passwordInput=self.waitForElelemetVisible(By.ID,password_id)
        loginButton=self.waitForElelemetVisible(By.ID,login_button_id)
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,validUserName)
        actions.send_keys_to_element(passwordInput,validPassword)
        actions.click(loginButton)
        actions.perform()
        baslik=self.waitForElelemetVisible(By.XPATH,baslikXpath)
        assert baslik.text==baslikText
        listOfProducts=self.waitForElelemetVisible(By.XPATH,productListXpat)
        assert len(listOfProducts)==6

      
      def readInvalidDataFromExcel():
        excelFile = openpyxl.load_workbook("data\invalidLogin.xlsx")
        sheet = excelFile["Sayfa1"]
        rows = sheet.max_row #kacıncı satıra kadar benim verim var
        data = []
        for i in range(2,rows+1):
            username = sheet.cell(i,1).value # i. satır 1. sutun daki veriler
            password = sheet.cell(i,2).value #i. satır 2. sutun daki veriler
            data.append((username,password))
        return data
    
      @pytest.mark.parametrize("username,password",readInvalidDataFromExcel())  
      def test_invalid_login(self,username,password):
        userNameInput=self.waitForElelemetVisible(By.ID,username_id)
        passwordInput=self.waitForElelemetVisible(By.ID,password_id)
        loginButton=self.waitForElelemetVisible(By.ID,login_button_id)
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.click(loginButton)
        actions.perform()
        errorMesssage=self.waitForElelemetVisible(By.XPATH,errorMessage_InvalidXpath)
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMesssage.text==errorMessage_Invalidtext

    
      #Sepete başarılı bir şekilde ürün eklenmesinin testi.
      def test_addToCartProduct(self):
        userNameInput=self.waitForElelemetVisible(By.ID,username_id)
        passwordInput=self.waitForElelemetVisible(By.ID,password_id)
        loginButton=self.waitForElelemetVisible(By.ID,login_button_id)
        userNameInput.send_keys(validUserName)
        passwordInput.send_keys(validPassword)
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

      def waitForElelemetVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
  
