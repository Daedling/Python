import re
def main():
    with open ('Kanawha.html','r',encoding='utf-8')as k:
        with open('result.html', 'w', encoding='utf-8') as res:
            
            ma = re.compile('(Птиц|Пти́ц)((ам)|(ами)|(ой)|(ах)|(ей)|(е)|(а)|(ы)|(у))?')
            mi = re.compile('(птиц|пти́ц)((ам)|(ами)|(ой)|(ах)|(ей)|(е)|(а)|(ы)|(у))?')

            for a in k:
                if re.search(ma,a)!= None:
                    d=re.search(ma,a)
                    if d.group(1) == 'Пти́ц':
                        a=re.sub(d.group(1),'Ры́б',a)
                    else:
                        a=re.sub(d.group(1),'Рыб',a)    
                    if d.group(2)==('ей'):
                        a=re.sub(d.group(2),'ой',a)
                        
                if re.search(mi,a)!= None:
                    d=re.search(mi,a)
                    if d.group(1) == 'пти́ц':
                        a=re.sub(d.group(1),'ры́б',a)
                    else:
                        a=re.sub(d.group(1),'рыб',a)  
                    if d.group(2)==('ей'):
                        a=re.sub(d.group(2),'ой',a)                
                res.write(a)
if __name__  ==  '__main__':
    main()            
