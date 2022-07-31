import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep



email = "aryennh.kulkarni22@gmail.com"
chrome_web_driver = "C:\development\chromedriver.exe"

job_to_search = "Python Intern"




chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
chrome_option.add_argument("start-maximized")
driver =  webdriver.Chrome(options=chrome_option,executable_path=chrome_web_driver)
driver.get("https://www.linkedin.com")


email_input = driver.find_element(By.CSS_SELECTOR," #session_key")
email_input.send_keys(email)
passwd_input = driver.find_element(By.CSS_SELECTOR,"#session_password")
passwd_input.send_keys(password)
submit = driver.find_element(By.CSS_SELECTOR,".sign-in-form__submit-button")
submit.click()

sleep(5)
navbar = driver.find_elements(By.CSS_SELECTOR,".global-nav__primary-item")
job_portal = navbar[2].click()

#reached job portal page
sleep(4)
job_search = driver.find_element(By.CSS_SELECTOR,".jobs-search-box__input .jobs-search-box__inner .jobs-search-box__text-input")
job_search.send_keys(job_to_search)
# job_location = driver.find_element(By.CSS_SELECTOR,".jobs-search-box__input .jobs-search-box__inner")
# job_location.send_keys("Bengaluru")
# job_location.click()
job_search.send_keys(Keys.SPACE)
job_search.send_keys(Keys.ENTER)
sleep(5)
# job_search.send_keys(Keys.ENTER)
# job_search.send_keys(Keys.SPACE)


sleep(10)
easy_apply = driver.find_element(By.CSS_SELECTOR,".search-reusables__filter-list .search-reusables__primary-filter .search-reusables__filter-binary-toggle").click()
sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-apply-button--top-card .jobs-apply-button").click()
sleep(5)
phone_number = driver.find_element(By.CSS_SELECTOR,".display-flex input").send_keys(PHONE)
sleep(5)
submit_button = driver.find_element(By.CSS_SELECTOR,"footer .display-flex button").click()
# if submit_button.get_attribute("aria-label") == "Submit application":
#     submit_button.click()

