# ABC_list 大写字母列表
# abc_list 小写字母列表
# abc 一次小写字母生成器 A = 仅大写 a = 仅小写 1 = 仅数字 A1 = 数字+大写 a1 = 数字+小写 Aa1 = 全混 Aa = 大小写混合
# temp1 临时数据-随机数生成数字保留
# temp2 临时数据-随机类型选择器保留
# a = 函数输入参数数据
# m1 = 键入的类型，类型见生成器类型
# m2 = 键入的模式，1 = 有限生成 2 = 无限生成
# r = 返回内容
# e = 错误数量
# t = 正确数量
# m2_sys 有限生成数量
# temp_r 临时数据-用户游戏开始时输入的内容
# everynum 用户答题总数

#预定义
ABC_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
abc_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
temp1 = 0
temp2 = 0
a = ''
m1 = ''
m2 = 0
m2_sys = 0
temp_m1 = ''
r = ''
e = 0
t = 0
temp_r = ''
everynum = 0

#预备主程序
import random
import sys
print('欢迎使用打字游戏v1.0')
print('注意：大小写敏感，游玩前检查caps lock的状态')
m1 = input('生成类型 1.仅小写 2.仅大写 3.仅数字 4.数字+大写 5.数字+小写 6.全混 7.大小写混合')
m2 = input('生成模式 1.有限 2.无限')
#输入差错检测
if m1 != '1' and m1 != '2' and m1 != '3' and m1 != '4' and m1 != '5' and m1 != '6' and m1 != '7':
    print('你第一个输入的内容似乎不是1234567中的任意一个')
    sys.exit()
if m2 != '1' and m2 != '2':
    print('你第二个输入的似乎不是12中的任意一个')
    sys.exit()
#提问生成模式
if m2 == '1':
    m2_sys = input('请输入你要生成的数量，一定要是整数，本问题不会进行差错检测')
elif m1 == '2':
    print('无限模式下输入 exit 即可退出')  

#随机生成器
def abc(a):
    #仅大写
    if a == 'A':
        temp1 = random.choice(ABC_list)
        return temp1
    #仅小写
    elif a == 'a':
        temp1 = random.randint(0,25)
        temp = abc_list[temp1]
        return temp
    #仅数字
    elif a == '1':
        temp1 = random.randint(0,9)
        return temp1
    #数字+大写
    elif a == 'A1':
        temp2 = random.randint(1,2)
        #大写生成
        if temp2 == 1:
            temp1 = random.randint(0,25)
            return ABC_list[temp1]
        #数字生成
        elif temp2 == 2:
            temp1 = random.randint(0,9)
            return temp1
    #数字+小写
    elif a == 'a1':
        temp2 = random.randint(1,2)
        if temp2 == 1:
            temp1 = random.randint(0,25)
            return abc_list[temp1]
        elif temp2 == 2:
            temp1 = random.randint(0,9)
            return temp1
    #大小写混
    elif a == 'Aa':
        temp2 = random.randint(1,2)
        if temp2 == 1:
            temp1 = random.randint(0,25)
            return abc_list[temp1]
        elif temp2 == 2:
            temp1 = random.randint(0,25)
            return ABC_list[temp1]
    #全混
    elif a == 'Aa1':
        temp2 = random.randint(1,3)
        if temp2 == 1:
            temp1 = random.randint(0,25)
            return abc_list[temp1]
        elif temp2 == 2:
            temp1 = random.randint(0,25)
            return ABC_list[temp2]
        elif temp2 == 3:
            temp1 = random.randint(0,9)
            return temp1

#主程序
#转译类型参数
if m1 == '1':
    m1 = 'a'
elif m1 == '2':
    m1 = 'A'
elif m1 == '3':
    m1 = '1'
elif m1 == '4':
    m1 = 'A1'
elif m1 == '5':
    m1 = 'a1'
elif m1 == '6':
    m1 = 'Aa1'
elif m1 == '7':
    m1 = 'Aa'
#输出并判断
print('游戏开始')
if m2 == '2':
    while True:
        r = abc(m1)
        r = str(r)
        temp_r = input(r)
        if 'exit' == str(temp_r):
            print('你打了',everynum,'个字母或数字,其中正确:',t,'错误:',e)
            print('游戏结束')
            if e > t:
                for i in range(5):
                    print('菜！就多练，以前是以前，现在是现在！')
            sys.exit()
        if r == str(temp_r):
            t += 1
            everynum += 1
            print('正确','目前正确数量:',t,'错误数量:',e)
        else:
            e += 1
            everynum += 1
            print('错误','目前正确数量:',t,'错误数量:',e)
elif m2 == '1':
    print('目前是有限模式，当设定的数量达到时自动退出，提前退出请键入exit','设定量为:',m2_sys)
    for i in range(int(m2_sys)):
        r = abc(m1)
        temp_r = input(r)
        if 'exit' == str(temp_r):
            print('你打了',everynum,'个字母或数字,其中正确:',t,'错误:',e,'剩余:',int(m2_sys)-everynum,'总量:',m2_sys)
            print('游戏结束')
            if t < e:
                for i in range(5):
                    print('菜！就多练，以前是以前，现在是现在！')
            sys.exit()
        if r == str(temp_r):
            t += 1
            everynum += 1
            print('正确','目前正确数量:',t,'错误数量:',e,'已打:',everynum,'剩余:',int(m2_sys)-everynum,'总量:',m2_sys)
        else:
            e += 1
            everynum += 1
            print('错误','目前正确数量:',t,'错误数量:',e,'已打:',everynum,'剩余:',int(m2_sys)-everynum,'总量:',m2_sys)
    print('恭喜！完成了目标','已打:',everynum,'总量:',m2_sys,'正确数量:',t,'错误数量:',e)
    if t < e:
        for i in range(5):
            print('菜！就多练，以前是以前，现在是现在！')
else:
    print('似乎没有运行成功，请重试')
print('运行结束')