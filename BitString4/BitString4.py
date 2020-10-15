import sys #for command line arguments proceed
from MyBitString import MyBitString

if len(sys.argv) <3: #check arguments count
    print('Not enough parameters')
    print('BitString2 a.txt b.txt c.txt')
    exit()
bs1=MyBitString() #creating empty objects
bs2=MyBitString()
bs1.f_inp(sys.argv[1]) #file input
bs2.f_inp(sys.argv[2])
print('a =', end=' ') #print ends by SPACE
bs1.outp() #console output
print('b =', end=' ')
bs2.outp()
bs3=bs1.conj(bs2) #conjunction
print('Result:', end=' ')
bs3.outp()
bs3.f_outp(sys.argv[3]) #file output

