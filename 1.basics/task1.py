'''
Напишете програма, която решава квадратно уравнение по зададени коефициенти. Коефициентите трябва да се приемат като аргумент от командния ред (виж лекция за символни низове).
Програмата трябва да извежда едно от следните неща (без самите кавички):
"x1|x2" - когато има два реални корена, където x1 и x2 са стойностите им
"no real roots" - когато няма реални корени
"x1" - когато има един корен, където x1 е стойността му
"special case" - когато е особен случай
'''
import math


# function for finding roots
def equationroots(a, b, c):
    x1 = 0
    x2 = 0

    if a == 0:
        if b == 0:
            return "special case"
        x1 = -c / b
        return x1

    # calculating discriminant using formula
    dis = (b ** 2) - (4 * a * c)
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        x1 = (-b + sqrt_val) / (2 * a)
        x2 = (-b - sqrt_val) / (2 * a)
        return f"{x1}|{x2}"
    elif dis == 0:
        x1 = (-b / (2 * a))
        return x1
    # discriminant is less than 0
    else:
        return "no real roots"


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(equationroots(a, b, c))
