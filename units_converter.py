#А теперь сотворим конфликт!


print('Please, choose unit to convert from (m3, dm3, l, ml, sm3):')
units_from = input()
print(f'Please, enter unit to convert in {units_from}')
number = float(input())
print('Please, choose unit to convert to (m3, dm3, l, ml, sm3):')
units_to = input()

ml = {
    'm3': lambda number: number / 1000 / 1000,
    'dm3': lambda number: number / 1000,
    'sm3': lambda number: number,
    'l': lambda number: number / 1000,
    'ml': lambda number: number,
    }

l = {
    'm3': lambda number: number / 1000,
    'dm3': lambda number: number,
    'sm3': lambda number: number * 1000,
    'l': lambda number: number,
    'ml': lambda number: number * 1000,
    }

sm3 = {
    'm3': lambda number: number / 1000 / 1000,
    'dm3': lambda number: number / 1000,
    'sm3': lambda number: number,
    'l': lambda number: number / 1000,
    'ml': lambda number: number,
    }

dm3 = {
    'm3': lambda number: number / 1000,
    'dm3': lambda number: number,
    'sm3': lambda number: number * 1000,
    'l': lambda number: number,
    'ml': lambda number: number * 1000,
    }

m3 = {
    'm3': lambda number: number,
    'dm3': lambda number: number * 1000,
    'sm3': lambda number: number * 1000 * 1000,
    'l': lambda number: number * 1000,
    'ml': lambda number: number * 1000 * 1000,
    }

dict_units = {
    'm3': m3,
    'dm3': dm3,
    'sm3': sm3,
    'l': l,
    'ml': ml
    }


print(dict_units[units_from][units_to](number))
