rs=0
note=0

while note!=1:
    rs=0
    in_=input('Введите сочетание символов:' )
    if len(in_)==0:
        note=1
        break
    with open('freq.txt', encoding='utf-8') as k:
        z=k.readlines()
        for y in z:
            y=y.split(' | ')
            if y[0]==in_:
                print('\n'+y[1])
                print(y[2])
                rs=1
                break
        if rs == 0:       
            print('Не найдено')
print('Работа закончена.')
