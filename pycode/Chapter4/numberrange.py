for value in range(1,5):
    print(value)

print('value step') # 2-11中，每2个取一个值
for value1 in range(2,11,2):
    print(value1)

print('squares') # 取1-10的平方，并添加到列表中
squares = []
for value2 in range(1,11):
    square = value2**2
    squares.append(square)
print(squares)