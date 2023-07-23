# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:20:29 2023

@author: Lenovo
"""

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

'''
ismlar = []
ismlar.append("Anvar")
ismlar.append("Alisher")
ismlar.append("Sohib")
 
print("salom ", ismlar[0], " ! ", ismlar[1], "ni ko'rgani boramizmi? ", ismlar[2], "ham keladi xozir" )
'''



# Sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang 
#(musbat, manfiy, butun, o'nlik). 
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

'''
sonlar=[5,20,-4,13,3.5,0.8]
print(sonlar[0]+sonlar[-1])
print(sonlar[1]-sonlar[2])
print(sonlar[3]*sonlar[4])
print(sonlar[2]+sonlar[5])
print(sonlar[1]+sonlar[0])

print(sonlar)
sonlar[5]=3
sonlar[0]=1
print(sonlar)

'''
# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p 
# hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik 
# bo'lgan shaxslarning ismini kiriting. 
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), 
# quyidagi ko'rinishda chiqaring:
# Men tarixiy shaxslardan Imom buxoriy bilan,
# Zamonamiz shaxslaridan esa Bill Gates bilan suxbatlashishni xolar edim

'''
t_shaxslar=["Abdullaxon 2", 'Amir Temur', 'Lenin', 'Imom Gazzoliy']
z_shaxslar=['Mubashshir Ahmad','Ilon Mask','Mark Sukerberg', 'Xalima Yoqub']

print("Men tarixiy shaxslardan ", t_shaxslar.pop(2), 'bilan \n', 'Zamonaviy shaxslardan esa', z_shaxslar.pop(-1), ' bilan suxbat qurishni istar edim')
'''

# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta 
# mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida 
# o'chrib tashlang. 

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() 
# va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends 
# ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

friends=[]
friends.append('farrux')
friends.append('Botir')
friends.append('Bobir')
friends.append('Begzod')
friends.append('Shoxrux')

print("dastlabki ro'yxat: ", friends)

friends.remove("Begzod")
friends.remove("Shoxrux")

print("mehmonga kela olmaydiganlar chiqarib yuborilgan ro'yxat:", friends)

friends.insert(2, "Bobir")
friends.insert(-1, "Jasur")
friends.insert(4, "Davron")

print("ro'yxatga yangi do'stlar kiritilgan xolat: ", friends)

mehmon=[]

mehmon.append(friends.pop(3))
mehmon.append( friends.pop(-1))
mehmon.append( friends.pop(0))
print("mehmonga kelgan do'stlar ro'yxati: ", mehmon)







