from selenium import webdriver
from selenium.webdriver.common.by import By #By sınıfı, Selenium WebDriver'da web sayfalarındaki belirli 
                                            #öğeleri bulmak için kullanılan stratejileri (selectors) içerir.
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
sleep (2)
input = driver.find_element(By.NAME,"q")
input.send_keys("kodlama.io")
sleep(3)
searchButton=driver.find_element(By.CLASS_NAME,"gNO89b")
sleep(2)
searchButton.click()
sleep(2) 

#Full Xpath: /html/body/div[6]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a
#Xpath: //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a
#Eğer bir attribute bulamazsak xpath'den yararlanabiliriz.Cunku yol değisebilir % 100 guvenilir diyemiyoryz.
button=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
button.click()
sleep(3)
listOfCourse = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlama.io sitesinde suan {len(listOfCourse)} adet kurs vardır.")