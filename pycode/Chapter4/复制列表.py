my_food = ['pizza','cake','falafel']
frienf_food = my_food[:] # 遍历my_food所有元素，输入到frirnd_food（可以理解为保存一个副本到frirnd_food）

print(my_food)
print(frienf_food)
my_food.append('ice')
frienf_food.append('cannoli')# my_food frirnd_food各加入一个元素，互不影响
print(my_food)
print(frienf_food)

my_food = frienf_food # 将my_food赋值给frirnd_food，两个表关联到一起，appen任何一个表后的元素出现在两个表中

my_food.append('ice')
frienf_food.append('cannoli')
print(my_food)
print(frienf_food)
