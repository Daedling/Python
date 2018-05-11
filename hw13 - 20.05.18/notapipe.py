import os
def main():
    z=os.walk('.')
    count=0
    name=''
    for a,b,c in z:
        if len(c)>count:
            count=len(c)
            name=a
    print(os.path.basename(name)) 
if __name__ ==  '__main__':
    main()
