import re
def op():
    z = input("Название файла, без расширения: ")
    misc=['\'', '\"', '!', '?', ')', '(', ':', ';', '.', ',']
    res=''
    with open (z+'.txt', 'r', encoding='utf-8') as k:
        a = k.read()
        for b in a:
            if b not in misc:
                res += b
        res = res.split()        
        for ct, c in enumerate(res):
            res[ct] = c.capitalize()      
        a = res
        return (a)
def fun(lst):
    res = []
    pat = re.compile('un.*', re.IGNORECASE)
    for a in lst:
        if re.match(pat,a) != None:
            res.append(a)
    return res
def checknum():
    flag = 0
    num=['1','2','3','4','5','6','7','8','9','0']
    a = ''
    while flag == 0:
        a = input("Введите цифру или End для завершения: ")
        if a != '':
            flag = 1
            for b in a:
                if b not in num and a != 'End':
                    flag = 0
                    break
    return a
def check(lst,num):
    total = len(lst)
    req = 0
    while num != 'End':
        num = int(num)
        if total != 0:
            for a in lst:
                if len(a)>num:
                    req += 1
            print((str(req/total*100)+'%'))
            num = checknum()
            req = 0
        else:
            return print(('no match'))
    return print('Конец')

def main():   
    return (check(fun(op()), checknum()))

if __name__  ==  '__main__':
    main() 
            
