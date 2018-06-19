#if not os.path.exists('fdas'):
#    os.makedirs('fdas')
import re
import os
from urllib.request import urlopen
z='https://ru.wikisource.org/wiki/%D0%9F%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F_%D0%90%D0%BD%D1%82%D0%BE%D0%BD%D0%B0_%D0%9F%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D0%B8%D1%87%D0%B0_%D0%A7%D0%B5%D1%85%D0%BE%D0%B2%D0%B0_%D0%B2_%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%BC_%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BA%D0%B5'
base='https://ru.wikisource.org'
wmat=''

sdate = re.compile('.*\"mw\-headline\" id=\"(.*?)\">.*$')
sname = re.compile('<li>.*?href=\"(.*?)\".*')
tname = re.compile('<title>(.*?)\(Чехов\) — Викитека</title>')
repl=re.compile('<\/?br.*?>')
txt=re.compile('<p>(.*?\n)')
subs=re.compile('(<.*/sup>)|(&#.*?;)|(<i.*>)')
sym=['\\','/','"',':','*','?','<','>','|','+',]
foldname=''
with urlopen(z) as k:
    for a in k:
       # print(a.decode('utf-8'))
       # print('----------')
        sn=re.search(sname,a.decode('utf-8'))
        sd=re.match(sdate,a.decode('utf-8'))
        if sd!=None:
            if not os.path.exists(sd.group(1)):
         #       print('________________NEW FOLDER___________')
                os.makedirs(sd.group(1))
                foldname=sd.group(1)
                for cx in sym:
                    foldname=foldname.replace(cx,'')
                foldname+='/'    
                    
      #  print(foldname)
     #   print(sn)
        if sn != None and foldname!='':
            urrl=base+sn.group(1)
         #   print(sn)
            with urlopen(urrl) as x:
                check=1
                for y in x:
             #       print(y.decode('utf-8'))
                    tn=re.match(tname,y.decode('utf-8'))
                    if check==1 and tn!= None:
                        check=0
                        nameyye=tn.group(1)
                        for cx in sym:
                            nameyye=nameyye.replace(cx,'')
                        namey=foldname+nameyye+'.txt'
   #                     print(namey)
                    if check == 0:
                        with open (namey,'w',encoding='utf-8') as r:
                            for w in x:
                                cv=re.sub(repl,'',w.decode('utf-8'))
                                cv=cv.replace('</p>','\n')
                                hh=re.match(txt,cv)
                                if hh != None:
                                    gof=re.sub(subs,'',hh.group(1))
                                    r.write(gof)
             #                       print(gof)
                            
                    
            wmat+=sn.group(1)
print(wmat)            


   
