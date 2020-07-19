import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json
    text=f'Confirmed Cases :{data["cases"]} \nDeaths: {data["deaths"]} \nRecovered: {data["recovered"]}'
    