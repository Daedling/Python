import os
import re
def main():
    pat = re.compile('.*((([a-z]).*([а-я]|ё))|(([а-я]|ё).*([a-z]))).*')
    k=os.listdir()
    num=0
    for a in k:
        if os.path.isdir(a) == True:
            if re.search(pat,a) != None:
                num+=1
                print(a)
    print('Всего найдено папок, название которых содержит и кириллические, и латинские символы: '+str(num))        
if __name__ == '__main__':
    main()
