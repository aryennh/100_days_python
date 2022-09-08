import requests as rq
from twilio.rest import Client
#CONSTANTS ->
STOCK = "TSLA"
COMPANY_NAME = "TSLA"

# API KEYS
# twilio_api = "dd290dee9667284e3181e95a22c3f714"
account_ssid = "ACa7b062a3d77906a5de81fb2196713d45"
auth_token = "d6c83676c38213b7a0ae16a2047ba019"
api_key_stock = "YKCKVMVJVEPFYB7P"
news_endpoint = "https://newsapi.org/v2/everything?q=TSLA&apiKey=ce2bf1a86dff4134889abb682e7d9d19"


# TODO 1. Get stock prices for a week, check for 5% increase or decrease
# TODO 2. get news for company
# TODO 3. send messages

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

source = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=YKCKVMVJVEPFYB7P'
data_params = {
    'fucntion': "TIME_SERIES_WEEKLY",
    'symbol': 'TSLA',
    'api_key': "YKCKVMVJVEPFYB7P",

}

data_json = rq.get(source,params=data_params).json()
weekly_time_series = data_json['Time Series (Daily)']
closing_price = [float(value['4. close']) for (key, value) in weekly_time_series.items()]
final = closing_price[:7]

news_params = {

    'q': COMPANY_NAME,
}
ans = []
for i in range(1, 6):
    if final[i] > final[i - 1] * 105 / 100 or final[i] < final[i + 1] * 105 / 100:
        news1 = rq.get(news_endpoint, params=news_params).json()['articles'][0]['title']
        news2 = rq.get(news_endpoint, params=news_params).json()['articles'][1]['title']
        news3 = rq.get(news_endpoint, params=news_params).json()['articles'][2]['title']
        ans = [news1, news2, news3]
        break
print(ans)
client= Client(account_ssid,auth_token)
print("IS IT WORKING -2 ")
message = client.messages \
    .create(
    messaging_service_sid='MG0f02b1b8de4ab25e79e8c777cc33f116',
    body= news1,
    from_='+18453828042',
    to='+919673401786',
)
# print('\n'.join(ans))
print(message.sid)
print(message.status)
