import requests
import json
city = input("Enter Your City: ")
url = f"https://api.weatherapi.com/v1/current.json?key=083c6737582d4c5abf223411231107&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
print(f"The Temperature of {city} is:",wdic["current"]["temp_c"])