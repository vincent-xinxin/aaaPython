#number = []
#for numb in range(1,51):
#    val = numb
#    number.append(val)
# 上面4行效果等同于下面一行，此方法称之为列表解析
number = [value for value in range(1,51) ]
print(number)
print('sum: '+ str(sum(number)))