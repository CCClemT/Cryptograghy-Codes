def str2hex(strs):          
    data = []
    for i in bytes(strs,'UTF-8'):
        data.append(hex(i)[2:].zfill(2))
    return data

def dec2hex(a:int):
    return hex(a)[2:].zfill(2)

def hex2hex(strs):
    data = []
    for i in range(0,len(strs),2):
        data.append(strs[i] + strs[i+1])
    return(data)

def hex2str(strs:list):
    res = ""
    for i in str(strs).strip("[']").split("', '"):
        res += i
    return res
def hex2chr(strs:list):
    res = ""
    for i in strs:
        res += chr(int(i,16))
    return res

def xor_hex2int(a:str,b:str):
    return int(a,16) ^ int(b,16)
def xor_hex2hex(a:str,b:str):
    return hex(int(a,16) ^ int(b,16))[2:].zfill(2)

def xtime(res:str):
    res = int(str(res),16) << 1
    if res > 255:
        res = xor_hex2int(hex(res)[3:],'1b')
    res = hex(res)[2:].zfill(2)
    return res
                                                                      
def GF2_8(factor1:str,factor2:str):    #伽罗瓦域GF(2^8)上乘法  factor1 * factor2
    max_f = []
    cnt1 = int(factor2,16)     #提取所有最大因数,提取出分配律后所有的加数
    while cnt1 >= 1: 
        temp1 = '01'
        cnt2 = cnt1
        temp2 = factor1
        while cnt2 > 1:
            temp1 = xtime(temp1)
            temp2 = xtime(temp2)
            cnt2 = cnt2 - int(temp1,16) 
        max_f.append(temp2)
        cnt1 = cnt1 - int(temp1,16)
    res = 0        
    for i in max_f:
        res ^= int(i,16)
    return hex(res)[2:].zfill(2)

def getNk(keys:list):
    if len(keys) == 16:#128bit密钥
        return 4 
    elif len(keys) == 24:#192bit密钥
        return 6
    elif len(keys) == 32:#256bit密钥
        return 8
    else:
        print("密钥长度错误\n")
        return 0
    

