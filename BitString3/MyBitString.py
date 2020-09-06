class MyBitString:
    def inp(self): #manual input
        self.mas=input('Input bit string : ') #mas is object member
        if len(self.mas)>8: 
            print('Incorrect input')
            exit()
        for b in self.mas: 
            if b!='0' and b!='1':
                print('Incorrect input')
                exit()
        suffixlen=8-len(self.mas)
        suffix='0'*suffixlen
        self.mas=suffix+self.mas
    
    def f_inp(self,filename): #file input
        try:
            file=open(filename, 'r')
        except:
            print('Unable to open file')
            exit()
        self.mas=file.readline()
        if len(self.mas)>8: 
            print('Incorrect input')
            exit()
        for b in self.mas: 
            if b!='0' and b!='1':
                print('Incorrect input')
                exit()
        suffixlen=8-len(self.mas)
        suffix='0'*suffixlen
        self.mas=suffix+self.mas
        file.close()

    def outp(self): #console output
        print(self.mas)
        
    def f_outp(self, filename): #file output
        res=open(filename,'w')
        res.write(self.mas)
        res.close()        

    def conj(self, b): #b is a MyBitString object
        c='' #c is string
        i=0
        while (i<8):
            if self.mas[i]=='1' and b.mas[i]=='1':
                c+='1'
            else:
                c+='0'
            i+=1
        return MyBitString(c) #return MyBitString object by calling constructor
        
    def __init__(self, init_str=None): # constructor
        if init_str!=None: #if init_str==None it works like default constructor
            self.mas=init_str
            if len(self.mas)>8: 
                print('Incorrect input')
                exit()
            for b in self.mas: 
                if b!='0' and b!='1':
                    print('Incorrect input')
                    exit()
            suffixlen=8-len(self.mas)
            suffix='0'*suffixlen
            self.mas=suffix+self.mas