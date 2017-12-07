
with open('freq.txt', encoding='utf-8') as k:
    z=k.readlines()
    for y in z:
        w=y.split('|')
        if 'перех' in w[1].split():
            print(y)
      
