# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:31:18 2023

@author: Lenovo
"""
# 1-vazifa Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

'''
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"

print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati ")
'''

# 2-vazifa Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) 
# qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

'''
kocha=input("ko'cha nomini kiriting: >>>   ")
mahalla=input("mahalla nomini kiriting: >>>   ")
tuman=input("tuman nomini kiriting: >>>   ")
viloyat=input("viloyat nomini kiriting: >>>   ")

print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati ")
'''

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
'''
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
print(kocha + " ko'chasi,\n " + mahalla + " mahallasi,\n " + tuman + " tumani, \n " + viloyat + " viloyati ")
'''



#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang


kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
manzil=f"{kocha} kochasi, {mahalla} mahallasi, {tuman}  tumani, {viloyat} viloyati "
#print(manzil)


#manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.

print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
print(manzil.upper())

#










