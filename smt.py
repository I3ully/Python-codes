# a = 'btu magaria kargia btu kargia btu'

# def func(x):
#     return ' '.join(set(x)), len(x) - len(set(x))

# print(func(a.split()))


'''ნინისთან ცხოვრობს ოთხი ძაღლი (ჯეკა, ტობი, ციცქნა, მოკა) და ერთი კატა (ციცი).
თქვენი ამოცანაა დაწეროთ ფუნქცია, რომელიც გამოთვლის ცხოველების ასაკს.
ფუნქციას არგუმენტად უნდა გადასცეთ თითოეული ცხოველისთვის შესაბამისი
„ადამიანური ასაკი“ და დააბრუნოს რეალურად რამდენი წლისაა ცხოველი.
საბოლოოდ უნდა დაიბეჭდოს რამდენი წლისაა თითოეული ცხოველი.
გაითვალისწინეთ: ძაღლის შემთხვევაში, პირველი „ადამიანური წელი“ შეადგენს ძაღლის 15
წელს, მეორე წელი არის 9 წლის ექვივალენტი, ხოლო ყველა მომდევნო წელი − +5 წელი.
რაც შეეხება კატას, საწყისი ორი წელი იდენტურია, რაც ძაღლთან, ხოლო მესამე წლიდან +4
წელი.
მაგალითად, თუ ციცი სამი ადამიანური წლისაა, მისი ასაკი, 15+9+4, ანუ 28 გამოდის.'''

# def func(age, type):
#     if age <= 1:
#         return age * 15
#     elif age <= 2:
#         return (age-1) * 9 + 15
#     else:
#         return (age-2) * type + 24

# cxoveli = input('kata tu dzagli: ')
# asaki = float(input('ramdeni wlisaa:'))
# saxeli = input('saxeli: ')


# if cxoveli == 'dzagli':
#     print('{} aris {} wlis.'.format(saxeli, func(asaki, 5)))
# if cxoveli == 'kata':
#     print('{} aris {} wlis.'.format(saxeli, func(asaki, 4)))



'''გაქვთ ჩემპიონთა ლიგის გამარჯვებულების სია. თქვენი ამოცანაა დაწეროთ ფუნქცია,
რომელსაც გადასცემთ აღნიშნულ სიას და დამატებით ერთ არგუმენტს (season, team ან
country). თუ არგუმენტად გადაეცემა სეზონი, ამ შემთხვევაში უნდა დაიბეჭდოს არჩეული
სეზონის გამარჯვებული. თუ გადავცემთ გუნდს - დაიბეჭდოს მოცემულ პერიოდში
რამდენჯერ გაიმარჯვა ამ გუნდმა, ხოლო ქვეყნის შემთხვევაში - რამდენჯერ გახდა ამ ქყვეყნის
წარმომადგენელი ჩემპიონი.
მაგალითად, თუ მეორე არგუმენტად გადავცემთ სეზონს 2002-03, უნდა დაბეჭდოს AC Milan.
თუ გადავცემთ გუნდს, მილანს, დაბეჭდოს 2. თუ გადავცემთ ქვეყანას იტალიას, დაბეჭდოს 3.'''


# leagueWinners = [
# {'season':'1999-00', 'team':'Real Madrid', 'country':'Spain'},
# {'season':'2000-01', 'team':'Bayern Munich', 'country':'Germany'},
# {'season':'2001-02', 'team': 'Real Madrid', 'country':'Spain'},
# {'season':'2002-03', 'team':'AC Milan', 'country':'Italy'},
# {'season':'2003-04', 'team':'Porto', 'country':'Portugal'},
# {'season':'2004-05', 'team':'Liverpool', 'country':'England'},
# {'season':'2005-06', 'team':'Barcelona', 'country':'Spain'},
# {'season':'2006-07', 'team':'AC Milan', 'country':'Italy'},
# {'season':'2007-08', 'team':'Manchester United', 'country':'England'},
# {'season':'2008-09', 'team':'Barcelona', 'country':'Spain'},
# {'season':'2009-10', 'team':'Inter Milan', 'country':'Italy'}]

# def func(lst, season=None, team=None, cntr=None):
#     if season:
#         for i in lst:
#             if season in i.values():
#                 return (i['team'])
#     if team:
#         for i in lst:
            
#             if team in i.values():
#                 return (len(i))
#     if cntr:
        
#         for i in lst:
#             if cntr in i.values():
#                 return (len(i))
# print(func(leagueWinners,season='2007-08'))
                


