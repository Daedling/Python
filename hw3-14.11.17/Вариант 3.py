a = str(input("Введите символы: "))*2
b = 0
while b < len(a)/2:
    print(a[b:int(len(a)*0.5)+b])
    b+=1
