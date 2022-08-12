import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class fill_form:
    def __init__(self,URL,driver,addr,prices,links):
        self.driver = driver
        self.URL = URL
        self.addr = addr
        self.prices = prices
        self.links = links


    def auto_form(self):
        for i in range(len(self.prices)):
            self.driver.get(self.URL)
            sleep(3)
            addr_field = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            price_field = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link_field = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            submit_button = self.driver.find_element(By.CSS_SELECTOR,".l4V7wb")
            addr_field.send_keys(self.addr[i])
            price_field.send_keys(self.prices[i])
            link_field.send_keys(self.links[i])
            submit_button.click()




