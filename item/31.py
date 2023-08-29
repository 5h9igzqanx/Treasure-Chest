#31
import os
import time
import webbrowser


def jia(a,b):
    #加法是将两个或者两个以上的数、量合起来,变成一个数、量的计算
    a = int(input("请输入第一个加数："))
    b = int(input("请输入第二个加数："))
    c = int(a) + int(b)
    out = str(a) + "加" + str(b) + "的和是" + str(c)
    print(out)

def jian(a,b):
    #减法是从一个数中减去另一个数的运算
    a = int(input("请输入被减数或减数1："))
    b = int(input("请输入被减数或减数2："))
    if a > b:
        c = int(a) - int(b)
        out = str(a) + "减" + str(b) + "的差是" + str(c)
        print(str(out))
    elif a == b:
        c = 0
        out = str(a) + "和" + str(b) + "相等,它们的差是" + str(c)
        print(str(out))
    else:
        c = int(b) - int(a)
        out = str(b) + "减" + str(a) + "的差是" + str(c)
        print(str(out))

def cheng(a,b):
    #乘法是将相同的数加起来的简便运算
    a = int(input("请输入第一个因数："))
    b = int(input("请输入第二个因数："))
    c = int(a) * int(b)
    out = str(a) + "乘" + str(b) + "的积是" + str(c)
    print(out)

def chu(a,b):
    #除法是已知两个因数的积与其中一个非零因数,求另一个因数的运算
    a = int(input("请输入被除数："))
    b = int(input("请输入除数："))
    while b == 0:
        b = int(input("除数不得等于0,请重新输入："))
    c = int(a) / int(b)
    out = str(a) + "除以" + str(b) + "的商是" + str(int(c))
    print(out)


yunsuan_xuanze = input("请选择你需要的四则运算,使用汉字：")
if yunsuan_xuanze == "加" or yunsuan_xuanze == "jia" or yunsuan_xuanze == "+":
    jia(0,0)
elif yunsuan_xuanze == "减" or yunsuan_xuanze == "jian" or yunsuan_xuanze == "-":
    jian(0,0)
elif yunsuan_xuanze == "乘" or yunsuan_xuanze == "cheng" or yunsuan_xuanze == "x":
    cheng(0,0)
elif yunsuan_xuanze == "除" or yunsuan_xuanze == "chu" or yunsuan_xuanze == "÷":
    chu(0,1)
else:
    print("这里没有你想要的运算,请在互联网上查找运算或打开计算器进行计算")
    jisuanqi_xuanze = input("是否为您打开计算器,是填T否填F:")
    if jisuanqi_xuanze == "T" or jisuanqi_xuanze =="t":
        print("请稍后,正在为您打开计算器")
        time.sleep(0.1)
        os.system("calc")
        webbrowser.open("https://www.baidu.com/s?wd=%E8%AE%A1%E7%AE%97%E5%99%A8&rsv_spt=1&rsv_iqid=0xa1cbddac0004a60d&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=8&rsv_sug1=11&rsv_sug7=101",new=0,autoraise=True)
        print("对不起,对于你的困惑,我们无法解决,深表歉意")
        #print("请联系qq：2109511809,发送反馈给我们")
    else:
        print("对不起,对于你的困惑,我们无法解决,深表歉意")
        #print("请联系qq：2109511809,发送反馈给我们")


close = input("\033[5;33m你需要继续使用吗,或是退出？(Y/N):\033[5;32m")
if close == "Y":
    print("===========================")
    py_z = r"cd . && python index.py"
    os.system(py_z)
elif close == "N" or close != "Y":
    print("===========================")
    os.system("pause")