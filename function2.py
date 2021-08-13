# def rec(x):
# 	if x<10:
# 		print(x)
# 		rec(x+1)
# rec(1)

# import sys
# print(sys.getrecursionlimit())

# def itc(x):
# 	if x<=1:
# 		return 1
# 	else:
# 		return x * itc(x-1)
# c = itc(int(input('vvedite chislo:')))
# print(c)

# a = (lambda a,s,d:(a*s*d))(4,2,3)
# print("Объем бассейна", a)

# b = (lambda a,s:(a-s))(365,76)
# print(b)

# def nechet(m):
# 	print(m)
# 	if m % 2 == 0:
# 		return m
# 	else:
# 		nechet(m + 2)
# nechet(1)

# def deb(a):
# 	print(a)
# 	if a == set():
# 		return a
# 	else:
# 		a.pop()
# 		deb(a)
# deb({1,2,3})

from random import *
def gtt():
	a = []
	i = 0
	while i <100:
		s = randrange(10,50)
		a.append(s)
		i += 1
	print(a)

	a = set(a)
	a = list(a)
	print(a)
 
gtt()