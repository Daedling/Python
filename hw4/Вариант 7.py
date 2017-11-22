r=[]
a=0
b=0
c=0
print('Имя фаила должно иметь вид "text.txt", пустые фаилы не принимаются')
with open('text.txt', encoding ='utf-8') as txt:
    k = txt.readlines()
if len (k) == 0:
    a=1
if a!=1:
    for i in k:
        c+=1
        if len(i.split())>5:
            b+=1
    if c == 0:
        c=1
    print(str(int(b/c*100))+'%')
else:
    print("Фаил пуст")
