ind = 0
num = {'1','2','3','4','5','6','7','8','9','0'}
a = input(str("Введите натуральное число: "))
b = ''

for i in a:
    if (i not in num):
       ind += 1     
if ind == 0:
    a = int(a)
    while ind != a:
        ind = ind + 1
        b = input(str("Введите последовательность знаков: "))
        if b != "программирование":             
            print(b)
        else:
            break
    print('fin')    
else:
    print('Не натуральное число') 
