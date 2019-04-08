pizza = ['sausage','beef','seafood']
friend_pizza = pizza[:]
pizza.append('chicken')
friend_pizza.append('cheese')
print('my pizza is: ')
for pizzaa in pizza[:]:
    print(pizzaa.title(),end = ',')

print('\nfriend pizza is: ')
for friend_pizzaa in friend_pizza[:]:
    print(friend_pizzaa.title( ),end = ',')

