import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

UP = 200
DOWN = 195
CHROME_DRIVER_PATH = "C:\development\chromedriver.exe"
TWITTER_ID = "ak222xsbot"
TWITTER_PSWD = "qaz!wsx@edc#"

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_option, executable_path=CHROME_DRIVER_PATH)
# driver.get(twitter)
sleep(3)
#getting internted speed
speed_test = "https://www.speedtest.net/"



class InternetSpeedTwitterBot:

    def __init__(self, driver, up, down):
        self.driver = driver
        self.up = up
        self.down = down

    def get_internet_speed(self):

        # start_time = time.time()
        driver.get(speed_test)
        go_buttton = driver.find_element(By.CSS_SELECTOR,".start-button .js-start-test .start-text")
        go_buttton.click()
        start_time = time.time()
        sleep(50)
        speeds = driver.find_elements(By.CSS_SELECTOR,".result-container-speed .result-container-data .result-item-container .result-item .result-data span")
        self.down = speeds[0].text
        self.up =speeds[1].text
        print(self.down,self.up)
        end_time = round(time.time() - start_time)
        print(f"Time taken :{end_time}" )
        return self.down
        # driver.close()
    def tweet_at_provider(self):
        driver.get("https://twitter.com/i/flow/login")
        sleep(5)
        sign_in_field = driver.find_element(By.CSS_SELECTOR,"input")
        sign_in_field.send_keys(TWITTER_ID)
        sleep(10)
        next_button = driver.find_element(By.CSS_SELECTOR,".css-18t94o4 .css-901oao")
        next_button.click()
        sleep(5)
        button = driver.find_elements(By.CSS_SELECTOR,".css-4rbku5 .css-901oao")[6].click()
        sleep(3)
        sign_in_field = driver.find_element(By.CSS_SELECTOR,"input")

        # print('reached here')
        sleep(3)
        sign_in_field.send_keys(TWITTER_ID)
        sleep(4)
        next_button = driver.find_elements(By.CSS_SELECTOR,".css-18t94o4 .css-901oao span span")[1].click()
        sleep(3)
        pswd_field = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PSWD)
        sleep(8)
        login = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
        login.click()
        sleep(5)
        x = float(self.down)

        if x< 400 :
            typing_tweet = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div").send_keys(f"testing automation, my speed is supposed to be 200Mbps but is actually {self.down}")
            tweet_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]").click()



        # print(next_button)










bot = InternetSpeedTwitterBot(driver,UP,DOWN)
bot.get_internet_speed()

bot.tweet_at_provider()


# bot.tweet_at_provider()

