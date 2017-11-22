mn=0
mx=0
a=0
print('Имя фаила должно иметь вид "text.exe", пустые фаилы не принимаются')
with open('text.txt', encoding ='utf-8') as txt:
    k = txt.readlines()    
if len (k) == 0:
    print ("пшол")
    a=1
if a!=1:
    mx=len(k[0])
    mn=len(k[0])
    for i in k:
        if len(i)> mx:
            mx=len(i)
        if len (i) < mn:
            mn = len(i)  
    print(str(int(mx-1/mn-1)))
else:
    print("Фаил пуст")
