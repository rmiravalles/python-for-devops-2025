# A dictionary in Python is a collection of key-value pairs.
# Each key is connected to a value.
# A key's value can be a number, a string, a list, or another dictionary.
# A dictionary is wrapped in braces {}. Every key is connected to its value by a colon :
# and individual key-value pairs are separated by commas ,

spaceship = {
    'name': 'Millennium Falcon',
    'type': 'freighter',
    'length': 34.75, # it's common practice to put a comma after the last key-value pair
}

print(spaceship['name'])  # this will get us the value associated with the name key from the spaceship dictionary

# Dictionaries are dynamic structures, meaning we can add, replace or remove key-value pairs.

# here we're adding new key-value pairs
spaceship['crew'] = 4
spaceship['location'] = 'Corellia'
print(spaceship)

# here we're replacing an existing value with a new one
spaceship['crew'] = 5
print(spaceship)

# it can also be done like this
spaceship.update({'crew': 6})
print(spaceship)

# we can also update multiple key-value pairs at once
spaceship.update({'crew': 7, 'location': 'Tatooine'})
print(spaceship)

# here we're deleting the location key
del spaceship['location']
print(spaceship)

