ind =  0
num = {'1','2','3','4','5','6','7','8','9','0'}
a = input(str("Введите натуральное число: "))
b = ''

for i in a:
    if (i not in num):
       ind += 1     
if ind == 0:  
    ind = 1     
    a = int(a)
    while ind <= a:
        b += str(ind) + ', '
        ind = ind * 2
    print(b[0:(len(b)-2)])
else:
    print('Не натуральное число') 

