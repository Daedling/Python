a=input('Введите слово: ')
let = {'q','w','e','r','t','y','u','i','o','p','a','s','d','f'
       ,'g','h','j','k','l','z','x','c','v','b','n','m',' '}
vow = {'e','y','u','o','a','i'}
con = {}
conbase = ''
k=''
I=0
a=a.replace(',','')
w=a.split()
output=''
if a == '':
    I+=1
for z in w:    
    for i in z:
        if i not in let:
            I+=1           
    while I==0:
         for i in z:
            while i not in vow and k == '':
                conbase+=i
                i=''
                break
            k+=i
         break    
    if(I!=0):
        output+='*не слово* '
    else:
        output+=k+conbase+'ay '
    k=''
    conbase=''
    I=0
print(output[:len(output)-1])
