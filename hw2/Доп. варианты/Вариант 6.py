ind = 0
num = {'1','2','3','4','5','6','7','8','9','0'}
a = input(str("Введите число: "))
b = ''

for i in a:
    if (i not in num):
       ind += 1     
if ind == 0:
 
    a = int(a)
    while ind != 10:
        ind = ind + 1
        b+= '"' + str(ind) + ' * ' + str(a)+' = '+str(a * ind) +'"; '+'\n'
        
    print(b[0:(len(b) - 3)],)
else:
    print('Не число') 
