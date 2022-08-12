from selenium import webdriver
from time import sleep
from get_list import get_data
from auto import fill_form
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER_PATH = "C:\development\chromedriver.exe"


driver_service = Service(executable_path=CHROME_DRIVER_PATH)

WEB_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
          "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122" \
          ".17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible" \
          "%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22" \
          "%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22" \
          "%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse" \
          "%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max" \
          "%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C" \
          "%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D "
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScanfN5zg6a0rgc_xkoOKdQtFBO5J2JFBIlg0Hjn8sFQq-N8w/viewform"

# options = Options()
# options.add_argument("start-maximized")
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options,
#                           executable_path=CHROME_DRIVER_PATH)


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

options.add_argument('window-size=1440,1440')
driver = webdriver.Chrome(service=driver_service,options=options,executable_path=CHROME_DRIVER_PATH)

# driver.get(WEB_URL)

data = get_data(WEB_URL, driver)
data.get_property_data()
prices = data.prices
addresses = data.addr
# links = [i.text for i in data.anchor]
links = data.final
print(prices)
print(addresses)
print(links)
# driver.get(FORM_URL)
# sleep(10)
form = fill_form(FORM_URL,driver,addresses,prices,links)
form.auto_form()

print(len(prices),len(data.addr),len(data.anchor))
print(data.anchor)
print(data.final)
print(len(data.final))
