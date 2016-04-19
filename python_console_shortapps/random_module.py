import random

print('How many days of weather?')
days_to_generate = int(input())

while days_to_generate > 0:
    day_temp = random.randint(32, 100)

    if day_temp > 90:
        forcast = 'Hot'
    elif day_temp > 60:
        forcast = 'Nice'
    else:
        forcast = 'Cold!'

    days_to_generate -= 1
    print(forcast)
