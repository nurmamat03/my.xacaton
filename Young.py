#zadanye
# list_1 = ['name', 'age', '1', '19']

# def half2():
# 	for i in range(len(list_1)):
# 		if i % 2 == 0:
# 			list_1[1], list_1[i+1] = list_1[i+1], list_1[1]
# 	print(list_1)
# 	half2()		

# def half3():
#     a = input().split()
#     print((list(reversed(a[:(int(len(a)) // 2)]))) 
#     + (list(reversed(a[(int(len(a)) // 2)::]))))
# half3()

#zadanye2
a = eval(input('Введите конечное число Фибонначи: '))
  
def fib(n):
  a, b = 0, 1
  for i in range(n):
    yield a
    a, b = b, a + b
print(list(fib(a)))

