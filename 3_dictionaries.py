# dictionary construction

country_capitals = {'Australia': 'Canberra', 'Eire': 'Dublin',
                    'France': 'Paris', 'Finland': 'Helsinki',
                    'UK': 'London', 'US': 'Washington'}

# Another way to construct a dictionary
alternate_country_capitals = dict(Hungary='Budapest', Sweden='Stockholm')

print(f"Country Capital Dictionary: {country_capitals}")
print(f"Alternate Country Capital Dictionary: {alternate_country_capitals}")

print(f"UK Capital City: {country_capitals['UK']}")

# add a key-value pair
country = 'Iceland'
country_capitals[country] = 'Reykjavik'
print(f"Country Capital Dictionary: {country_capitals}")

# add a key-value pair
country = 'Germany'
capital = 'Berlin'
country_capitals[country] = capital
print(f"Country Capital Dictionary: {country_capitals}")

# dictionary of string keys and list values
country_cities = {'UK': ['London', 'Wigan', 'Macclesfield', 'Bolton'],
                  'US': ['Miami', 'Springfield', 'New York', 'Boston']}

print(f"Country Cities Dictionary: {country_cities}")

print(f"Third UK City: {country_cities['UK'][2]}")

homer = 1
print(country_cities['US'][homer])

# add a key-value pair
country_cities['FR'] = ['Paris', 'Lyon', 'Bordeaux', 'Toulouse']

for country in country_cities.keys():
    print(country, ': ', country_cities[country])

# remove an item

del country_cities['US']

print(f"Country Cities Dictionary: {country_cities}")

removed_item = country_cities.pop('FR')
print(f"Removed item: {removed_item}")

# key error
# removed_item = country_cities.pop('DE')

# clear the dictionary, an empty dictionary
country_cities.clear()
print(f"Country Cities Dictionary: {country_cities}")

# merge two dictionaries
fruit = {1: 'Apple', 2: 'Banana', 3: 'Cherries'}
vegetables = {11: 'Tomatoes', 12: 'Carrots'}

for k, v in fruit.items():
    print(k, v)


for k, v in vegetables.items():
    print(k, v)

# update method, pass one dictionary to another dictionary, merge dictionaries
fruit.update(vegetables)

for k, v in fruit.items():
    print(k, v)


# as a tuple, with a key-value
for kv in vegetables.items():
    print(kv)

# turn values into a list
veggies_list = list(vegetables.values())
print(veggies_list)

# see keys in either dictionary using | all / union operator
all_keys = fruit.keys() | vegetables.keys()
print(all_keys)
