import re
aa=re.compile('')
##'[а-я]\r\n.+?\r\n<w>'
def one():
    lex=0
    w=0
    with open('aaea.txt', 'r', encoding='utf-8') as a:
        a=a.readlines()
        for b in a:
            if re.search('<ana',b)!=None:
                lex+=1
            if re.search('<w>',b)!=None:
                w+=1
    print(lex/w)            
one()
def two():
    res={}
    d=re.compile('gr=\"([A-Z]*)')
    with open('aaea.txt', 'r', encoding='utf-8') as a:
        a=a.readlines()
        for b in a:
            if re.search(d,b)!=None:
                if re.search(d,b).group(1) not in res.keys():
                    res[re.search(d,b).group(1)]=1
                else:
                    res[re.search(d,b).group(1)]+=1
    with open('results.txt','w',encoding='utf-8')as k:
        for a in res.keys():
            k.write(a+'\t'+str(res[a])+'\n')
two()
def three():
    z=re.compile('<w>.*?<\w>',re.MULTILINE)
    with open ('aaea.txt', 'r', encoding='utf-8') as a:
        a=a.read()
        a=a.replace('</w>\n','')
        a=a.split('<w>\n')
        a=a.replace()
        with open ('ea.txt', 'w', encoding='utf-8') as f:
            for b in a:
                f.write(b+'\n')
        pat=re.compile('S.*?=твор')
        wd=re.compile('[а-я]*?\n',re.IGNORECASE)
        for num, b in enumerate(a):
            for c in b:
                if re.search(pat,c)!=None:
                    if re.search(pat,c).group(1)!=None:
                        dfg=re.search(pat,c).group(1)
                    
            
                            
three()
