ind =0 
b = 1
c = ''
d = {'ё','й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а',
'п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю'}
a = input(str("Наберите слово прописной кириллицей без пробелов: "))
for i in a:
    if (i not in d):
       ind += 1 
if ind == 0:        
    for i in a:
        if b % 2 == 0 and i != 'а' and i != 'к' :
            c += i + ', '
        b += 1
    c = c[0:(len(c) - 2)]   
    print (c)    
else:
    print('Условия нарушены') 
