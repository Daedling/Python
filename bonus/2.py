gcnt = 0
cnt = 0
am = 0
to = 0
mx = 0
mn = 0
tag = True
a = 'i'
num = {'1','2','3','4','5','6','7','8','9','0','-'}
print('������� ����� ���������')
while(a != '')
    a = input(str())
    if a == '' and gcnt==0
        print('��� �����')
        tag = False
        break
    for i in a
        cnt += 1
        if i not in num or (i=='-' and (cnt != 1 or len(a) = 1))
            print(conditions wrong)
            tag = False
            break
    cnt = 0
    gcnt += 1
    if gcnt  1 and tag == False
        print(����� ����� +str(am)+n����� ����� +str(to)+n������� ����. +str(toam)+n���������� ����� +str(mx)+n���������� ����� +str(mn))
    if tag == False
        break
    if a !=''
        to+=int(a)
        am+=1
        if gcnt==1
           mx = int(a) 
           mn = int(a)     
        else
            if int(a) mx
                mx = int(a)
            if int(a) mn
                mn = int(a)

if tag == True    
    print(����� ����� +str(am)+n����� ����� +str(to)+n������� ����. +str(toam)+n���������� ����� +str(mx)+n���������� ����� +str(mn))
