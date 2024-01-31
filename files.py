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


def animal(x, y):
    if x == 1: 
        return x * 15
    if x == 2:
        return (x-1) * 9 + 15
    if x > 2: 
        return (x-2) * y + 24
cxoveli = input("zagli tu kata: ")
asaki = int(input("ramdeni wlisaa: "))
saxeli = input('ra hqvia: ')

if cxoveli == 'zagli':
    print('{} aris {} wlis'.format(saxeli, animal(asaki, 5)))
if cxoveli == 'kata':
    print('{} aris {} wlis'.format(saxeli, animal(asaki, 4)))



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

# def func(lst, seas=None, team=None, cntr=None):
#     if seas:
#         for i in lst:
#             if seas in i.values():
#                 return team
#     if team:
#         for i in lst:
#             if team in i.values():
#                 return len(i)
#     if cntr:
#         for i in lst:
#             if cntr in i.values():
#                 return len(i)
# print(func(leagueWinners, cntr='Spain'))


'''დაწერეთ ფუნქცია, რომელიც იღებს რიცხვს და დაპრინტავს რიცხვის შესაბამის
ფლოიდის სამკუთხედს.
ფლოიდის სამკუთხედი 5-ზე გამოიყურება შემდეგნაირად:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15.'''

# from random import randrange
# def func(x):
#     num=1
#     for i in range(1,x+1):
#         for j in range(i):
#             print(num,end=' ')
#             num += 1
#         print('')
# func(100)


