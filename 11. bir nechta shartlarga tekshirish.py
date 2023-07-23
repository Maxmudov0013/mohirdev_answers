# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 05:29:15 2023

@author: Lenovo
"""

# AMALIYOT
# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
    
    
# -----------------------------------------------------------------
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi 
# juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" 
# degan xabarni chiqaring.

'''
son=float(input("Juft son kiriting: <<< "))
if son%2:
    print("kiritilgan son juft emas")
else:
    print("raxmat")
'''


# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta 
# narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

'''
yosh=int(input("Yoshingizni kiriting: <<< "))

if yosh<4 or yosh>60 :
    print("Siz uchun kirish bepul taqdim etiladi ")
elif yosh>4 and yosh<18 :
    print("chipta narxi 10 000 so'm ")
elif yosh>18 and yosh<60:
    print("Siz uchun chipta narxlari 20 000 so'm")
''' 


# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni 
# solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring


'''
b_son=int(input("birinchi sonni kiriting <<< :"))
i_son=int(input("ikkinchi sonni kiriting <<< :"))

if b_son>i_son:
    print(f"birinchi son {b_son} ikkinchi {i_son} dan katta")
elif i_son>b_son:
    print(f"ikkinchi {i_son} soni birinchi {b_son} soni dan katta")
elif i_son==b_son:
    print("xar ikkala son teng")
'''

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli 
# mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating 
# va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring 
# va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.


'''
mahsulotlar=["non", "choy","salfetka", "bumaga", "pasta", "banan", "olma", "nok", "anor", "shaftoli"
              ,"qovun", "tarvuz"]
royxat=[]
i=0
for i in range(0, 5):
    i=i+1
    royxat.append(input(f"{i} chi maxsulot nomini kiriting: <<<"))
if mahsulotlar:
    for test in mahsulotlar:
        if test in royxat:
            print(f"Menyuda {test} bor")
        # else:
        #     print(f"menyuda {test} yoq")
else:
    print("savatchangiz bo'sh")
'''
            


# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 
# 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va 
# do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, 
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  
# Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar 
# do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar 
# do'konimizda yo'q: ....." degan xabarni chiqaring.

mahsulotlar=["non", "choy","salfetka", "bumaga", "pasta", "banan", "olma", "nok", "anor", "shaftoli"
              ,"qovun", "tarvuz"]
royxat=[]
mavjud_tovarlar=[]
yoq_tovarlar=[]

# i=0
# for i in range(0, 5):
#     i=i+1
#     royxat.append(input(f"{i} chi maxsulot nomini kiriting: <<<"))

#     for test in royxat:
#         if test in royxat:
#             mavjud_tovarlar.append(test)
#         else:
#             yoq_tovarlar.append(test)

#     if royxat:
#         for check in royxat:
#             if check in mavjud_tovarlar:
#                 print("siz so'ragan maxsulotlar barchasi do'konimizda mavjud")
#             elif check in :
#                 print(f"siz so'ragan tovarlardan {mavjud_tovarlar} do'konimizda mavjud")
                
# else:
#         print("siz so'ragan tovarlar do'konimizda mavjud emas")
        
        



# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

users=["admin", "qwerty", ""]
n=5
for i in range(0, n):
    pass
    users.append(input("user nomini kiriting:"))
    





# Foydalanuvchidan biror butun son kiritishni so'rang. 
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan 
# qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 



