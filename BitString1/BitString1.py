'''---input bit string 1---'''
bs1=input('Input bit string 1: ')
if len(bs1)>8: #check length
    print('Incorrect input')
    exit()
for b in bs1: #check incorrect sybmols
    if b!='0' and b!='1':
        print('Incorrect input')
        exit()
suffixlen=8-len(bs1) #calculate prior 0 count
suffix='0'*suffixlen
bs1=suffix+bs1 #add prior 0s
'''---input bit string 2---'''
bs2=input('Input bit string 2: ')
if len(bs2)>8:
    print('Incorrect input')
    exit()
for b in bs2:
    if b!='0' and b!='1':
        print('Incorrect input')
        exit()
suffixlen=8-len(bs2)
suffix='0'*suffixlen
bs2=suffix+bs2
'''---conjunction---'''
bs3=''
i=0
while (i<8):
    if bs1[i]=='1' and bs2[i]=='1':
        bs3+='1'
    else:
        bs3+='0'
    i+=1
print('Result: ',bs3)

