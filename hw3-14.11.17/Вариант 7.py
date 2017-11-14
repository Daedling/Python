a = str(input("Введите символы: "))
b = 0
while b < len(a):
    print(a[b:(len(a)-b)])
    b+=1
    
