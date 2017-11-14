a = str(input("Введите символы: "))*2
b = int(len(a)/2)
while b > 0:
    print(a[b:len(a)+b-int(len(a)/2)])
    b-=1
