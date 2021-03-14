import random
from wzory import *

#zad1
# a =[1-x for x in range(1,11)]
# ## for x in range(1,11):
# ##     a.append(1-x)
# print(a)
# b=[4**y for y in range(6)]
# ## for y in range(6):
# ##     b.append(4**y)
# print(b)
# c=[z for z in b if z % 2 ==0]
# ## for z in b:
# ##     if z % 2 == 0:
# ##        c.append(z)
# print(c)


#zad2
# a = random.randint(0, 100)
# b = random.randint(0, 100)
# c = random.randint(0, 100)
# d = random.randint(0, 100)
# e = random.randint(0, 100)
# f = random.randint(0, 100)
# g = random.randint(0, 100)
# h = random.randint(0, 100)
# i = random.randint(0, 100)
# j = random.randint(0, 100)
# lista1 = [a,b,c,d,e,f,g,h,i,j]
# print(lista1)
# lista2 = []
# for x in lista1:
#     if x%2 == 0:
#         lista2.append(x)
# print(lista2)

#zad 3
# produkty={'pomidory':'sztuki','orzechy':'kg','ziemniaki':'kg'}
# sztuki={key:value for key,value in produkty.items() if value=='sztuki'}
# print(sztuki)


#Zad 4

# def trojkat_prostokatny(a,b,c):
#     if a**2 + b**2 == c**2:
#         print("jest prostokatny")
#         return 1
#     elif a**2 + c**2 == b**2:
#         print("jest prostokatny")
#         return 1
#     elif b**2 + c**2 == a**2:
#         print("jest prostokatny")
#         return 1
#     else:
#         print("nie jest prostokatny")
#         return 0

#zad5
# def pole_trapezu(a=0,b=0,h=0):
#      pole = ((a+b) * h)/2
#      return pole
#zad6
# def ciag(a=1,b=4,ile=10)
#     lista = []
#     for i in range(a,ile+a)
#         lista.append(i*b)
#     return lista

#zad 7
# a = 1
# def ciag(* liczby):
#     if len(liczby)==0:
#         return 0
#     else:
#         a = 1
#         b = 4
#         for i in liczby:
#             a*=(i*b)
#         return a
# print(ciag(a,2,3,4,5))

#zad 8
# def zakupy(** rzeczy):
#     wartosc = 0
#     ilosc = len(rzeczy.items())
#     for i in rzeczy.values():
#         wartosc += i
#     return ilosc, wartosc


#zad 9
# print(arytmetyczne.nty_wyraz(1, 3, 9))
# print(arytmetyczne.suma_nwyrazow(2, 3, 4))
# print(geometryczne.nty_wyraz(3, 5, 6))
# print(geometryczne.suma_nwyrazow(2, 4, 8))





