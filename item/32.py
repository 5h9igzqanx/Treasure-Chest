#32
import random
import os


xuanxiang_shuliang = int(input("请输入您困惑的条数，最多支持5个:"))
while xuanxiang_shuliang > 5:
    xuanxiang_shuliang = int(input("最多支持5条选项，请重新输入："))

xuanxiang_wenti = input("请输入您的问题：")
xuanxiang_1 = input("请输入您的第一个选项：")
xuanxiang_2 = input("请输入您的第二个选项：")
if xuanxiang_shuliang == 3 :
    xuanxiang_3 = input("请输入您的第三个选项：")
elif xuanxiang_shuliang == 4:
    xuanxiang_3 = input("请输入您的第三个选项：")
    xuanxiang_4 = input("请输入您的第四个选项：")
elif xuanxiang_shuliang == 5:
    xuanxiang_3 = input("请输入您的第三个选项：")
    xuanxiang_4 = input("请输入您的第四个选项：")
    xuanxiang_5 = input("请输入您的第五个选项：")

if xuanxiang_shuliang == 2 :
    xuanxiang_suijishu = int(random.randint(1,2))
    if xuanxiang_suijishu == 1:
        xuanxiang_shuchu = xuanxiang_1
    elif xuanxiang_suijishu == 2:
        xuanxiang_shuchu = xuanxiang_2
elif xuanxiang_shuliang == 3:
    xuanxiang_suijishu = int(random.randint(1,3))
    if xuanxiang_suijishu == 1:
        xuanxiang_shuchu = xuanxiang_1
    elif xuanxiang_suijishu == 2:
        xuanxiang_shuchu = xuanxiang_2
    elif xuanxiang_suijishu == 3:
        xuanxiang_shuchu = xuanxiang_3
elif xuanxiang_shuliang == 4:
    xuanxiang_suijishu = int(random.randint(1,4))
    if xuanxiang_suijishu == 1:
        xuanxiang_shuchu = xuanxiang_1
    elif xuanxiang_suijishu == 2:
        xuanxiang_shuchu = xuanxiang_2
    elif xuanxiang_suijishu == 3:
        xuanxiang_shuchu = xuanxiang_3
    elif xuanxiang_suijishu == 4:
        xuanxiang_shuchu = xuanxiang_4
elif xuanxiang_shuliang == 5:
    xuanxiang_suijishu = int(random.randint(1,5))
    if xuanxiang_suijishu == 1:
        xuanxiang_shuchu = xuanxiang_1
    elif xuanxiang_suijishu == 2:
        xuanxiang_shuchu = xuanxiang_2
    elif xuanxiang_suijishu == 3:
        xuanxiang_shuchu = xuanxiang_3
    elif xuanxiang_suijishu == 4:
        xuanxiang_shuchu = xuanxiang_4
    elif xuanxiang_suijishu == 5:
        xuanxiang_shuchu = xuanxiang_5

shuchu_zong1 = "恭喜，您关于“" + xuanxiang_wenti + "”的问题已有答复."
shuchu_zong2 = "“" + xuanxiang_shuchu + "”" + "被选中了！"
print(shuchu_zong1 + shuchu_zong2)


close = input("\033[5;33m你需要继续使用吗，或是退出？(Y/N):\033[5;32m")
if close == "Y":
    print("===========================")
    py_z = r"cd . && python index.py"
    os.system(py_z)
elif close == "N" or close != "Y":
    print("===========================")
    os.system("pause")