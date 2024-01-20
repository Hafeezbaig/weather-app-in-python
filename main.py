import requests
import json

city = input("Enter the Name of the City : ")
url = "https://api.weatherapi.com/v1/current.json?key=dc32cac418a7443e801112522242001&q={city}"
r=requests.get(url)
# print(r.text)
weather = json.loads(r.text)
print("Current Weather Details for",city)
print("Region:", weather["location"]["region"])
print("Latitute:", weather["location"]["lat"])
print("Longitute:", weather["location"]["lon"])
print("Local time for",city,":" ,weather["location"]["localtime"])
print("Temperature in Celsius :", weather["current"]["temp_c"])
print("Temperature in Farenheit :", weather["current"]["temp_f"])


