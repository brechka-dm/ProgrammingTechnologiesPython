import sys #for command line arguments proceed

'''---MANUAL INPUT FUNCTION---'''
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
    
'''---FILE INPUT FUNCTION---'''
def inp(filename):
    try: #exception handling
        file=open(filename, 'r') #trying to open file to read
    except: #in case of file open fault
        print('Unable to open file')
        exit()
    res=file.readline() #read one line from file
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
    file.close()
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
'''---manual input---'''
#bs1=inp()
#bs2=inp()
'''---file input---'''
if len(sys.argv) <3: #check arguments count
    print('Not enough parameters')
    print('BitString2 a.txt b.txt c.txt')
    exit()
bs1=inp(sys.argv[1])
bs2=inp(sys.argv[2])
'''---conjunction---'''
bs3=conj(bs1,bs2)
'''---manual output---'''
#print('Result: ',bs3)
'''---file output---'''
res=open(sys.argv[3],'w')
res.write(bs3)
res.close()


