import re
def main():
    s=input('Введите имя фаила: ')
    with open(s+'.html', 'r', encoding ='utf-8') as k:
        pat=re.compile('iso639-3/documentation\.asp\?id=....')
        for a in k:
            m=re.search(pat,a)
            if m != None:
                z=m.group()     
    with open('result.txt','w', encoding='utf-8') as k:
        k.write(z[-4:-1])
if __name__  ==  '__main__':
    main()         
