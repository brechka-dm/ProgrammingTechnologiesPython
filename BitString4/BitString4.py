import sys #for command line arguments proceed
from MyBitString import MyBitString
bs1=MyBitString()
bs2=MyBitString()
if len(sys.argv) <3:
    bs1.inp()
    bs2.inp()
    print('a & b = ', end='')
    c=bs1.conj(bs2)
    c.outp()
else:
    bs1.f_inp(sys.argv[1]) #file input
    bs2.f_inp(sys.argv[2])
    print('a = ', end='')
    bs1.outp()
    print('b = ', end='')
    bs2.outp()
    bs3=bs1.conj(bs2) #conjunction
    print('a & b = ', end='')
    bs3.outp()
    bs3.f_outp(sys.argv[3]) #file output