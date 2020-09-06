'''---INPUT FUNCTION---'''
def inp():
    res=input('Input bit string : ')
    if len(res)>8: 
        print('Incorrect input')
        exit()
    for b in res: 
        if b!='0' and b!='1':
            print('Incorrect input')
            exit()
    suffixlen=8-len(res)
    suffix='0'*suffixlen
    res=suffix+res
    return res

'''---CONJUNCTION FUNCTION---'''
def conj(a, b):
    c=''
    i=0
    while (i<8):
        if a[i]=='1' and b[i]=='1':
            c+='1'
        else:
            c+='0'
        i+=1
    return c

'''---MAIN---'''
'''---input---'''
bs1=inp()
bs2=inp()
'''---conjunction---'''
bs3=conj(bs1,bs2)
'''---output---'''
print('Result: ',bs3)

