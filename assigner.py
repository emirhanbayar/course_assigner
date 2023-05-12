import time
import os
from selenium import webdriver
from get_chrome_driver import GetChromeDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Eba:
    def __init__(self,username, password):
        self.browser = webdriver.Chrome("chromedriver")
        self.username = username
        self.password = password
        self.acts = ActionChains(self.browser)
    
    def logIn(self):
        self.browser.get("https://giris.eba.gov.tr/EBA_GIRIS/teacher.jsp")
        time.sleep(1)
        self.browser.find_element(By.XPATH, "//*[@id='teacher']/div/button[2]").click()
        usernameInput = self.browser.find_element(By.XPATH, "//*[@id='tridField']")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='egpField']")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div[2]/input[4]").click()
        time.sleep(10)
    
    def Assign(self, ders):
        self.browser.get("https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.861/index.html#/main/editExternalLiveSession")
        time.sleep(20)
        # self.browser.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input').send_keys(ders[0])
        self.browser.find_element(By.XPATH,  '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input').send_keys(ders[0])
        # self.browser.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/select').send_keys(ders[1][0])
        self.browser.find_element(By.XPATH,  '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/select').send_keys(ders[1][0])
        # self.browser.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/p/input').send_keys(Keys.ARROW_DOWN)
        self.browser.find_element(By.XPATH,  '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[3]/p/input').send_keys(Keys.ARROW_DOWN)
        ders[2] = int(ders[2])
        while(ders[2] > 0):
            self.browser.switch_to_active_element().send_keys(Keys.ARROW_RIGHT)
            ders[2] -= 1
        self.browser.switch_to_active_element().send_keys(Keys.ENTER)
        #time.sleep(20)
        # self.browser.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[8]/select').send_keys("z")
        self.browser.find_element(By.XPATH,  '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[8]/select').send_keys("z")
        # self.browser.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[9]/input').send_keys(ders[3])
        self.browser.find_element(By.XPATH,  '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[9]/input').send_keys(ders[3])
        # self.browser.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[10]/input').send_keys(ders[4])
        self.browser.find_element(By.XPATH,  '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[10]/input').send_keys(ders[4])
        time.sleep(20)
        # self.browser.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div').click()
        self.browser.find_element(By.XPATH,  '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div').click()
        time.sleep(2)
        # self.browser.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[2]/div[2]/div[2]/div').click()
        self.browser.find_element(By.XPATH,  '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[2]/div[2]/div[2]/div').click()



if __name__ == "__main__":

    print("Chrome Driver Kontrol Ediliyor...")
    if not os.path.isdir("chromedriver"):
        print("Chrome Driver Bulunamadı. İndiriliyor...")
        get_driver = GetChromeDriver()
        get_driver.install()
        print("Chrome Driver İndirildi.")
    else:
        print("Chrome Driver Bulundu.")

    username = input("Kullanıcı adınız: ")
    password = input("Şifreniz: ")

    print("Giriş yapılıyor...")
    eba = Eba(username,password)
    eba.logIn()

    print("Dersler atanıyor...")
    file = open('DersProgram.txt')
    ders = file.readlines()
    while ders:
        ders = ders[0]
        eba.Assign(eval(ders))
        ders = file.readlines()