r=[]
a=0
b=0
c=0
print('Имя фаила должно иметь вид "text.exe", пустые фаилы не принимаются')
with open('text.txt', encoding ='utf-8') as txt:
    k = txt.readlines()
if len (k) == 0:
    print ("пшол")
    a=1
if a!=1:
    for i in k:
        c+=len(i.split())
    print(str(c/len(k)))
else:
    print("Фаил пуст")
