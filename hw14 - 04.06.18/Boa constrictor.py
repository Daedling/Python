import re
guts='[,.;:!?)(]?(([a-z]|[а-я]|ё|-)+)[,.;:!?)(]?'
gut='[,.;:!?)(\s]'
def main():
    z=re.compile(guts,re.IGNORECASE)
    with open ('word.txt','r',encoding='utf-8') as a:
        for ct, b in enumerate(a,1):
            res={}
            res.update({re.match(z,c).group(1).title() : len(re.findall(gut+re.match(z,c).group(1)+gut,b,re.IGNORECASE)) for c in b.split() if c !='—'})
            print('Предложение '+str(ct)+':')
            for d in res:
                if res[d]>1:
                    print(d,'{:^12}'.format(res[d]))
                
if __name__ ==  '__main__':
    main()
