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
            res[ct] = c.lower()      
        a = res
        return (a)
def loc(a):
    res=[]
    pat=re.compile('си((жу)|(д((е((л(а|и|о)?)|(в((ши)|(ший)|(шее)|(шая))?)|(ть(ся)?)))|(я(т|(щий)|(щая)|(щее))?)|(и(т|м|(шь))?))))\Z')
    for b in a:
        if re.match(pat,b)!= None and b not in res:
            res.append(b)
    if res==[]:
        print('Пусто')
    else:
        for b in res:
            print(b)
if __name__ == '__main__':
    loc(op())
        

