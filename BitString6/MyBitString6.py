class MyBitString:
    def mas_from_str(self, st):
        self.mas=""
        for b in st: 
            if b!='0' and b!='1':
                #print('Incorrect input')
                #exit()
                raise ValueError("Incorrect symbol found")
            else:
                self.mas+=(b)
                
    def inp(self): #manual input
        m=input('Input bit string : ') #mas is object member
        self.mas_from_str(m)
    
    def f_inp(self,filename): #file input
        file=open(filename, 'r')
        m=file.readline()
        self.mas_from_str(m)
        file.close()

    def outp(self): #console output
        print(self.mas)
        
    def f_outp(self, filename): #file output
        res=open(filename,'w')
        res.write(self.mas)
        res.close()        

    def conj(self, b): #b is a MyBitString object
        c='' #c is string
        mi=self.mas #determine max and min strings
        ma=b.mas
        if len(ma)<len(mi):
            mi=ma
            ma=self.mas
        sl=len(ma)-len(mi) #both strings must be equal bby length
        suf='0'*sl #add previous 0s to smallest string
        mi=suf+mi
        i=0
        while (i<len(ma)): 
            if mi[i]=='1' and ma[i]=='1':
                c+='1'
            else:
                c+='0'
            i+=1
        c=c[c.find('1'):] #delete extra 0s from the begin 
        return MyBitString(c) #return MyBitString object by calling constructor
        
    def __init__(self, init_str=None): # constructor
        if init_str!=None: #if init_str==None it works like default constructor
            self.mas_from_str(init_str)

    def __and__(self, b): #overloading &
        return self.conj(b)
    
    def __str__(self): # overloading str
        return self.mas
        
    def __getitem__(self, i): #overloading []
        if i>=0 and i<len(self.mas): #if i in mas index range
            return self.mas[i]
        else:
            raise IndexError("Index out of bounds")
    
    def __setitem__(self, i, x): #overloading []
        if i>=0 and i<len(self.mas): #if i in mas index range
            self.mas=self.mas[:i]+str(x)+self.mas[i+1:] #construct new self.mas
        else:
            raise IndexError("Index out of bounds")