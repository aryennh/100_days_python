import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

#SETUP -
CHROME_DRIVER_PATH = "C:\development\chromedriver.exe"
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_option, executable_path=CHROME_DRIVER_PATH)
##

INSTAGRAM = "https://www.instagram.com/"
EMAIL = "aryennh.kulkarni22@yahoo.com"
PSWD = "UNtYAP3F3yQUVVc"
HOST = "buzzfeedtasty"

driver.get(INSTAGRAM)

class instagram_follower_bot :
    def __init__(self,account):
        self.account = account

    def login(self):
        sleep(3)
        input_fields = driver.find_elements(By.CSS_SELECTOR,".-MzZI ._9GP1n   .f0n8F input")
        email_field = input_fields[0]
        email_field.send_keys(EMAIL)
        password_field = input_fields[1]
        password_field.send_keys(PSWD)
        sleep(5)
        login_button = driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        login_button.click()



    def find_host_account(self):
        search_box = driver.find_element(By.CSS_SELECTOR,".MWDvN .QY4Ed input")
        search_box.send_keys(HOST)
        sleep(1)
        search_box.send_keys(Keys.ENTER)
        search_box.send_keys(Keys.ENTER)




    def send_requests(self):
        followers = driver.find_elements(By.CSS_SELECTOR,"._aa_7 ._aa_5")[1]
        followers.click()
        sleep(3)
        ppl = driver.find_elements(By.CSS_SELECTOR,"._acan ")
        ppl = ppl[2:]
        for i in ppl :
            print(i.text)
            i.click()
            sleep(1)
        sleep(3)

x = instagram_follower_bot(EMAIL)


x.login()
sleep(5)
x.find_host_account()
sleep(5)
x.send_requests()