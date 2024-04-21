import requests
from bs4 import BeautifulSoup
import csv

number_game = int(input(f'Введите номер игры в базе: '))
name_game = str(input(f'Введите название игры: '))
wiki_link = str(input(f'Wiki_link: '))
igcd_link = str(input(f'igcd_link: '))
steamdb_link = str(input(f'steamdb_link if have game in steam, or not_link == Null : '))
license = str(f'True or False:')
print(f"INSERT INTO games "
 f"VALUES ('{name_game}', '{wiki_link}', '{igcd_link}', '{steamdb_link}')")


url = igcd_link # Замените на вашу ссылку
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
list_cars = []
all_cars = soup.findAll('div', class_="voiture mdl-card mdl-shadow--4dp")
for cars in all_cars:
    cars_good = cars.find('div', class_="mdl-card__supporting-text").find('center')
    vehicle_name = str(cars_good.contents[0]).strip()
    list_cars.append(vehicle_name)

print(list_cars)
cars_unique = list(dict.fromkeys(list_cars))
print(cars_unique)


'''
INSERT INTO cars (id_game, car_make, model, playable_vehicles, note)
VALUES (1, 'Mercedes-Benz', 'AMG ONE', true, 'This car is playable in career mode');

-- Вставляем вторую машину в таблицу cars
INSERT INTO cars (id_game, car_make, model, playable_vehicles, note)
VALUES (1, 'Aston Martin', 'Valhalla', true, 'This car is playable in quick race mode');
'''
