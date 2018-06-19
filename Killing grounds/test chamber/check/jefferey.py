import re
def unun():
    with open('zee.xml','r',encoding='utf-8') as a:
        res1={}
        premier=re.compile('<w><ana lex=\"(.*?)\".*')
        for b in a:
            if re.match(premier,b) != None:
                if re.match(premier,b).group(1) not in res1:
                    res1[re.match(premier,b).group(1)]=1
                else:
                    res1[re.match(premier,b).group(1)]=res1[re.match(premier,b).group(1)]+1
    return(res1)
def undeu(res1):
    num=0
    ct=0
    for b in res1:        
        num+=res1[b]
        ct+=1
    print(num/ct)
#undeu(unun())
#======================================================================================================    
def deuun():
    with open('zee.xml','r',encoding='utf-8') as a:
        res2={}
        deux=re.compile('.*? gr=\"([a-z]+)[\,\",\=].*',re.IGNORECASE)
        for b in a:
            if re.match(deux,b) != None:
                    if re.match(deux,b).group(1) not in res2:
                        res2[re.match(deux,b).group(1)]=1
                    else:
                        res2[re.match(deux,b).group(1)]=res2[re.match(deux,b).group(1)]+1
        return(res2)
def deudeu(res2):
    with open('res.xml','w',encoding='utf-8') as x:
        for a in res2:
            x.write(a+'\t'+str(res2[a])+'\n')
#deudeu(deuun())
#====================================================================================================    
with open('zee.xml','r',encoding='utf-8') as a:
    trx=re.compile('.*?gr=\".*?(ins).*')
    trx1=re.compile('.*?</ana>(.+?)</w>.*?')
   # for b in a:
     #   if re.match(trx1,b) != None:
      #      print(re.match(trx1,b).group(1)+'\t')
    a=a.readlines()    
    for ct,b in enumerate(a):
        outp=''
        if re.match(trx,b) != None:
            cot=-3
            while ct+cot<0:
                cot+=1
            while ct+cot <=len(a) and cot!=3:
                if re.match(trx1,a[ct+cot]) != None:
                    if cot!=0:
                        outp+=re.match(trx1,a[ct+cot]).group(1)+'\t'
                    else:
                        outp+='==='+re.match(trx1,a[ct+cot]).group(1)+'==='+'\t'
                cot+=1
            outp+='\n'
            with open ('res2.xml','a',encoding='utf-8')as df:
                df.write(outp)
                    


















    
