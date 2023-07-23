# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 19:04:28 2023

@author: Lenovo
"""

# AMALIYOT
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har 
# bir ismga takrorlanuvchi xabar yozing
'''
n=0
ismlar=['Ali','Vali', 'Hasan', "Husan","Olim"]
for x in ismlar:
    print("Salom ",x)
    n=n+1
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi"
# degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {n} martta takrorlandi")
'''

# ------------kutilayotgan natija
# Salom Ali
# Salom Vali
# Salom Hasan                          
# Salom Husan 
# Salom Olim

                         

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning 
# xar bir elementining kubini yangi qatordan konsolga chiqaring.

'''
toqlar=list(range(11,100,2))
kublar=[]
for kub in toqlar:
     print(f"{kub} sonining kubi {kub**3} ga teng \n")
     kublar.append(kub**3)
print(kublar)
'''

# Foydalanuvchidan 5 ta eng sevimli kinolarini 
# kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. 
# Natijani konsolga chiqaring.

'''
kinolar = []
for kino in range(0, 5):
    kinolar.append(input(f"{kino+1} inchi Kino nomini kiriting: <<< \n"))
print(kinolar)
'''



# Foydalanuvchidan bugun nechta odam bilan uchrashganini
#  (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning 
#  ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
'''
royxat=[]
suxbatdosh_soni=int(input("bugungi suxbatdoshlaringiz sonini kiriting: >>> "))
for sonlar in range(suxbatdosh_soni):
    royxat.append(input(f"{sonlar+1}  suxbatdoshingiz ismini kiriting: >>> "))
    
print("sizning suxbatdoshlaringiz ro'yxati: \n", royxat)
'''
    





