from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from time import sleep


class get_data:
    def __init__(self, URL, driver):
        self.URL = URL
        self.driver = driver
        self.prices = []
        self.anchor = []
        self.addr = []
        self.final = []
        # self.HEADERS = HEADERS

    def get_property_data(self):
        # response = requests.get(url=self.URL, headers=self.HEADERS).text
        # soup = BeautifulSoup(response, "html.parser")
        # prop_list = list(soup.find(soup.find(name="ul", class_="List-c11n-8-69-2__sc-1smrmqp-0 ")).get_text())
        # print(prop_list)
        #         prices = self.driver.find_elements(By.CSS_SELECTOR."")
        self.driver.get(self.URL)
        sleep(20)
        self.prices = self.driver.find_elements(By.CLASS_NAME, "list-card-price")
        self.prices =[x.text[:6] for x in self.prices]
        self.anchor = self.driver.find_elements(By.CSS_SELECTOR, ".list-card-link")

        for element in self.anchor :
            self.final.append(element.get_attribute("href"))
        self.final = [x for x in self.final if x]
        self.final = [x for x in self.final if x.startswith("https")]
        self.final = [x for x in self.final if self.final.index(x)%2==0]
        # final = [x.text for x in self.anchor if x.text.startswith('https:')]
        sleep(5)
        self.addr = self.driver.find_elements(By.CSS_SELECTOR, ".list-card-addr")
        self.addr = [x.text for x in self.addr]
        # print(anchor_list)
        # print(address_list)
