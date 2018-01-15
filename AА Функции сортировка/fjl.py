d=''
co = 0
c=[]
m=[',','.']

def text(textname):
    with open (textname,'r',encoding='utf-8') as w:
        d=w.read()
        d=d.split()
    return(d)
def srt(list):
    srted=[]
    m=[',','.']
    for k in list:
        if (len(k)>2 and k[len(k)-2]=='_') or k in m:
            srted.append(k)
    return(srted)
def chsr(c):
    co=0
    res=''
    while co <len(c):
        if c[co][len(c[co])-1] == 'A' and c[co+1] [len(c[co+1])-1] == 'S':
            res+=c[co][0:len(c[co])-2]+' '+c[co+1][0:len(c[co+1])-2]+'\n'
        co+=1  
    return(res)

print(chsr(srt(text('txit.txt'))))
#with open('txit.txt', 'r', encoding = 'utf-8') as w:
#    d=w.read()
#d=d.split()
#for k in d:
#    if (len(k)>2 and k[len(k)-2]=='_') or k in m:
#        c.append(k)
#d=''
#d=''
#while co <len(c):
 #   if c[co][len(c[co])-1] == 'A' and c[co+1] [len(c[co+1])-1] == 'S':
  #      d+=c[co][0:len(c[co])-2]+' '+c[co+1][0:len(c[co+1])-2]+'\n'
   # co+=1    
#print(d)        
        
