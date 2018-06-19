import re
import os
#a=os.walk('fold')
#for b in a:
#    print(b[3])
def one():
    bg=0
    a=os.listdir('fold')
    pt_idi=re.compile('<title>(.*?)</title>')
    pt_rst=re.compile('<meta content=\"(.*?)\" name=\"(author|tagging|created|topic|docid)\"></meta>')
    with open ('result.csv', 'w', encoding='windows-1251')as k:
        for b in a:
            nme='fold/'+b
            with open (nme,'r',encoding='windows-1251')as v:
                v=v.readlines()
                ff=''
                for j in v:
                    if bg==0:
                        k.write('Title'+','+'Tagging'+','+'Autor'+','+'Created'+','+'Topic'+','+'Doc_id'+'\n')
                        bg=1
                    else:
                        if re.match(pt_rst,j)!= None:
                            if re.match(pt_rst,j).group(2)=='docid':
                                ff+=re.match(pt_rst,j).group(1)+'\n'
                                k.write(ff)
                                break
                            else:
                                ff+=re.match(pt_rst,j).group(1)+','
                            
                        if re.match(pt_idi,j)!= None:
                            ff+=re.match(pt_idi,j).group(1)+',' 

def two():
    a=os.listdir('fold')
    usd={}
    pt=re.compile('<w><ana lex=\"(([A-Z]|[А-Я])*?-?([A-Z]|[А-Я])*?)\"')
    with open ('list.csv', 'w', encoding='windows-1251')as k:#рудиментарный список, но убрать долго
        for b in a:
            nme='fold/'+b
            with open (nme,'r',encoding='windows-1251')as v:
                v=v.readlines()
                for j in v:
                    if re.search(pt,j)!=None:
                        ll=re.search(pt,j).group(1)
                        if ll not in usd:
                            usd[ll]=1
                        else:
                           usd[ll]+=1 
                           
    with open('freq.csv','w',encoding='windows-1251')as p:
        for i in usd.keys():
            wrt=str(i)+'\t'+str(usd[i])+'\n'
            p.write(wrt)
def main():
    one()
    two()
if __name__ ==  '__main__':
    main()
