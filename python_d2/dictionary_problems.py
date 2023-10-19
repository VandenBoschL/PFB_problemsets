#!/usr/bin/env python3


favs_dict = {"book": "Green Grass, Running Water",
	"song":"Lauv - I Like Me Better",
	"tree":"Evergreen"}

print(favs_dict['book'])

fav_obj = 'book'
print(favs_dict[fav_obj])

print(favs_dict["tree"])

favs_dict['organism'] = "Hapalochlaena"
print(favs_dict['organism'])

for favorite in favs_dict:
	print(f'favorite {favorite} is {favs_dict[favorite]}')
new_fav = input("What's your favorite rock?")
favs_dict['rock'] = new_fav

favs_dict['organsim'] = 'cat'

print("Let's change a favorite item. Pick a category from these options:")
for fav in favs_dict:
	print(fav, sep=',')
category = input()

print(f'What\'s your favorite {category}?')
fav_thing = input()

favs_dict[category] = fav_thing

print('Here are the favorites again:')
for favorite in favs_dict:
  print(f'favorite {favorite} is {favs_dict[favorite]}')


