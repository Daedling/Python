a = 0
c=''
b=[]
print('Введите 8 слов построчно, фаил вывода: \'result.txt\'')
while a != 8:
    a+=1
    b.append(input())
with open('result.txt', 'w', encoding='utf-8' )as k:
        a=0
        while a < len(b):
            if a%2==0:
                c=b[a]
            else:
                c+=b[a]
                k.write(str(c)+'\n')
            a+=1    
