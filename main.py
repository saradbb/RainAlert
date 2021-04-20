import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


#NO PAID APT's :p

API_KEY = "fd998923a35d1256a9ad953409713678"
#Only including the hourly data
url = "https://api.openweathermap.org/data/2.5/onecall?lat=37.9480&lon=122.0608&units=metric&exclude=daily,minutely,current&appid=" + API_KEY
account_sid = "AC146bd719b7377b7751aa78879325f8b6"
auth_token = "085b7c86f8a31be1ffccf264e6b4352f"

proxy_client = TwilioHttpClient()   #For pythonanywhere hosting
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

data  = requests.get(url).json()["hourly"]
for i in range(0,12):   #Checking if it rains in the next 12 hours
    if data[i]['weather'][0]['main'] == "Rain":
        client = Client(account_sid, auth_token,http_client=proxy_client) # If it does, create a client and send text
        message = client.messages \
            .create(
            body="Bring your Umbrella",
            from_='+18305417609',
            to='+13235107659'   #Not my number
        )
        break




