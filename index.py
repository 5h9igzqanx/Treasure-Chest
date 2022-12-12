import webbrowser
import input.DevIndexSubCategory as ZDISC

print("\033[34m欢迎来到我的百宝箱！")
webbrowser.open("https://5h9igzqanx.github.io/SCDWBST",new=0,autoraise=True)
print("\033[34m    |我们的类别:\n    |1.日常使用\n    |2.社交聊天\n    |3.实用工具\n    |4.电脑报废\033[0m")
InputCategoryParent = input("\033[34m    |\033[33m请选择:\033[32m")
while InputCategoryParent != "1" and InputCategoryParent != "2" and InputCategoryParent != "3" and InputCategoryParent != "4":
    InputCategoryParent = input("\033[34m    |\033[33m请在上面4个中选择一个:\033[32m")
if InputCategoryParent == "1":
    ZDISC.Subcategory_1()
elif InputCategoryParent == "2":
    ZDISC.Subcategory_2()
elif InputCategoryParent == "3":
    ZDISC.Subcategory_3()
elif InputCategoryParent == "4":
    ZDISC.Subcategory_4()

##开发中尚未完成，禁止发布任何包或自解压程序！！！
##此文件已完成编辑，可以封装
##为此已内置环境，无需再次安装python