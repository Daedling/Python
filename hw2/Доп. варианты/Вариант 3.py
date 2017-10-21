ind = 0
c = ''
d = {' '}
a = input(str("Наберите слово без пробелов: "))
for i in a:
    if (i in d):
       ind += 1
if ind == 0:
    ind -= 1
    while(ind >= -len(a)):
        if a[ind] != 'з' and a[ind] != 'я':
            c += a[ind]
        ind -= 1    
    print (c)
else:
    print('Условия нарушены') 
