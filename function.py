# def num():
# 		a = 12
# 		b = 8
# 		return a+b
# print(num())

# def sum():
# 	b = 12+5
# 	c = 20+5
# 	return b
# print(sum())

# def itc(*args):
# 	print(args)
# itc(10, 23, 444)	

# def team(name, *sok):
# 	print(f"hello: {name}")
# 	for i in sok:
# 		print(i)
# team("Vova", 100, 200, 3223)

# def add(a,b):
# 	print(a+b)
# def substract(a,b):
# 	print(a-b)
# def multiply(a,b):
# 	print(a*b)
# def divide(a,b):  
# 	print(a/b)
# add(213,56)	
# substract(516,78)
# multiply(445,45)
# divide(600,20)

# def func(str):
# 	index = 0
# 	for i in str:
# 		index += 1
# 	print(index)
# str =input("how words on text:")
# func(str)

 # def word_sum(a):
#     c = 0
#     for x in a:
#         if ('a' <= x <= 'z') or ('A' <= x <= 'Z') or ('а' <= x <= 'я') or ('А' <= x <= 'Я'):
#             c += 1
#         else:
#             pass
#     print(c)
# a = input('Введите предложение:')
# word_sum(a)

# def l():
#   s = input("Введите предложение: ")
#   e = 0
#   for i in s:
#     e +=1
#   print(e)
# l()

d1={'brand':'honda','model':'fit','year':'2002'}
d2={'color':'blue'}
def dict(d1,d2):
    d1.update(d2)
    print(d1)
dict(d1,d2)

def men():
   name = input("Назовите имя файла: ")
   a = open(f'/home/range/lesson/1{name}.txt', 'a+')
   pokushat = input("Что бы вы хотели поесть : ")
   vypit = input("Что бы вы хотели поесть : ")
   a.write(pokushat)
   a.write(" ")
   a.write(vypit)
   a.close()
men()
