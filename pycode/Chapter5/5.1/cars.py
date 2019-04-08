cars = ['audi','bmw','passt','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
cars.insert(0,'BMW')
print(cars)
for car in cars:
    if car.lower() == 'bmw':
        print(car.title())
    else:
        print(car)