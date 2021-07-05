import requests
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

def API(CITY):
    user_api = "722278b2860571acd63e219de61d4fe1"
    location = CITY
    endpoint = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api+"&units=metric"
    r = requests.get(endpoint)
    temp = r.json()['main']['temp']
    return temp

def selenium(CITY):
    drivpath = os.getcwd()
    PATH = drivpath+"\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get("https://weather.com/")
    time.sleep(5)
    inputElement = driver.find_element_by_id("LocationSearch_input")
    inputElement.send_keys(CITY)
    time.sleep(3)
    inputElement.send_keys(Keys.RETURN)
    EWSStatus = driver.find_elements_by_xpath("/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/span")[0].text
    st=""
    for i in EWSStatus:
        if (i=="°"):
            pass
        else:
            st=st+i
    st=int(st)
    return st

def City_varience(val1,val2,Varience):
    if val2>val1:
        difnum=((val2-val1)/val1)*100
    elif val1>val2:
        difnum=((val1-val2)/val2)*100
    else:
        difnum=0
    print(difnum)
    if difnum>Varience:
        return 0
    else:
        return 1

if __name__ == '__main__':
    f = open('Climate.json',)
    data = json.load(f)
    City=data['Country_City_Name']
    Varience=float(data['Varience'])
    val1=float(API(City))
    val2=float(selenium(City))
    result=City_varience(val1,val2,Varience)
    if result==1:
        print("success Match")
    else:
        print("Matcher Exception")
