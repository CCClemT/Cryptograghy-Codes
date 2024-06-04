
def isPrime(num)->bool:
    if(num == 2):
        return True
    if(num <= 0 or num % 2 == 0):
        return False
    else:
        for i in range(2,int(pow(num,0.5))):
            if(num % i == 0):
                return False
    return True

def gcd(num1,num2)->int:    #欧几里得除法求最大公约数
    while(num1 % num2 != 0):
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num2

def exgcd(a,b):     #扩展欧几里得除法
    if(b == 0):
        return 1,0
    x1,y1 = exgcd(b,a%b)
    return y1,(x1 - a//b * y1)

def encode(n: int,e: int,cnt: int):
    c = []
    with open(r".\toEncode.txt","r",encoding = "utf-8") as inputs:#加密文本
        lines = inputs.readlines()
        for i in lines:
            for j in bytes(i,encoding = 'utf-8'):
                c.append(str(j ** e % n).zfill(cnt))
    f = open(r".\ResultText.txt", "a", encoding = "UTF-8")
    f.write("------加密后的密文为------\n")
    for i in c:
        f.write(i)
    f.write("\n-------------------")
    f.close()

def decode(n: int,d: int, cnt: int):
    c = ""
    with open(r".\toDecode.txt","r",encoding = "utf-8") as inputs:#解密文本
        line = inputs.readline()
        for i in range(0,len(line),cnt):
            temp = ""
            for j in range(i,i+cnt):
                temp += line[j]
            c += chr(pow(int(temp),d)%n)
    f = open(r".\ResultText.txt", "a", encoding = "UTF-8")
    f.write("------解密后的明文为------\n")
    f.write(c)
    f.write("\n-------------------\n")
    f.close()



def RSA():
    p = int(input("输入p = "))
    if(isPrime(p) == False):
       exit("p不是质数")
    q = int(input("输入q = "))
    if(isPrime(q) == False):
        exit("q不是质数")
    n = p * q
    cnt = 0
    temp = n
    while temp > 0:
        temp = temp // 10
        cnt += 1
    on = (p - 1)*(q - 1)    #n的欧拉函数
    e = int(input("输入e = "))
    if(e <= 1 or e > on or gcd(e,on) != 1):
        exit("e不符合要求")
    d = exgcd(e,on)[0]      #生成乘法逆元,公钥(e,n)私钥(d,n)
    if d < 0:
        d = on + d
    mode = input("选择你要进行的操作(对当前文件夹下的toEncode.txt或toDecode.txt进行操作，结果输出到ResultText.txt中)：\n0:退出、1解密、2加密")
    while(True):
        if mode == '1':
            encode(n,e,cnt)
            mode = input("选择下一个操作")
        elif mode == '2':
            decode(n,d,cnt)
            mode = input("选择下一个操作")
        elif mode == '0':
            exit("退出程序")
        else:
            exit("无此操作")


if __name__ == '__main__':
    RSA()


