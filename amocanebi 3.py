# '''1. დაწერეთ ანონიმური ფუნქცია, რომელსაც გადავცემთ პარალელოგრამის
# სიმაღლეს და ფუძის ზომებს, დათვლის და დააბრუნებს ფართობს.'''

# print((lambda a, b: a * b)(int(input("A: ")), int(input("b: "))))

# '''2, დაწერეთ ანონიმური ფუნქცია, რომელსაც გადავცემთ ტრაპეციის სიმაღლეს და
# პარალელური გვერდების ზომებს, დათვლის და დააბრუნებს ფართობი'''

# print((lambda a, b, h: a + b/2 * h)(int(input("base 1: ")), int(input("base 2: ")), int(input("height: "))))


# '''3. დაწერეთ ანონიმური ფუნქცია, რომელიც მიიღებს რიცხვს და დააბრუნებს
# გადუბლირებული სახით 15=1515, 20=2020, 17=1717'''

# print(((lambda x: int(str(x)*2)))(int(input("x: "))))

# '''4. დაწერეთ ფუნქცია, რომელსაც გადავცემთ ტექსტს და ყველა ასოს შეუცვლის
# რეგისტრს (თუ მაღალ რეგისტრშია, გადაიყვანს დაბალში და პირიქით).
# სტრინგების მეთოდებს არ იყენებთ'''

# def func(x):
#     for i in x:
#         if 65 <= ord(i) <= 90:
#             print(chr(ord(i)+32),end="")
#         elif 97 <= ord(i) <= 122:
#             print(chr(ord(i)-32),end="")
#         else:print(i,end="")

# func("BsdsBBDSsdfsBDFDsdsNSs")



# '''5. დაწერეთ ფუნქცია, რომელსაც გადავცემთ ორ ასოს და ამ ასოების დიაპაზონში
# არსებულ ყველა ასოს დააბრუნებს ერთიანი სტრინგის სახით.
# '''
# def func(x,y):
#     s = ""
#     for i in range(min(ord(x),ord(y)),max(ord(x),ord(y)) + 1):
#         s += chr(i)
#     return s
# print(func('d','a'))


# '''6. დაწერეთ ფუნქცია, რომელსაც გადავცემთ სტრინგს და დათვლის რამდენი ასოა
# მაღალ რეგისტრში. გაითვალისწინეთ, მეთოდების, რომლითაც შეგიძლიათ
# განსაზღვროთ სიმბოლოს რეგისტრი, გამოყენების უფლება არ გაქვთ.
# '''
# def func(x):
#     s = 0
#     for i in x:
#         if 65 <= ord(i) <= 90:
#             s += 1
#     return s

# print(func("AAss"))


# '''7. დაწერეთ ფუნქცია, რომელსაც გადავცემთ სტრინგს და ყველა ასოს ანბანში h-
# მდე გადააქცევს a-დ, დანარჩენებს b-დ.'''

# def func(x):
#     s = ""
#     for i in x:
#         if 65 <= ord(i) < 72 or 97 <= ord(i) < 104:
#             s += 'a'
#         elif 74 <= ord(i) < 90 or 104 < ord(i) <= 122:
#             s += 'b'
#         else: s+= 'h'
#     print(s)
# func('AAabchkk')


# '''8. ფუნქცია იღებს ორ არგუმენტს, მამის და შვილის ასაკს, უნდა გამოვთვალოთ
# როდის იყო ან როდის იქნება მამა შვილზე ორჯერ დიდი.'''

# a = int(input("mamis asaki: "))
# b = int(input("shvilis asaki: "))
# def func(a,b):
#     x = a-b
#     c = a-2*x
#     if c>0: print("orjer didi iyo {} wlis win".format(c))
#     elif c<0: print("orjer didi iqneba{}wlis shemdeg".format(c))
#     else: print("orjer didia axla")
# func(a,b)

            
# '''9. პროგრამამ გამოიმუშაოს 100 შემთხვევითი რიცხვი 65-დან 122-ის ჩათვლით და
# გამომუშავებულ რიცხვის შესაბამისი სიმბოლოებით ASCII-ის ცხრილიდან
# შექმნას ტექსტი. შემდეგ კი მიღებული ტექსტი გადასცეს ფუნქციას. ფუნქციამ
# დათვალოს და დაბეჭდოს რამდენი სიმბოლოა დაბალ რეგისტრში.'''
# import random
# y = ''
# for i in range(100):
#     x = random.randint(65,122)
#     y = y + chr(x)
# print(y)
# def func(y):
#     s = 0
#     for k in y:
#         if 97 <= ord(k) <= 122:
#             s += 1
#     print(s)
# func(y)

# '''10. პროგრამამ გამოიმუშაოს 100 შემთხვევითი რიცხვი 65-დან 122-ის ჩათვლით და
# გამომუშავებულ რიცხვის შესაბამისი სიმბოლოებით ASCII-ის ცხრილიდან
# შექმნას ტექსტი. შემდეგ კი მიღებული ტექსტი გადასცეს ფუნქციას. დაბეჭდოს
# რამდენჯერ მეორდება სიმბოლო “k” (სიმბოლოების დასათვლელად არ
# გამოიყენოთ ჩაშენებული ფუნქციები ან მეთოდები).'''

# import random
# y = ''
# for i in range(100):
#     x = random.randint(65,122)
#     y = y + chr(x)
# print(y)
# def func(y):
#     s = 0
#     for k in y:
#         if ord(k) == 107:
#             s += 1

#     print(s)    
# func(y) 



import random
y = ''
for i in range(100):
    x = random.randint(65,122)
    y = y + chr(x)
def func(y):
    s = 0
    for k in y:
        if 65<=ord(k)<=90 or 97<=ord(k)<=122:
            if k == 'k':
                s += 1
        else: y = y.replace(k, '')
    print(y)
    print(s)    
func(y) 