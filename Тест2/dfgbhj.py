import re
def main():
    with open ('l.xml','r',encoding = 'utf-8') as k:
        with open('frequency.csv', 'w', encoding = 'utf-8') as z:
            k=k.readlines()
            stuff=[]
            stuff2={}
            a=re.compile('type=\"l.f.*\"')
            for h in k:
                if re.search(a,h) != None:
                    stuff.append(h)
            a=re.compile('lemma=\"(.*)\".*type=\"(.*)\"')
            for h in stuff:
                d=re.search(a,h)
                counter=1
                if d.group(2) not in stuff2.keys():
                    stuff2[d.group(2)]=counter
                else:
                    stuff2[d.group(2)]+=1
            for a in stuff2:
                p=a+','+str(stuff2[a])+'\n'
                z.write(p)
if __name__  ==  '__main__':
    main()            
  #  with open ('body.txt','r',encoding='utf-8') as c:
   #     a = re.compile('(<..*>)')
    #    b = re.compile('(<\..*>)')
     #   stuff=[]
      #  c=c.readlines()    
       ## for x in c:
        #    print(x)
         #   jj=re.search(a,x)
          #  print(jj)
           # fd=re.sub(jj.group(1),'',x)
          #  fd=re.sub(jj.group(2),'',fd)
           # stuff.append(fd)
       # print(stuff)                 
    #re.search()
