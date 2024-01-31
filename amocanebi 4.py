# 1.

# print((lambda b, h: b * h)(int(input("base: ")), int(input("height:"))))




# def registri(x):
#     for i in x:
#         if ord(i)>64 and ord(i)<91: 
#             i=chr(ord(i)+32)
#             print(i, end="")
#         elif ord(i)>96 and ord(i)<123:
#             i=chr(ord(i)-32)
#             print(i, end="")
#         else: print(i,end= "")
# registri("ZZZzz")





# '''დაწერეთ ფუნქცია, რომელსაც გადავცემთ ორ ასოს და ამ ასოების დიაპაზონში
#  არსებულ ყველა ასოს დააბრუნებს ერთიანი სტრინგის სახით.'''

# def xazi(x, y):
#     s = ""
#     for i in range(min(ord(x),ord(y)), max(ord(x),ord(y) + 1)):
#         s += chr(i)
#     return s
# print(xazi('j', 'a'))







# '''დაწერეთ ფუნქცია, რომელსაც გადავცემთ სტრინგს და დათვლის რამდენი ასოა
# მაღალ რეგისტრში. გაითვალისწინეთ, მეთოდების, რომლითაც შეგიძლიათ
# განსაზღვროთ სიმბოლოს რეგისტრი, გამოყენების უფლება არ გაქვთ.'''

# def func(x):
#     counter = 0
#     for i in x:
#         if 65 <= ord(i) <= 90:
#             counter += 1
#     return counter

# print(func('sdasSDAD')) 





# '''დაწერეთ ფუნქცია, რომელსაც გადავცემთ სტრინგს და ყველა ასოს ანბანში h-
# მდე გადააქცევს a-დ, დანარჩენებს b-დ.'''


# def func(X):
#     s = ""
#     for i in X:
#         s += i
#     return s

# print(func('asSFGAFASnw'))






# '''
# 9. პროგრამამ გამოიმუშაოს 10 შემთხვევითი რიცხვი 65-დან 122-ის ჩათვლით და
# გამომუშავებულ რიცხვის შესაბამისი სიმბოლოებით ASCII-ის ცხრილიდან
# შექმნას ტექსტი. შემდეგ კი მიღებული ტექსტი გადასცეს ფუნქციას. ფუნქციამ
# დათვალოს და დაბეჭდოს რამდენი სიმბოლოა დაბალ რეგისტრში.'''


# import random

# sityva = ''
# for i in range(10):
#     ricxvi = random.randint(65,122)
#     sityva = sityva + chr(ricxvi)
# print(sityva)

# def texti(sityva):
#     x=0
#     for k in sityva:
#         if 123>ord(k)>97:
#             x+=1
            
#     print(x)


# texti(sityva)

'''10. პროგრამამ გამოიმუშაოს 100 შემთხვევითი რიცხვი 65-დან 122-ის ჩათვლით და
გამომუშავებულ რიცხვის შესაბამისი სიმბოლოებით ASCII-ის ცხრილიდან
შექმნას ტექსტი. შემდეგ კი მიღებული ტექსტი გადასცეს ფუნქციას. დაბეჭდოს
რამდენჯერ მეორდება სიმბოლო “k” (სიმბოლოების დასათვლელად არ
გამოიყენოთ ჩაშენებული ფუნქციები ან მეთოდები).'''

import random
sityva = ''
for i in range(100):
    x = random.randint(65, 122)
    sityva = sityva + chr(x)
def func(y):
    z = 0
    for i in y:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            if i == 'k':
                z += 1
        else: y = y.replace(i, '')
    print(y)
    print(z)
func(sityva)

# def asaki(a,b):
#     x=a-b
#     c=a-2*x
#     if c>0: print("orjer didi iyo {} wlis win".format(c))
#     elif c<0: print("orjer didi iqneba {} wlis Shemdeg".format(abs(c)))
#     else: print("orjer didia axla")
# asaki(int(input("mamis asaki:   ")),int(input("shvilis asaki:   ")))

# #მეორე გზა
# def asaki(a,b):
#     x=a-b
#     c=a-2*x
#     if c>0: return "orjer didi iyo {} wlis win".format(c)
#     elif c<0: return "orjer didi iqneba {} wlis Shemdeg".format(abs(c))
#     else: return "orjer didia axla"
# print(asaki(int(input("mamis asaki:   ")),int(input("shvilis asaki:   "))))




