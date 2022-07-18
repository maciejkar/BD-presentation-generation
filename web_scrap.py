from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from PIL import Image
from time import sleep
import numpy as np
import json
import os

def true_time_to_time(scrap_time : str , mul : float ):  
    """Czas zeskrapowany w formacie hh:mm 'h' zminia na sa hh 'h' mnożąc czas przes zdefiniowaną stałą np 
    4:47 h zmienia na 6 h dla stałej wynoszącej 1.2"""
    time = scrap_time[:-2]
    return str(round((int(time[0]) + int(time[2:4])/60) * mul )) + ' h'

def scrap(path):
    # 1. Ręcznie stworzyć C:\Program Files\Google\GoogleUpdater"
    # 2. Zainstalować chrome beta 104 
    # if not os.path.exists("C:\Program Files\Google\GoogleUpdater"): Ręcznie stworzyć
    #     os.makedirs("C:\Program Files\Google\GoogleUpdater")

    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument("headless")
    options.binary_location="C:\Program Files\Google\Chrome Beta\Application\chrome.exe"

    # 2
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='104.0.5112.20').install()), options=options)

    with open('settings.json',"r", encoding="utf-8") as f:
        settings = json.load(f)
    log_path = 'https://mapa-turystyczna.pl/login'
    

    print("---------------------------------")
    driver.get(log_path)

    #accept cookies
    sleep(1)
    driver.find_element(By.CLASS_NAME,'fc-button-label').click()


    #login 
    driver.find_element(By.NAME,"signin[username]").send_keys(settings["login"]) 
    driver.find_element(By.NAME,"signin[password]").send_keys(settings["password"]) 
    driver.find_element(By.CSS_SELECTOR,'.mdl-button--primary.mdl-button--primary.mdl-button--raised').click()
    sleep(3)


    print(os.getcwd())
    driver.get(path)

    # get html code to scrap data such as distance
    html = driver.page_source



    soup = BeautifulSoup(html,'html.parser')
    heightest_point =soup.find('div', class_='ts-user-activity__data-inline-item').get_text()[25:].replace('\n','').replace('\t','').replace(',',', ')
    index = heightest_point.find(', ')
    max_height = int(heightest_point[index+2:index + 6])
    data = soup.find_all("span", class_= 'ts-user-activity__data-item-value ts-user-activity__data-item-value--primary')
    distance = data[0].get_text().strip()
    true_time = data[1].get_text().strip()
    up = data[2].get_text().strip()
    down = data[3].get_text().strip()

    profil_json= json.loads(soup.find('div', class_="ts-user-activity__profile ts-profile-container").attrs["data-profile"])

    min_height = 2000
    for dict in profil_json['segments']:
        # print(dict)
        temp = dict['elevation']
        if temp < min_height:
            min_height = temp


    elevation = f'{int(max_height - min_height)} m'

    print(os.getcwd())
    if os.path.exists('data.json'):
        with open('data.json','r',encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}
        data['level'] = None
        data['name_of_route'] = None
        data['leader'] = None

    data['distance'] = distance
    data['heightest_point'] = heightest_point
    data['elevation'] = elevation
    data['up'] = up
    data['down'] = down
    data['time'] = true_time_to_time(true_time,settings['time_multiplier'])

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    #go to proile and save it 
    driver.get(path + '/profile')
    sleep(1)
    select = Select(driver.find_element(By.ID,'profile-size-type'))
    select.select_by_visible_text('Szeroki')
    driver.find_element(By.ID,'ts-ep-static').screenshot('zdjecie.png')
    driver.close()

    # cover time in profile
    img= Image.open('zdjecie.png')
    im = np.array(img)
    im[0:65,0:400] = [255, 255, 255, 255]
    Image.fromarray(im).save('zdjecie.png')

if __name__ == '__main__':
    scrap(path ='https://mapa-turystyczna.pl/account/route/1391934')






