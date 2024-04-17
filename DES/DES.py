def change_to_data(str):
    data = []
    for x in str:
        data.append(int(x))
    return data

class PermutationTables:#置换表集
    initial_permutation_table = [58,50,42,34,26,18,10,2, #初始置换表
                                60,52,44,36,28,20,12,4,
                                62,54,46,38,30,22,14,6,
                                64,56,48,40,32,24,16,8,
                                57,49,41,33,25,17,9,1,
                                59,51,43,35,27,19,11,3,
                                61,53,45,37,29,21,13,5,
                                63,55,47,39,31,23,15,7,]

    inverse_initial_permutation_table =[40,8,48,16,56,24,64,32, #逆初始置换表
                                        39,7,47,15,55,23,63,31,
                                        38,6,46,14,54,22,62,30,
                                        37,5,45,13,53,21,61,29,
                                        36,4,44,12,52,20,60,28,
                                        35,3,43,11,51,19,59,27,
                                        34,2,42,10,50,18,58,26,
                                        33,1,41,9,49,17,57,25]

    permutation_seletion_table_1 = [57,49,41,33,25,17,9,    #置换选择1
                                    1,58,50,42,34,26,18,
                                    10,2,59,51,43,35,27,
                                    19,11,3,60,52,44,36,
                                    63,55,47,39,31,23,15,
                                    7,62,54,46,38,30,22,
                                    14,6,61,53,45,37,29,
                                    21,13,5,28,20,12,4]
    permutation_selection_table_2 = [14,17,11,24,1,5,       #置换选择2
                                      3,28,15,6,21,10,
                                      23,19,12,4,26,8,
                                      16,7,27,20,13,2,
                                      41,52,31,37,47,55,
                                      30,40,51,45,33,48,
                                      44,49,39,56,34,53,
                                      46,42,50,36,29,32]
    L = [1,2,3,4,5,6,7,8,
         9,10,11,12,13,14,15,16,
         17,18,19,20,21,22,23,24,
         25,26,27,28,29,30,31,32]
    R = [33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 
        49, 50, 51, 52, 53, 54, 55, 56, 
        57, 58, 59, 60, 61, 62, 63, 64]
    
    E_table = [32,1,2,3,4,5,
               4,5,6,7,8,9,
               8,9,10,11,12,13,
               12,13,14,15,16,17,
               16,17,18,19,20,21,
               20,21,22,23,24,25,
               24,25,26,27,28,29,
               28,29,30,31,32,1]
    P_table = [16,7,20,21,
               29,12,28,17,
               1,15,23,26,
               5,18,31,10,
               2,8,24,14,
               32,27,3,9,
               19,13,30,6,
               22,11,4,25]
    C = [1, 2, 3, 4, 5, 6, 7, 8, 
        9, 10, 11, 12, 13, 14, 15, 16, 
        17, 18, 19, 20, 21, 22, 23, 24, 
        25, 26, 27, 28]
    D = [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 46, 47, 48, 
       49, 50, 51, 52, 53, 54, 55, 56]
    
    rortate_left_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]#左循环移位表

    S_box = [[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],#s1
             [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
             [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
             [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],

             [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],#s2
             [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
             [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
             [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],

             [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],#S3
             [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
             [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
             [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],


             [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],#S4
             [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
             [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
             [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],

             [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],#S5
             [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
             [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
             [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],

             [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],#S6
             [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
             [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
             [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],

             [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],#S7
             [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
             [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
             [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],

             [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],#S8
             [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
             [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
             [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]

class Operate:
    def permutate(data:list,mode:PermutationTables):#置换mode
        temp = []
        temp.extend(mode)
        for x in range(len(mode)):
            n = mode[x] - 1
            temp[x] = data[n]
        return temp
    def replace(data:list,mode:PermutationTables):#代换mode
            row = int(str(data[0]) + str(data[-1]),2)
            temp = ''
            for i in data[1:5]: 
                temp += str(i)
            column = int(temp,2)
            temp = list(bin(mode[row][column])[2:].zfill(4))
            temp = list(map(int,temp)) #字符数组转数字数组
            return temp

    def rortate_left(data:list,time:int):#左循环移位
        temp = []
        for x in range(time,len(data)):
            temp.append(data[x])
        temp.append(data[0])
        if time == 2:
            temp.append(data[1])
        return temp
    
    def F(R:list,K1:list):  #F函数
        R1 = Operate.permutate(R,PermutationTables.E_table)#扩展置换(E表)
        temp1 = [] 
        temp2 = []
        for x in range(len(R1)):
            temp1.append(R1[x]^K1[x])       #XOR
        cnt = 0
        num = 0
        for x in range(6,len(temp1) + 1,6):
            temp2.extend(Operate.replace(temp1[cnt:x],PermutationTables.S_box[num]))        #S盒代换
            cnt += 6
            num += 1
        return(Operate.permutate(temp2,PermutationTables.P_table))    #P置换

def getkeys(k:list):
    k = Operate.permutate(k,PermutationTables.permutation_seletion_table_1)#置换选择1
    keys = []
    C = Operate.permutate(k,PermutationTables.C)#C0
    D = Operate.permutate(k,PermutationTables.D)#D0
    time = 1
    while time <= 16:
        C1 = Operate.rortate_left(C,PermutationTables.rortate_left_table[time - 1])#C左移位
        D1 = Operate.rortate_left(D,PermutationTables.rortate_left_table[time - 1])#D左移位
        temp = []       
        temp.extend(C1)
        temp.extend(D1)
        keys.append(Operate.permutate(temp,PermutationTables.permutation_selection_table_2)) #K1 置换选择2
        C = C1
        D = D1
        time += 1
    return keys

def turn(L1:list,R1:list,K1:list):

    R_1 = Operate.F(R1,K1)      #F函数
    R2 = []
    for x in range(len(R_1)):
        R2.append(L1[x]^R_1[x])
    L2 = R1         

    #下一轮数据 L2,R2
    return([L2,R2])

def encode(data:list,key:list):
    keys = getkeys(key)
    data = Operate.permutate(data,PermutationTables.initial_permutation_table)#初始置换IP
    L = Operate.permutate(data,PermutationTables.L)#L0
    R = Operate.permutate(data,PermutationTables.R)#R0

    time = 1
    while time <= 16:   #轮结构
        l = turn(L,R,keys[time - 1])
        L = l[0] 
        R = l[1] 
        time += 1

    temp = []
    temp.extend(R)
    temp.extend(L)    

    ciphertext = Operate.permutate(temp,PermutationTables.inverse_initial_permutation_table)

    
    for x in range(0,len(ciphertext),8):        #比特串转字符
        temp = ciphertext[x:x+8]
        string = ''
        for y in temp:
            string += str(y)
        print((hex(int(string,2))[2:].zfill(2)),end = '')

def decode(data:list,key:list):
    keys = getkeys(key)
    data = Operate.permutate(data,PermutationTables.initial_permutation_table)#初始置换IP
    L = Operate.permutate(data,PermutationTables.L)#L0
    R = Operate.permutate(data,PermutationTables.R)#R0

    time = 1
    while time <= 16:   #轮结构
        l = turn(L,R,keys[16 - time])
        L = l[0] 
        R = l[1] 
        time += 1

    temp = []
    temp.extend(R)
    temp.extend(L)    

    cleartext = Operate.permutate(temp,PermutationTables.inverse_initial_permutation_table)
    #print(cleartext)
    for x in range(0,len(cleartext),8):        #比特串转字符
        temp = cleartext[x:x+8]
        string = ''
        for y in temp:
            string += str(y)
        print(chr(int(string,2)),end = '')

def DES_encode():
    data = input("输入明文:\n")
    temp = []
    for i in bytes(data,'UTF-8'):
        temp.extend(change_to_data(bin(i)[2:].zfill(8)))
    data = []
    for i in range(0,len(temp),64):
        data.extend([temp[i:i+64]])
    while(len(data[-1]) != 64):#末尾不足补零
        data[-1].append(0)

    key = input("输入8位密钥:\n")
    temp.clear()
    for i in bytes(key,'UTF-8'):
        temp.extend(change_to_data(bin(i)[2:].zfill(8)))
    key = []
    for i in range(0,64):
        key.append(temp[i])

    print("密文为:")
    for data in data:
        encode(data,key)

def DES_decode():
    data = input("输入密文:\n")
    temp = []
    for i in range(0,len(data),2):
        str1 = str(data[i]) + str(data[i + 1])
        temp.extend(change_to_data(bin(int(str1,16))[2:].zfill(8)))
    data = []
    for i in range(0,len(temp),64):
        data.extend([temp[i:i+64]])
    while(len(data[-1]) != 64):#末尾不足补零
        data[-1].append(0)


    key = input("输入8位密钥:\n")
    temp.clear()
    for i in bytes(key,'UTF-8'):
        temp.extend(change_to_data(bin(i)[2:].zfill(8))) 
    key = []
    for i in range(0,64):
        key.append(temp[i])
    
    print("明文为:")
    for data in data:
        decode(data,key)

if __name__ == '__main__':

    while True:
        print("\n选择接下来的操作：")
        choise = input("1.加密 2.解密 3.结束\n")
        if choise == '1':
            DES_encode()
        elif choise == '2':
            DES_decode()
        elif choise == '3':
            exit("结束")
        else:
            print("无此操作")




