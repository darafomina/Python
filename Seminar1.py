
def triangle(a,b,c):
    if (a == b) and (b == c):
        return 'Треугольник равносторонний'
    elif ((a == b) or (a == c) or (b == c)) and (a + b > c) and (a + c > b) and (b + c > a):
        return 'Треугольник равнобедренный'
    elif (a + b > c) and (a + c > b) and (b + c > a):
        return 'Треугольник существует'
    else:
        return 'Треугольник не существует'

def Main():
    print("Введите стороны треугольника a, b, c")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(triangle(a,b,c))
Main()


prime = True
maxDig = 100000
while True:
    n = int(input('введите число от 1 до 100000. n = '))
    if 0 < n < maxDig: break
for i in range (2, n//2):
    if n%i == 0 :
        prime = False
        break
if prime : print('число ', n, ' простое')
else : print('число ', n, ' составное')