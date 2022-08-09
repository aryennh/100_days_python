from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

TOP = 10
BOTTOM = 150
driver= "C:\web_drivers\chromedriver\chromedriver_win32"
SPEEDTEST_URL = "https://www.speedtest.net/result/13462611945"

response = requests.get(url=SPEEDTEST_URL).text

class InternetSpeedTwitterBot:
    def __init__(self,driver,down,up):
        self.driver = "C:\web_drivers\chromedriver\chromedriver_win32"
        self.down = BOTTOM
        self.up = TOP

    def get_internet_speed(self):


    def tweet_at_provider(self):

bot = InternetSpeedTwitterBot(CHROME_DRIVER,BOTTOM,TOP)
bot.get_internet_speed()
bot.tweet_at_provider()