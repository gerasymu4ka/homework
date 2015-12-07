#get weather forecast for now and compare it with one stored in forecast5.py 
#write comparisons to compare_forecast.txt

import pickle
from datetime import datetime, date
import json
import urllib2

#get url weather at the moment
weather_now = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Lviv,uk&units=metric&appid=2de143494c0b295cca9337e1e96b00e0').read()

#convert json to unicode
converted = json.loads(weather_now)

#date and time now
now = datetime.now()
dt = str(now)

with open('compare_forecast.txt', 'a') as cf:
    
    dtt = {}                        #dtt means date time temperature
    dtt['date time'] = dt[:19]
    dtt['temperature'] = converted['main']['temp']
    
    cf.writelines('Weather now: ' + '\n')
    cf.writelines(str(dtt))
    cf.writelines('\n')
    
    with open('forecast5.txt', 'r') as f5:
        cf.writelines('Temperature predicted for today: ' + '\n')
        for line in f5:
            if str(now.date()) in line:
                cf.writelines(line)


                    
        
    









    







