a = 0
prd=0
c=''
b=[]
lst=['1','2','3','4','5','6','7','8','9','0']
print('Введите 7 неотрицательных чисел построчно, фаил вывода: \'result.txt\'')
while a != 7 and prd == 0 :
    a+=1
    print(a)
    z=input()
    b.append(z)
    if z not in lst:
        prd=1
if prd == 1:
    print('Нарушение условий')
else:    
    with open('result.txt', 'w', encoding='utf-8' )as k:
        for i in b:
            k.write('X'*int(i)+'\n')