'''OOP დაპროგრამების პარადიგმის სტილში დაწერეთ პროგრამა, რომელიც ინტერაქტიულად
მიიღებს პიროვნების სახელს, გვარს და დაბადების თარიღს (დღე/თვე/წელი). Პროგრამაში
მონაცემების შეტანის შემდეგ, ეკრანზე უნდა გამოიბეჭდოს მისალმება მითითებულ სახელზე და
გვარზე, პიროვნების ასაკი და განსაზღვრება თუ რომელ ზოდიაქოს ნიშანს ეკუთვნის ის.
გამოიყენეთ კლასები, ობიექტები, მეთოდები.

ზოდიაქოს ნიშნების განაწილება თარიღების მიხედვით:
ვერძი - 21 მარტი - 20 აპრილი
კურო - 21 აპრილი - 21 მაისი
ტყუპები - 22 მაისი - 21 ივნისი
კირჩხიბი - 22 ივნისი - 23 ივლისი
ლომი - 24 ივლისი - 23 აგვისტო
ქალწული - 24 აგვისტო - 23 სექტემბერი
სასწორი - 24 სექტემბერი - 23 ოქტომბერი
მორიელი - 24 ოქტომბერი - 22 ნოემბერი
მშვილდოსანი - 23 ნოემბერი - 21 დეკემბერი
თხის რქა - 22 დეკემბერი - 20 იანვარი
მერწყული - 21 იანვარი - 19 თებერვალი
თევზები - 20 თებერვალი - 20 მარტი'''

# def zodiac(day, month):
#     zodiaqo = [('თხის რქა', 20),
#                ('მერწყული', 19),
#                ('თევზები', 20),
#                ('ვერძი', 20),
#                ('კურო', 21),
#                ('ტყუპები', 21),
#                ('კირჩხიბი', 23),
#                ('ლომი', 23),
#                ('ქალწული', 23),
#                ('სასწორი', 23),
#                ('მორიელი', 22),
#                ('მშვილდოსანი', 21)]
#     if day <= zodiaqo[month - 1][1]:
#         return zodiaqo[month-1][0]
#     else: return zodiaqo[month][0]
# tve = int(input('Sheiyvanet romel tves daibadet ricxvebshi: '))
# dge = int(input('Sheiyvanet romel ricxvshi daibadet: '))
# print(zodiac(dge,tve))



'''ნინისთან ცხოვრობს ოთხი ძაღლი (ჯეკა, ტობი, ციცქნა, მოკა) და ერთი კატა (ციცი).
თქვენი ამოცანაა დაწეროთ ფუნქცია, რომელიც გამოთვლის ცხოველების ასაკს.
ფუნქციას არგუმენტად უნდა გადასცეთ თითოეული ცხოველისთვის შესაბამისი
„ადამიანური ასაკი“ და დააბრუნოს რეალურად რამდენი წლისაა ცხოველი.
საბოლოოდ უნდა დაიბეჭდოს რამდენი წლისაა თითოეული ცხოველი.
გაითვალისწინეთ: ძაღლის შემთხვევაში, პირველი „ადამიანური წელი“ შეადგენს ძაღლის 15
წელს, მეორე წელი არის 9 წლის ექვივალენტი, ხოლო ყველა მომდევნო წელი − +5 წელი.
რაც შეეხება კატას, საწყისი ორი წელი იდენტურია, რაც ძაღლთან, ხოლო მესამე წლიდან +4
წელი.
მაგალითად, თუ ციცი სამი ადამიანური წლისაა, მისი ასაკი, 15+9+4, ანუ 28 გამოდის.'''

# def animal(name, age, type):
#     if age <= 1: return f'{name} is {age * 15} years old'
#     elif age <= 2: return f'{name} is {(age-1)*9+15} years old'
#     else: return f'{name} is {(age-2)*type+24} years old'
# def func(*args):
#     result = ()
#     for i in args:
#         if i[1] == 'dzagli':
#             result += animal(i[0], i[2], 5),
#         elif i[1] == 'kata':
#             result += animal(i[0], i[2], 4),
#     return result

# print(func(('toby', 'dzagli', 5), ('cici', 'kata', 3)))




# from random import randrange
# lst = [randrange(1,20) for i in range(100)]
# print(lst)

# def func(x):
#     d = {i:x.count(i) for i in x}
#     t = [(i + max(d.values())) / max(d.values()) for i in d if d[i] == max(d.values())]
#     return d, t, sum(t)
# print(func(lst))








# from random import randrange
# lst = [randrange(1,20) for i in range(10)]
# print(lst)
# def func(x):
#     result = ()
#     for i in range(len(x)//2):
#         result += (x[i] + x[-(i+1)]),
#     return result
# print(func(lst))







# text = 'love me feed me never leave me'
# def func(x):
#     result = ()
#     f = open('words.txt','a')
#     for i in x:
#         f.write(i + '\n')
#         result += len(i),
#     f.close()
#     return result
# print(func(text.split()))






# from random import randrange
# matrx = [[randrange(5,15) for j in range(2)] for i in range(2)]
# for i in matrx:
#     print(i)

# def func(x):
#     det = x[0][0] * x[1][1] - x[0][1] * x[1][0]
#     return det
# print(f'randomuli matricis determinatia {func(matrx)}')

from random import randrange

def dete(a):
   x = (a[0][0] * a[1][1] * a[2][2]) + (a[1][0] * a[2][1] * a[3][2]) + (a[2][0] * a[3][1] * a[4][2])
   y = (a[0][2] * a[1][1] * a[2][0]) + (a[1][2] * a[2][1] * a[3][0]) + (a[2][2] * a[3][1] * a[4][0])
   return x - y

matrix = [[randrange(2,6) for i in range(3)] for i in range(5)]
print(dete(matrix))