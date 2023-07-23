# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 15:07:00 2023

@author: Lenovo
"""

'''
# AMALIYOT:
    1. 
O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
Ro'yxatning uzunligini konsolga chiqaring

sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

Asl ro'yxatni qaytadan konsolga chiqaring

reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga 
teskari tartibda konsolga chiqaring.
'''
####   1111111111111
'''
davlatlar=["Singapur", "Germany", "Italy", "Russia", "Uzbekistan", 'Saudian Arabia', "China", "France"]

print(davlatlar)
print("ro'yxat uzunligi : \n ", len(davlatlar) , " ta")


print("tartiblangan ro'yxat: \n")
print(sorted(davlatlar))

print("teskari tartibdagi davlatlar : \n")
print(sorted(davlatlar ,reverse=True))

print("dastlabki ro'yxat \n ")

print(davlatlar)
'''

# ---------------2222222222222222-------------

'''
120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

Ro'yxatdagi elementlar sonini hisoblang

Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
'''

# -----222222222

'''
juftlar=list(range(20,121,2))
print("20 dan 120 gacha bo'lgan juft sonlar ro'yxati: \n", juftlar)
summ=juftlar
print("20 dan 120 gacha bo'lgan juft sonlar yig'indisi: \n", sum(summ))

ayirma=max(juftlar)-min(juftlar)
print("eng katta va eng kichik sonlar ayirmasi: \n", ayirma)

print("20 dan 120 gacha bo'lgan juft sonlar soni: \n ", len(juftlar))

print("tanlab olingan 20 ta son : \n")
print("birinchi yigirmattalik \n", juftlar[:20])

print("so'ngi yigirmattalik \n", juftlar[-20:])
'''
 
 
# ---------------333333333333333333--------------------

'''


taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
nonushta degan yangi ro'yxatga taomlardan nusxa oling
Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va 
qo'shimcha 2 ta taom qo'shing
Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va 
nonushta[0] = "qaymoq va non" 
deb qiymat berib ko'ring.
'''

taomlar=("osh","somsa","shashlik","lag'mon","KFS")

nonushta=taomlar
nonushta.remove("somsa")
nonushta.remove("shashlik")
nonushta.remove("osh")
nonushta.append("mastava")
nonushta.append("atala")
print(nonushta)
nonushta=tuple(nonushta)
nonushta[0]=("norin")





