#schedule to run the file each 5 day to get weather forcast for the next 5 days.
#append data to file.

import pickle
from datetime import datetime
import json
import urllib2

#get url weather 5 days
forecast5 = urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=Lviv,us&units=metric&mode=json&appid=2de143494c0b295cca9337e1e96b00e0').read()

#convert json to unicode
converted5 = json.loads(forecast5)

#get temperature and time for every 3 hour
all_list = converted5.get('list')

i = 0
with open('forecast5.txt', 'a') as f:
    now = datetime.now()
    f.writelines(str(now.ctime() + '\n'))
    
    while i < len(all_list):
        dtt5 = {}                   #dtt means date time temperature for 5 days
        m = all_list[i].get('main')
        dtt5['temperature'] = m.get('temp')
        dtt5['date time'] = all_list[i].get('dt_txt')

        i += 1
        f.writelines(str(dtt5) + '\n')
    f.writelines('\n')