Sbox =  [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
         [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
         [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
         [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
         [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
         [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
         [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
         [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
         [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
         [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
         [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
         [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
         [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
         [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
         [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
         [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]
inverse_Sbox = [
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
	[0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
	[0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
	[0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
	[0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
	[0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
	[0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
	[0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
	[0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
	[0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
	[0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
	[0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
	[0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
	[0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
	[0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
	[0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

Shift_Row = [0,5,10,15,
             4,9,14,3,
             8,13,2,7,
             12,1,6,11]
inverse_Shift_Row = [0,13,10,7,
                     4,1,14,11,
                     8,5,2,15,
                     12,9,6,3]

class Key:
    def __init__(self,nk:int):
        self.nk = nk
        self.RCON = self.initRCON()

    def initRCON(self):   #轮常数
        RCON = ['00','01']
        res = hex(0x01)[2:].zfill(2)
        for i in range(2,self.nk + 7):
            res = xtime(res)
            RCON.append(res)
        return RCON

    def T(self,datas:list,j:int)->list:              #轮常量j
        datas.append(datas.pop(0))  #1.左移一位
        for i in range(len(datas)): #2.S盒替换
            x = (int(datas[i][0],16))
            y = (int(datas[i][1],16))
            datas[i] = hex(Sbox[x][y])[2:].zfill(2)
        RCON = self.RCON
        temp = xor_hex2int(datas[0],RCON[j]) #轮常量异或
        datas[0] = hex(temp)[2:].zfill(2)   
        return(datas)

    def getKeys(self,datas:list):
        w = []
        for i in range(0,len(datas),4):
            temp = []
            for j in range(i,i+4):
                temp.append(datas[j])
            w.append(temp)

        if self.nk == 4:
            end = 44
        elif self.nk == 6:
            end = 52
        elif self.nk == 8:
            end = 60

        cnt = 1
        for i in range(self.nk,end):
            if self.nk == 8 and i % self.nk != 0 and i % 4 == 0:

                temp = []
                t = []
                t.extend(w[i-1])
                for j in range(len(t)): #字节代换
                    x = (int(t[j][0],16))
                    y = (int(t[j][1],16))
                    t[j] = hex(Sbox[x][y])[2:].zfill(2)

                for j in range(0,4):
                    temp.append(dec2hex(xor_hex2int(w[i-self.nk][j],t[j])))
                w.append(temp)
            elif i % self.nk != 0:
                temp = []
                for j in range(0,4):
                    temp.append(dec2hex(xor_hex2int(w[i-self.nk][j],w[i-1][j])))
                w.append(temp)
            else:
                temp = []
                t = [] 
                t.extend(w[i-1])
                t = self.T(t,cnt)
                cnt += 1  
                for j in range(0,4):
                    temp.append(dec2hex(xor_hex2int(w[i-self.nk][j],t[j])))
                w.append(temp)
        return(w)

class Test:
    def __init__(self):
        pass

    def subBytes(self,datas:list):       # 1.S盒替换
        for i in range(len(datas)): 
            x = (int(datas[i][0],16))
            y = (int(datas[i][1],16))
            datas[i] = hex(Sbox[x][y])[2:].zfill(2)
        return datas
    def inverse_subBytes(self,datas:list):#_1.逆S盒替换
        for i in range(len(datas)): 
            x = (int(datas[i][0],16))
            y = (int(datas[i][1],16))
            datas[i] = hex(inverse_Sbox[x][y])[2:].zfill(2)
        return datas

    def shiftRows(self,datas:list):      # 2.行位移
        temp = []
        for i in Shift_Row:
            temp.append(datas[i])  #左移
        return temp
    def inverse_shiftRows(self,datas:list):#_2.逆行位移
        temp = []
        for i in inverse_Shift_Row:
            temp.append(datas[i])  #右移
        return temp

    def mixColumns(self,datas:list):     # 3.列混合
        temp = []
        for i in range(0,16,4):
            temp.append(xor_hex2hex(xor_hex2hex(GF2_8('2',datas[i]),GF2_8('3',datas[i + 1])),xor_hex2hex(datas[i + 2],datas[i + 3])))
            temp.append(xor_hex2hex(xor_hex2hex(datas[i],GF2_8('2',datas[i + 1])),xor_hex2hex(GF2_8('3',datas[i + 2]),datas[i + 3])))
            temp.append(xor_hex2hex(xor_hex2hex(datas[i],datas[i + 1]),xor_hex2hex(GF2_8('2',datas[i + 2]),GF2_8('3',datas[i + 3]))))
            temp.append(xor_hex2hex(xor_hex2hex(GF2_8('3',datas[i]),datas[i + 1]),xor_hex2hex(datas[i + 2],GF2_8('2',datas[i + 3]))))
        return temp

    def inverse_mixColumns(self,datas:list):     # _3.逆列混合
        temp = []
        for i in range(0,16,4):
            temp.append(xor_hex2hex(xor_hex2hex(GF2_8('0E',datas[i]),GF2_8('0B',datas[i + 1])),xor_hex2hex(GF2_8('0D',datas[i + 2]),GF2_8('09',datas[i + 3]))))
            temp.append(xor_hex2hex(xor_hex2hex(GF2_8('09',datas[i]),GF2_8('0E',datas[i + 1])),xor_hex2hex(GF2_8('0B',datas[i + 2]),GF2_8('0D',datas[i + 3]))))
            temp.append(xor_hex2hex(xor_hex2hex(GF2_8('0D',datas[i]),GF2_8('09',datas[i + 1])),xor_hex2hex(GF2_8('0E',datas[i + 2]),GF2_8('0B',datas[i + 3]))))
            temp.append(xor_hex2hex(xor_hex2hex(GF2_8('0B',datas[i]),GF2_8('0D',datas[i + 1])),xor_hex2hex(GF2_8('09',datas[i + 2]),GF2_8('0E',datas[i + 3]))))
        return temp

    def addRoundKey(self,datas:list,W:list,round:int):   # 4.轮密钥加
        x = 0
        temp = []
        for i in range(4*round,4*round + 4):
            for j in W[i]:
                temp.append(xor_hex2hex(datas[x],j))
                x += 1
        return temp

    def turn(self,datas:list,W:list,Nk:int):
        i = 1
        while i < Nk + 6:
            datas = self.subBytes(datas)
            datas = self.shiftRows(datas)
            datas = self.mixColumns(datas)
            datas = self.addRoundKey(datas,W,i)
            i += 1
        datas = self.subBytes(datas)
        datas = self.shiftRows(datas)
        datas = self.addRoundKey(datas,W,i)
        return datas

    def inverse_turn(self,datas:list,W:list,Nk:int):
        i = Nk + 5
        while i > 0:
            datas = self.inverse_shiftRows(datas)
            datas = self.inverse_subBytes(datas)
            datas = self.addRoundKey(datas,W,i)
            datas = self.inverse_mixColumns(datas)
            i -= 1
        datas = self.inverse_shiftRows(datas)
        datas = self.inverse_subBytes(datas)
        datas = self.addRoundKey(datas,W,i)
        return datas      

def encode():
    temp = str2hex(input("输入单组明文\n"))
    keys = str2hex(input("输入16\\24\\32字节密钥\n"))
    Nk = getNk(keys)
    plaintest = Test()
    key = Key(Nk)
    keys = key.getKeys(keys)
    x = 0   #第一次轮密钥加
    datas = []
    for i in range(0,4):
        for j in keys[i]:
            datas.append(xor_hex2hex(temp[x],j))
            x += 1
    print("密文为:\n"+hex2str(plaintest.turn(datas,keys,Nk)))

def decode():
    temp = hex2hex(input("输入单组密文\n"))
    keys = str2hex(input("输入16\\24\\32字节密钥\n"))
    Nk = getNk(keys)
    plaintest = Test()
    key = Key(Nk)
    keys = key.getKeys(keys)
    x = 0   #第一次轮密钥加
    datas = []
    for i in range(len(keys)-4,len(keys)):
        for j in keys[i]:
            datas.append(xor_hex2hex(temp[x],j))
            x += 1
    print("明文为:\n",(hex2chr(plaintest.inverse_turn(datas,keys,Nk))))

if __name__ == '__main__':
    while True:
        mode = input("选择模式:\n1.加密  2.解密  3.退出\n")
        if mode == '1':
            encode()
        elif mode == '2':
            decode()
        elif mode == '3':
            exit()
        else:
            print("无此操作") 
