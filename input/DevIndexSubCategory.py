import os
def Subcategory_1():
    print("\033[34m    |    |\033[34m你选择的类别是\033[32m1.日常使用")
    print("\033[34m    |    |\033[33m我们的类别：\033[34m\n    |    |1.未定\n    |    |2.未定\n    |    |3.未定\n    |    |4.未定")
    InputSubCategory_1 = input("\033[34m    |    |\033[33m请选择:\033[32m")
    while InputSubCategory_1 != "1" and InputSubCategory_1 != "2" and InputSubCategory_1 != "3" and InputSubCategory_1 != "4":
        InputSubCategory_1 = input("\033[34m    |    |\033[33m请在上面4个中选择一个:\033[32m")
    if InputSubCategory_1 == "1":
        Unavailable(2)
    elif InputSubCategory_1 == "2":
        Unavailable(2)
    elif InputSubCategory_1 == "3":
        Unavailable(2)
    elif InputSubCategory_1 == "4":
        Unavailable(2)

def Subcategory_2():
    print("\033[34m    |    |你选择的类别是\033[32m2.社交聊天")
    print("\033[34m    |    |\033[33m我们的类别：\033[34m\n    |    |1.未定\n    |    |2.未定\n    |    |3.未定\n    |    |4.未定")
    InputSubCategory_1 = input("\033[34m    |    |\033[33m请选择:\033[32m")
    while InputSubCategory_1 != "1" and InputSubCategory_1 != "2" and InputSubCategory_1 != "3" and InputSubCategory_1 != "4":
        InputSubCategory_1 = input("\033[34m    |    |\033[33m请在上面4个中选择一个:\033[32m")
    if InputSubCategory_1 == "1":
        Unavailable(2)
    elif InputSubCategory_1 == "2":
        Unavailable(2)
    elif InputSubCategory_1 == "3":
        Unavailable(2)
    elif InputSubCategory_1 == "4":
        Unavailable(2)

def Subcategory_3():
    print("\033[34m    |    |你选择的类别是\033[32m3.实用工具")
    print("\033[34m    |    |\033[33m我们的类别：\033[34m\n    |    |1.计算器\n    |    |2.困惑转盘\n    |    |3.未定\n    |    |4.未定")
    InputSubCategory_1 = input("\033[34m    |    |\033[33m请选择:\033[32m")
    while InputSubCategory_1 != "1" and InputSubCategory_1 != "2" and InputSubCategory_1 != "3" and InputSubCategory_1 != "4":
        InputSubCategory_1 = input("\033[34m    |    |\033[33m请在上面4个中选择一个:\033[32m")
    if InputSubCategory_1 == "1":
        Subcategory_31()
    elif InputSubCategory_1 == "2":
        Subcategory_32()
    elif InputSubCategory_1 == "3":
        Unavailable(2)
    elif InputSubCategory_1 == "4":
        Unavailable(2)

def Subcategory_4():
    print("\033[34m    |    |你选择的类别是\033[32m4.电脑报废")
    yn = input("\033[34m    |    |此为实验性功能,可能对你的pc有\033[33m不可逆的损伤\n\033[34m    |    |你确定吗(Y/N):\033[32m")
    if yn == "Y":
        print("\033[34m    |    |\033[33m我们的类别：\033[34m\n    |    |1.未定\n    |    |2.未定\n    |    |3.未定\n    |    |4.未定")
        InputSubCategory_1 = input("\033[34m    |    |\033[33m请选择:\033[32m")
        while InputSubCategory_1 != "1" and InputSubCategory_1 != "2" and InputSubCategory_1 != "3" and InputSubCategory_1 != "4":
               InputSubCategory_1 = input("\033[34m    |    |\033[33m请在上面4个中选择一个:\033[32m")
        if InputSubCategory_1 == "1":
            Unavailable(2)
        elif InputSubCategory_1 == "2":
            Unavailable(2)
        elif InputSubCategory_1 == "3":
            Unavailable(2)
        elif InputSubCategory_1 == "4":
            Unavailable(2)
    elif yn == "N" or yn != "Y":
        os.system("pause")

# ↑ 子类别1 函数


def Subcategory_11():
    print("\033[34m    |    |    |你选择的类别是\033[32m1.未定")
    Unavailable(3)
    #yn = input("\033[34m    |    |    |你确定吗(Y/N):\033[32m")
    #print("\033[0m")
    #if yn = "Y":
    #    cmd_z = r"pytnon item\\11.py"
    #    os.system(cmd_z)
    #elif yn == "N" or yn != "Y":
    #    Subcategory_1()

#……

def Subcategory_31():
    print("\033[34m    |    |    |\033[34m你选择的类别是\033[32m1.计算器")
    yn = input("\033[34m    |    |    |\033[33m你确定吗(Y/N):\033[32m")
    print("\033[0m")
    if yn == "Y":
        print("===========================")
        cmd_z = r"python item\\31.py"
        os.system(cmd_z)
    elif yn == "N" or yn != "Y":
        Subcategory_3()

def Subcategory_32():
    print("\033[34m    |    |    |\033[34m你选择的类别是\033[32m2.困惑转盘")
    yn = input("\033[34m    |    |    |\033[33m你确定吗(Y/N):\033[32m")
    print("\033[0m")
    if yn == "Y":
        print("===========================")
        cmd_z = r"python item\\32.py"
        os.system(cmd_z)
    elif yn == "N" or yn != "Y":
        Subcategory_3()

# ↑ 子类别2 函数

def Unavailable(level):
    if level == 2:
        print("\033[34m    |    |\033[33m该功能暂不可用\033[0m")
        os.system("pause")
    elif level == 3:
        print("\033[34m    |    |    |\033[33m该功能暂不可用\033[0m")
        os.system("pause")
    elif level == 4:
        print("\033[31mError!\033[0m")

# ↑ 暂不可用 函数

#此文件暂未完成编辑,禁止封装