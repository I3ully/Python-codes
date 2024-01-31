'''დაწერეთ ფუნქცია, რომელსაც გადაეცემა შემთხვევითობის პრინციპით
დაგენერირებული 10 ელემენტიანი სიმრავლე და დააბრუნებს სიდიდით ყველაზე დიდ
ორ ელემენტს. გაითვალისწინეთ, სორტირების გამოყენება არ შეგიძლიათ.'''
from random import randrange
x = [randrange(20) for i in range(10)]
print(x)
def func(num):
    didi = max(num)
    num.remove(didi)
    kido = max(num)
    return didi, kido
print(func(x))
    


