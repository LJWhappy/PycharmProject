# print ('世界')
# a=input('输入第一一个数字')
# b=input('输入第二个数字')
# num=int(a)+int(b)
# print('两数之和为：')
# print('数字{0}和数字{1}相加结果为{2}'.format(a,b,num))
# 平方根
# import math
# number = float(input("请输入一个数字: "))
# number_sqrt =  (math.sqrt(number))
# print('%0.3f 的平方根为 %0.3f '%(number,number_sqrt))
# print('number_sqrt is %.3f'%(number_sqrt))
# print('number_sqrt is {0}'.format(number_sqrt))
#二次函数
# print("计算三角形面积，请输入三边的值")
# a=float(input('请输入a值'))
# b=float(input('请输入b值'))
# c=float(input('请输入c值'))
# if a+b>c and a-b<c:
#    print("该三角形成立")
#    P=(a+b+c)/2
#    S =float((P*(P-a)*(P-b)*(P-c))**0.5)
#    print('面积 s= %0.3f' %(S))
# else:
#     print("该三角形不成立")
#随机数生成
# import random
# a=0
# while(a<10):
#     print("随机数 %d 是 %.0f" %(a,random.random()*100))
#     a=a+1
#交换变量
#可用添加一个新的变量来进行交换，也可直接交换
# a=input("input a:")
# b=input("input b:")
#
    # c=a
    # a=b
    # b=c
#
# a,b=b,a
# print("a,b,swap后的值为{0}，{1}".format(a,b))
#定义函数
# def is_number(s):
#   try:
#       float(s)
#       return True
#   except ValueError:
#       pass
#   try:
#       import unicodedata
#       unicodedata.numeric(s)
#       return True
#   except(TypeError,ValueError):
#       pass
#   return False
# print(is_number('asd'))
# print(is_number('123'))
# print(is_number('-1.37'))
# print(is_number('小羊'))
# print(is_number('๒'))
#判断奇数偶数
# def judge_number(s):
#     try:
#         if s%2==0:
#             print('{0}是偶数'.format(s))
#         else:
#             print('{0}是奇数'.format(s))
#     except ValueError:
#         pass
# judge_number(5)
# judge_number(6)
#判断闰年
# def is_reyear(year):
#     try:
#         if year%4==0 and year%100!=0:
#             print("此年为普通闰年")
#         else:
#             print("今年不是普通闰年")
#     except ValueError:
#         pass
#     try:
#         if year%400==0:
#           print("今年为世界闰年")
#         else:
#           print("今年不是世纪闰年")
#     except ValueError:
#         pass
# is_reyear(2000)
#最大值函数max（a,d,s,s,f,）
#而elif后面的命令是根据上一个if是否运行，如果运行了，elif则略过
#print(max(5,1,2,3,4,9,10,66))
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and j!=i and j!=k:
#                 num =i*100+j*10+k
#                 print(num)
# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
# 可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，
# 超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# i=int(input('净利润:'))
# profit=[1000000,600000,400000,200000,100000,0]
# rate=[0.01,0.015,0.03,0.05,0.075,0.1]
# r=0
# for time in range(0,6):
#     if i>profit[time]:
#         r+=(i-profit[time])*rate[time]
#         print((i-profit[time])*rate[time])
#         i=profit[time]
# print(r)
# 一个整数，它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？完全平方指用一个整数乘以自己例如1*1，2*2，3*3等
# 程序分析：
#
# 假设该数为 x。
#
# 1、则：x + 100 = n2, x + 100 + 168 = m2
#
# 2、计算等式：m2 - n2 = (m + n)(m - n) = 168
#
# 3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
#
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
#
# 5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
#
# 6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
#
# 7、接下来将 i 的所有数字循环计算即可。
# 输入某年某月某日，判断这一天是这一年的第几天？
# year=int(input('year:'))
# month=int(input('month:'))
# day=int(input('day:'))
# zmonth=[0,31,59,90,120,151,181,212,243,273,304,334]
# runmonth=[0,31,60,91,121,152,182,213,244,274,305,335]
# if(year%4==0 and year%100!=0 or year%400==0):
#     daytime=runmonth[month-1]+day
# else:
#     daytime=zmonth[month-1]+day
# print(daytime)
# 输入三个整数x,y,z，请把这三个数由小到大输出。
# x=int(input('x:'))
# y=int(input('y:'))
# z=int(input('z:'))
# l = []
# for i in range(3):
#     x = int(input('integer:\n'))
#     l.append(x)  #用于列表中元素的的添加
# l.sort()#用于排序的函数
# print (l)
# classmates = ('Michael', 'Bob', 'Tracy')
# print('classmates =', classmates)
# print('len(classmates) =', len(classmates))
# print('classmates[0] =', classmates[0])
# print('classmates[1] =', classmates[1])
# print('classmates[2] =', classmates[2])
# print('classmates[-1] =', classmates[-1])

# cannot modify tuple:
# classmates[0] = 'Adam'
# tuple 不变性是指tuple每一个元素指向永远不变，变换的是list里面的值
# names=['bart','lisa','Adam']
# for x in names:
#
#     print('hello',x)
#     continue
#     print('nihao')
#字典相当于一个map  一个键只能对应一个键值
# d={'make':'haha','bob':'mary'}
# d['bob']='xixi'
# print(d['bob'])
# d = {
#     'Michael': 95,
#     'Bob': 75,
#     'Tracy': 85
# }
# print('d[\'Michael\'] =', d['Michael'])
# print('d[\'Bob\'] =', d['Bob'])
# print('d[\'Tracy\'] =', d['Tracy'])
# print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
# s1 = set([1, 1, 2, 2, 3, 3])
# print(s1)
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)
# def power(x,n):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# 函数
# print(power(2,4))
# def print_scores(**kw):
#     print('      Name  Score')
#     print('------------------')
#     for name, score in kw.items():
#         print('%10s  %d' % (name, score))
#     print()
#
# print_scores(Adam=99, Lisa=88, Bart=77)
#
# data = {
#     'Adam Lee': 99,
#     'Lisa S': 88,
#     'F.Bart': 77
# }
#
# print_scores(**data)
#
# def print_info(name, *, gender, city='Beijing', age):
#     print('Personal Info')
#     print('---------------')
#     print('   Name: %s' % name)
#     print(' Gender: %s' % gender)
#     print('   City: %s' % city)
#     print('    Age: %s' % age)
#     print()
#
# print_info('Bob', gender='male', age=20)
# print_info('Lisa', gender='female', city='Shanghai', age=18)
# 一百例题6-10
# 斐波那契数列
# def feibo(n):
#     a,b=1,1
#     for i in range(n-1):
#          a,b=b,a+b
#          print(a,b)
#          return a
# print(feibo(0))
#输出多个斐波那契数列
# def naqi(n):
#     a,b=1,1
#     l=[1,1]
#     #range(x,y)从x开始Y结束但不包括y
#     #for循环里面的数第一个从2开始是是因为数组里面已经有两个数字的占用了0，1下标
#     #第二个for循环只要加8个数字就可以了
#     for i in range(2,n):
#          for j in range(n-2):
#             a,b=b,a+b
#             l.append(a)
#     return l
# print(naqi(10))

#递归算出斐波
# def diguifeibo(n):
#    if n==1 or n==2:
#        return 1
#    return diguifeibo(n-1)+diguifeibo(n-2)
# print(diguifeibo(10))

#将一个列表中的内容复制到另一个列表中
# a=[1,2,3]
# b=[]
# for i in range(3):
#     #因为b是一个空的list所以添加进去的是一个顺序添加
#     b.append(a[i])
# print(b)


#简单的方法
# a=[1,2,3]
# b=a[:]
# print('\n')
# print(b)
#9*9乘法口诀表
# for i in range(1,10):
#
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,end='')
#     print('\n')

#暂停一秒输出，dict中的key值不可以相同
# import time
# late={'‘姓名’':'张三','年龄':'18','32':'18','2':'18','1':'18','4':'18'}
# for key,value in dict.items(late):
#     print(key,value)
#     time.sleep(0.5)#暂停一秒

#暂停一秒输出并格式化当前时间
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.sleep(2)
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#利用 递归函数计算阶乘
# def jiecheng(n):
#     if n==1:
#         return 1#掉了1这一步很关键
#     return jiecheng(n-1)*n
# print(jiecheng(3))
#普通方法计算阶乘
# def jiecheng(n):
#     if n==1:
#         return 1
#     s=1
#     for i in range(1,n+1):
#      s=s*i
#     return s
# print(jiecheng(3))
#汉若塔 递归计算
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)
#
# move(4, 'A', 'B', 'C')
#切片函数将李斯特切片为好几个段并取出其中的部分
# L=[1,2,3,5,6,7]
#倒着切片的时候必须从前往最后一个切片，要不就啥也没有
# print(L[-3:-2])
# print(L[1:4])
# [:]是可以复制一个list
# 每几个数取一个[::n]第一个数一定取到
#print(L[::2])
#前10个数，每两个取一个：
# print(L[:10:2])

# f1 = 1
# f2 = 1
# for i in range(1,22):
#     print ('%12ld %12ld' % (f1,f2))
#     f1 = f1 + f2
#     f2 = f1 + f2

#11
# def feibo(n):
#     f=[1,1]
#     for i in range (2,n):
#       f[i]=f[-1]+f[-2]
#       f.append(f[i])
#       print(f)
# #print(feibo(10))
# feibo(10)
#切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# print('L[0:3] =', L[0:3])
# print('L[:3] =', L[:3])
# print('L[1:3] =', L[1:3])
# print('L[-2:] =', L[-2:])
#
# R = list(range(100))
# print('R[:10] =', R[:10])
# print('R[-10:] =', R[-10:])
# print('R[10:20] =', R[10:20])
# print('R[:10:2] =', R[:10:2])
# print('R[::5] =', R[::5])
#迭代 遍历list 或者tuple  dict的遍历与众不同  字符串也可作为iew迭代对象
# dict={1:2,3:4,6:5}
# truple=(1,)  #能用truple就用他代替list
# for key in dict:
#     print(key)
# print()
# for k,v in dict.items():
#     print(k,v)
# print()
# for v in dict.values():
#     print(v)
# print()
#对list进行遍历并求出最大值和最小值，然后将结果放回tuple
# list=[1,2,3,4,5,6]
# for i in range(0,len(list)):
#     Max=list[0]
#     Min=list[0]
#     if Min>list[i]:
#         Min=list[i]
#     if Max<=list[i]:
#         Max=list[i]
#     tuple=({'Max:':Max,'Min:':Min})
# print(tuple)
# list=[i for i in range(1,12)]
# print(list)
# list=[x*x for x  in range(1,11)]
# print(list)
# list=[i for i in range(1,100) if i%2==0]
# print(len(list))
# for i in range(len(list)):
#     if i%5==0:
#       print('\n')
#     print(list[i],'\t',end='')
# L1 = ['Hello', 'World', 18, 'Apple', None]
#
# L2 = [item.lower() for item in L1 if isinstance(item,str)]
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')
# strings = ['Right', 'SAID', 'Fred']
# strings = [item.lower() for item in strings]
# print(strings)
#
# print([x * x for x in range(1, 11)])
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])
#
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print([k + '=' + v for k, v in d.items()])
#
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
#生成器
# list=[x*x for x  in range(1,11)]
# print(list)
# l=(x*x for x  in range(1,11))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# for i in l:
#     print(i)
#判断素数
# import math
# l=[]
# k=1
# a=0
# for i in range(101,201):
#    for j in range(2,int(math.sqrt(i))+1):
#       if (i%j) == 0:
#           k=0
#           break
#    if(k==1):
#      a=a+1
#      l.append(i)
#    k=1#此处K必须更改为1
# print(l)
# print('总共有：',a)
#判断水仙花数

# for num in range(100,1000):
#     i=num//100
#     j=num//10%10
#     k=num%10
#     if num == i**3+j**3+k**3:
#        print(num)
#将一个正整数分解质因数
# def reduceNum(n):
#     print ('{} = '.format(n))
#     if not isinstance(n, int) or n <= 0 :
#         print ('请输入一个正确的数字 !')
#         exit(0)
#     elif n in [1] :
#         print ('{}'.format(n))
#     while n not in [1] : # 循环保证递归
#         for index in  range(2, n + 1) :
#             if n % index == 0:
#                 n /= index # n 等于 n/index
#                 if n == 1:
#                     print (index)
#                 else : # index 一定是素数
#                     print ('{} *'.format(index))
#                 break
# reduceNum(90)
#利用条件运算嵌套完成
# print("请输入分数：")
# grade=int(input())
# print((grade>=90)?A:((60<grade<89)?B:C))

# n = num = int(input('请输入一个数字：'))  # 用num保留初始值
# f = []  # 存放质因数的列表
#
# for j in range(int(num / 2) + 1):  # 判断次数仅需该数字的一半多1次
#     for i in range(2, n):
#         t = n % i  # i不能是n本身
#         if t == 0:  # 若能整除
#             f.append(i)  # 则表示i是质因数
#             n = n // i  # 除以质因数后的n重新进入判断，注意应用两个除号，使n保持整数
#             break  # 找到1个质因数后马上break，防止非质数却可以整除的数字进入质因数列表
#
# if len(f) == 0:  # 若一个质因数也没有
#     print('该数字没有任何质因数。')
# else:  # 若至少有一个质因数
#     f.append(n)  # 此时n已被某个质因数整除过，最后一个n也是其中一个质因数
#     f.sort()  # 排下序
#     print('%d=%d' % (num, f[0]), end='')
#     for i in range(1, len(f)):
#         print('*%d' % f[i], end='')
#质因数的算法是根据先对该数从2到该数的一半进行取余看是否能够整除，若能整除则进行一个append,然后将该数整除刚刚获取的质因数，

# n=num=int(input())
# s=[]
# for i in range(int(num/2+1)):
#   for i in range(2,num):
#     t= num % i
#     if t==0:
#         s.append(i)
#         num=num//i
#         break
# if len(s)==0:
#     print("no zhi shu")
# else:
#   s.append(num)
#   s.sort()
#   print("%d=%d" %(n,s[0]),end='')
#   for i in range(1,len(s)):
#     print('*',s[i],end='')

# def triangles():
#     list=[1,1]
#     print(1)
#     print(1,1)
#     for i in range(3,11):
#        if(i%2==0):
#            print(i)
# def f(x):
#     return x*x
# r=map(f,[1,2,3,4,5,6,])
# print(list(r))
# def normalize(name):
#    return  name[0].upper()+name[1:].lower()
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
# from functools import reduce
# def prod(L):
#     return  reduce(lambda x, y: x*y, L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#      print('测试成功!')
# else:
#      print('测试失败!')
# from functools import reduce
#
# CHAR_TO_INT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9
# }
#
# def str2int(s):
#     ints = map(lambda ch: CHAR_TO_INT[ch], s)
#     return reduce(lambda x, y: x * 10 + y, ints)
#
# print(str2int('0'))
# print(str2int('12300'))
# print(str2int('0012345'))
#
# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }
#
# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#     return reduce(to_float, nums, 0.0)
#
# print(str2float('0'))
# print(str2float('123.456'))
# print(str2float('123.45600'))
# print(str2float('0.1234'))
# print(str2float('.1234'))
# print(str2float('120.0034'))
#过滤掉一个数列中的偶数
# def is_oushu(n):
#    return  n%2==1
# print(list(filter(is_oushu,[1,2,3,4,5,6,7,8,9])))

#删除字符串中的一空传
# def not_empty(s):
#     return s and s.strip('') and s.strip('  ')
#
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# def is_odd(n):
#     return n % 2 == 1
#
#
# tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# newlist = list(tmplist)
# print(newlist)stripstrip
#函数式编成
# f=abs
# print(f(-9))
# 排序算法：
# import math
# print(sorted())
#忽略大小写的函数
#print(sorted(['bob','Zoo','Jhf'],key=str.lower))
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0].lower()
# def by_score(t):
#     return t[1]
# print(sorted(L,key=by_name))
# print(sorted(L,key=by_score))
#因为L传进来时是一对键值所以t[0]表示前键，t[1]表示后建
#高jie函数

##########
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# count写入的是（f,f,f）
# 因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果为9
#相当于返回闭包
# f1,f2,f3= count()
# print(f1(),f2(),f3())
# def is_odd():
#     for i in range(1,20):
#      print lambda x : x%2==1
# print(is_odd())
# import functools
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# now()
#
# def logger(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @logger('DEBUG')
# def today():
#     print('2015-3-25')
#
# today()
# print(today.__name__)
#
# import datetime
# print(datetime.date.today().strftime('%d-%m-%Y'))
# #创建日期对象
# date =datetime.date.today()
# print(date)
#  # 日期算术运算
# miyazakiBirthNextDay = date + datetime.timedelta(days=1)
# print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
#使用while
# import string
# s=input('请输入一个字符串：')
# zimu=0
# space=0
# number=0
# otherchar=0
# for i in range(0,len(s)):
#     if s[i].isalpha():
#          zimu=zimu+1
#     elif s[i].isspace():
#         space=space+1
#     elif s[i].isalnum():
#         number=number+1
#     else:
#         otherchar=otherchar+1
# print(zimu,space,number,otherchar)

#求s=a+aa+aaa+aaaa...
# a=int(input('请输入变量a'))
# n=int(input('请输入计算范围'))
# sum=0
# num=[]
# num1=[]
# sumnum=0
# s=0
# num1[0]=num1.append(a)
# for i in range(n):
#      s=(10**(i))*a
#      num.append(s)
#      print(num)
# for j in range(1,len(num)):
#    for k in range(0,j+1):
#      sumnum=num[k]+sumnum
#    num1[j].append(sumnum)
#
# print(num1)
# for w in range(len(num)):
#     sum=num[w]+sum
# print(sum)
# from functools import reduce
# for count in range(n):
#     sum=sum+a
#     a=a*10
#     num.append(sum)
# Sn=0
# Sn=reduce(lambda a,b:a+b,num)
# print(Sn)
# 跳过19，14
# high=100
# for i in range(1,3):
#     h=high+(2)*100/(2**i)
# print(high)
# x2 = 1
# range 一版为三个参数，最后一个写为-1时表示到着      9.8.7.。。
# for day in range(9,0,-1):
#     x1 = (x2 + 1) * 2
#     x2 = x1
# print (x1)
# base=几进制
# def int2(x, base=16):
#     return int(x, base)
# print(int2('10102'))
# import functools
# ints=functools.partial(int ,base=16)
# print(ints('123'))
# print(ints('123',base=10))
######################################################
# 类的定义和实现
# class Student (object):
#     def __init__(self,name,score,gender):
#         # 对name只能进行内部的访问因为前面加了_
#         self._name=name
#         self.score=score
#         self._gender=gender
#     def get_gender(self):
#         return self._gender
#     def set_gender(self,gender):
#         self._gender=gender
#     # 加入get，set方法就可以让外部进行访问
#     def get_name(self):
#         return self._name
#     #定义set方法是因为i可以对参数做检查，避免传入无效参数
#     def set_score(self,name):
#         self._name=name
#     def get_score(self):
#         return self.score
#     def print_sco(std):
#         print('%s:%s'%(std.name,std.score))
# bart = Student('Bart Simpson', 59,'female')
# # print(bart.name)
# print(bart.score)
# bart.score=100
# print(bart.score)
# #__xxx__是特殊变量   _xxx是可以被访问但是请把此变量视为私有变量
# # __xxx双下划线开头的实例
#
#
# #此处更改的不是类里面的变量，bart.__name和内部的name 是两个变量
# bart.__name='haha'
# print(bart.__name)
# print(bart.get_name())
# #此处对于成绩的更改是可以的因为不是内部的变量
# bart.score=10
# print(bart.get_score())
# bart.set_gender('male')
# print(bart.get_gender())
##########################################################
#继承和多态
# class Animal(object):
#     def run(self):
#         print('animal id running!')
#     def run_twice(animal):
#         animal.run()
#         animal.run()
# class Dog(Animal):
#     def run(self):
#         print('dog is running!')
# class Cat(Animal):
#     def run(self):
#         print('cat is running!')
# dog=Dog()
# cat=Cat()
# dog.run_twice()
# # dog.run()
#
# #判断某个类型可以用isinstance()
# print(isinstance(dog,Dog))
# print(isinstance(dog,Animal))
# #开闭原则
# # 对扩展开放：允许新增子类
# # 对修改封闭：不需要修改一览animal的类型
# #动态语言决定了继承不像静态语言那样，如果存在相同的类方法就可以视为鸭子类
# #如何知道对象的类型和方法使用type（）
# print(type(dog))
# print(type(cat))
# if type(dog)==type(cat):
#     print('dog type is same as cat')
# print(dir(dog))
# class MyObject(object):
#
#     def __init__(self):
#         self.x = 9
#
#     def power(self):
#         return self.x * self.x
#
# obj = MyObject()
#
# print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
# print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
# setattr(obj, 'y', 19) # 设置一个属性'y'
# print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
# print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
# print('obj.y =', obj.y) # 获取属性'y'
#
# print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404
#
# f = getattr(obj, 'power') # 获取属性'power'
# print(f)
# print(f())
###########################################################################
#实例属性和类属性
#为了统计学生人数，可以给Student类增加一个类属性，
# 每创建一个实例，该属性自动增加：
# class Student(object):
#      count=0
#      def __init__(self,name,sex):
#          self.name=name
#          self.sex=sex
#          self.__set_count()
#      def __set_count(self):
#          Student.count +=1
# #s=Student('haha','man')
# # y=Student('xyr')
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
#################################################################
# 还可以尝试给实例绑定一个方法：
#
# >>> def set_age(self, age): # 定义一个函数作为实例方法
# ...     self.age = age
# ...
# >>> from types import MethodType
# >>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
# >>> s.set_age(25) # 调用实例方法
# >>> s.age # 测试结果
# 25
# 限制实例属性,比如只允许对student实例添加name和age
# 为了达到限制的木的，python允许定义一个特殊的__slots__
# class Student(object):
#     __slots__ = ('name','age')
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
# class Xiao(Student):
#     def run(self):
#         print('asd')
# b = Xiao('xiao','man',10)
# print(b.score)
#s=Student('xiao','man',10)
# 报错哦'Student' object has no attribute 'score'
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#
# class GraduateStudent(Student):
#     pass
#
# s = Student() # 创建新的实例
# s.name = 'Michael' # 绑定属性'name'
# s.age = 25 # 绑定属性'age'
# # ERROR: AttributeError: 'Student' object has no attribute 'score'
# try:
#     s.score = 99
# except AttributeError as e:
#     print('AttributeError:', e)
#
# g = GraduateStudent()
# g.score = 99
# print('g.score =', g.score)
############################################################
#get  set方法可以检查参数属性
# @property  负责把一个方法变成属性调用
# class Screen(object):
#     # def __init__(self,width,height):
#     #     self.width=width
#     #     self.height=height
#     @property
#     def width(self):
#         return self.width
#     @width.setter
#     def width(self,value):
#         self._width=value
#     @property
#     def height(self):
#         return self.height
#     @height.setter
#     def height(self, value2):
#         self.height = value2
#     @property
#     def resolution(self):
#         return self._width * self.height
# s = Screen(1024,768)
# class Screen(object) :
#     @property
#     def width(self) :
#         return self._width
#
#     @width.setter
#     def width(self,valuer) :
#         if not isinstance(valuer,int):
#             raise ValueError('score must be an integer')
#         if valuer < 0 :
#             raise ValueError('score must over zero')
#         self._width=valuer
#
#     @property
#     def height(self) :
#         return self._height
#
#     @height.setter
#     def height(self,number) :
#         if not isinstance(number,int) :
#             raise ValueError('score must be an integer')
#         if number < 0 :
#             raise ValueError('score must be an zero')
#         self._height = number
#
#     @property
#     def resolution(self):
#         return self._width * self._height
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')
#########################################################
#多继承，在继承的类中在加上两个类
# class Dog(Mammal, Runnable):
#     pass
# Python自带了TCPServer和UDPServer这两类网络服务，而要同时服
# 务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和
# ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
# 比如，编写一个多进程模式的TCP服务，定义如下：
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass
# 编写一个多线程模式的UDP服务，定义如下：
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass
# 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass

# def __str__(self):
#     return 'Student object (name=%s)' % self.name
# 如果一个类想被用于for ... in循环，类似list或tuple那样，
# 就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
# Python的for循环就会不断调用该迭代对象的__next__()
# 方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# ######要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b
#       def __getitem__(self, n):
#           a, b = 1, 1
#           for x in range(n):
#              a, b = b, a + b
#           return a
#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int):  # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):  # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
# f = Fib()
# print(f[0:5])
#

# class Student(object):
#
#     def __init__(self):
#         self.name = 'Michael'
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
# 比如定义Student类当调用不存在的属性时，比如score，Python解释器
# 会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们
# 就有机会返回score的值
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。


#     def __getattr__(self, attr):
#         if attr=='score':
#             return 99
#         if attr=='age':
#             return lambda: 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#
# s = Student()
# print(s.name)
# print(s.score)
# print(s.age())
# # AttributeError: 'Student' object has no attribute 'grade'
# print(s.grade)


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     # 定义一个__call__()方法，就可以直接对实例进行调用
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
# s = Student('Michael')
# s()


# from enum import Enum, unique
#
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# day1 = Weekday.Mon
#
# print('day1 =', day1)
# print('Weekday.Tue =', Weekday.Tue)
# print('Weekday[\'Tue\'] =', Weekday['Tue'])
# print('Weekday.Tue.value =', Weekday.Tue.value)
# print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
# print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
# print('day1 == Weekday(1) ?', day1 == Weekday(1))
#
# for name, member in Weekday.__members__.items():
#     print(name, '=>', member)
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
########################################################
# class Hello (object):
#     def hello(self,name='w'):
#         print('nihao %s'% name)
# h=Hello()
# h.hello('xiaoyang')
# type()函数可以查寻类型变量的类型   我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# def fn(self,name='world'):
#     print('Helllo,%s.' % name)
# def fm(self,age=12):
#     print('i am %d years old'% age)
# Hello =type('Hello',(object,),dict(hello=fn,old=fm))
# h=Hello()
# h.hello()
# h.old()
# print('type(Hello) =', type(Hello))
# print('type(h) =', type(h))
####################
  # metaclass是创建类，所以必须从`type`类型派生：
# class ListMetaclass(type):
#       def __new__(cls, name, bases, attrs):
#           attrs['add'] = lambda self, value: self.append(value)
#           return type.__new__(cls, name, bases, attrs)
#
#   # 指示使用ListMetaclass来定制类
# class MyList(list, metaclass=ListMetaclass):
#       pass
#
# L = MyList()
# L.add(1)
# L.add(2)
# L.add(3)
# L.add('END')
# print(L)
# import logging
# def foo():
#     try:
#         print('jin ru try')
#         r=10/0
#         print('result',r)
#         #除数为0的错误   except是错误处理代码块
#     except ZeroDivisionError as e:
#         print('chu shu chu cuo')
#     finally:
#         print('finally')
# foo()
# print('end')
#若没有发生错误，则后续的except不会执行，但是finally如果存在则一定会被执行
#错误处理模块可以有多个处理方法既有多个 except
#常见的错误类型和继承关系看这里：
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# from functools import reduce
#
# def str2num(s):
#     return float(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = int(calc('100 + 200 + 345'))
#     print('100 + 200 + 345 =', r)
#     r = int(calc('99 + 88 + 7.6'))
#     print('99 + 88 + 7.6 =', r)
#
# main()
##########################################
#错误处理
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# def foo(s):
#       try:
#         return 10 / int(s)
#       except   ZeroDivisionError as e:
#         print('zerodivisionerror')
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()

# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo('0')
#     错误调试法
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
# import pdb
#
# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)

#单元测试
# import  unittest
# class Student(object):
#      def __init__(self, name, score):
#              self.name = name
#              self.score = score
#      def get_grade(self):
#              if self.score >= 60:
#                  return 'B'
#              if self.score >= 80:
#                   return 'A'
#              return 'C'
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
# if __name__ == '__main__':
#     unittest.main()
# 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，
# 又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# x=1
# for i in range(9,0,-1):
#     a=2*(x+1)
#     x=a
# print(a)
########################################################################
# 题目：两个乒乓球队进行比赛，各出三人。
# 甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，
# 请编程序找出三队赛手的名单。
# for i in range(ord('x'),ord('z') + 1):
#     for j in range(ord('x'),ord('z') + 1):
#         if i != j:
#             for k in range(ord('x'),ord('z') + 1):
#                 if (i != k) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)) )
#############################################################################
# n=int(input('input the lever'))
# j,k = 1,1
# for i in range(1,n+1):
#     if i<=n/2:
#         for j in range(j,2*j-1):
#             print('*',end='')
#         print()
#     if i>n/2:
#         for k in range(k-2,1):
#             print('*',end=''
# with open('/home/happygirl/桌面/test','r') as f:
#     print(f.read())
#     # print(f.readline())
#     f.close()
# with open('/home/happygirl/桌面/test','a',) as w:
#     w.write('learning wirte with append')
# with open('/home/happygirl/桌面/test', 'r') as q:
#     print(q.read())
#     q.close()
# from datetime import datetime
#
# with open('/home/happygirl/桌面/test', 'w') as f:
#     f.write('今天是 ')
#     f.write(datetime.now().strftime('%Y-%m-%d'))
#
# with open('/home/happygirl/桌面/test', 'r') as f:
#     s = f.read()
#     print('open for read...')
#     print(s)
#
# with open('/home/happygirl/桌面/test', 'rb') as f:
#     s = f.read()
#     print('open as binary for read...')
#     print(s)
# from io import StringIO
# # f=StringIO()
# # f.write('hello')
# # f.write(' ')
# # f.write('world!')
# # print(f.getvalue())
# f=StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s=f.readline()
#     if s=='':  #当便利完整个列表时break跳出永贞的循环
#         break
#     print(s.strip())
# from io import BytesIO
# f=BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())
####################
# 文件的操作
# import os
# print(os.environ)
#cha kan dang qian mu lu de  jue dui lu jing
# print(os.path.abspath('.'))
# #os.
# os.path.join('/home/happygirl/PycharmProject','testdir')
# #os.mkdir('/home/happygirl/PycharmProject/testdir1')
# #delete
# #os.rmdir('/home/happygirl/PycharmProject/testdir1')
# print(os.path.splitext('/home/happygirl/PycharmProject/test'))
# #现实列表下所有的文件
# print([testdir1 for testdir1 in os.listdir('.') if os.path.isdir(testdir1)])
# #显示列表下所有的.py文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
########################################序列化
# import  pickle
# from io import StringIO
# d=dict(name='Bob',age=20,score=88)
# #pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# # pickle.dumps(d)
# f=open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()
# f=open('dump.txt','rb')
# print(f.read())

# import pickle
#
# d = dict(name='Bob', age=20, score=88)
# data = pickle.dumps(d)
# print(data)
#
# reborn = pickle.loads(data)
# print(reborn)


# import json
#
# d = dict(name='Bob', age=20, score=88)
# data = json.dumps(d)
# print('JSON Data is a str:', data)
# reborn = json.loads(data)
# print(reborn)
#
# class Student(object):
#
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def __str__(self):
#         return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)
#
# s = Student('Bob', 20, 88)
# std_data = json.dumps(s, default=lambda obj: obj.__dict__)
# print('Dump Student:', std_data)
# rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
# print(rebuild)
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
# if __name__=='__main__':
#     print('父进程 ',os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print('Child process wll start.')
#     p.start()
#     p.join()
#     print('Child process will end')
#创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# from multiprocessing import Pool
# import os, time, random
# #os模块就是对操作系统进行操作，使用该模块必须先导入模块：
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(9):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
#import threading,time
# def loop():
#     print('threading %s' % threading.current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print('thread %s     %s' %(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread end' %threading.current_thread().name)
# print('thread w %s is running...' %threading.current_thread().name)
# t=threading.Thread(target=loop,name='hahha')
# t.start()
# t.join()
# print('thread w end ' % threading.current_thread().name)
# balance=0
# lock=threading.Lock()
# def change_it(n):
#     global balance
#     balance = balance+n
#     balance = balance-n
# def run_thread(n):
#     for i in range(10000):
#         #先获取锁
#         lock.acquire()
#         try:
#          change_it(n)
#         finally:
#             lock.release()
# t=threading.Thread(target='run_thread',args=(5))
# t1=threading.Thread(target='run_thread', args=(40))
# t.start()
# t.join()
# t1.start()
# t1.join()
# print(balance)
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

#threadlocal
# import threading
# local_school=threading.local
# def process_student():
#     std=local_school.tu
#     print('hello,%s(in %s)'%(std,threading.current_thread().name))
# def process_thread(name):
#     local_school.tu=name
#     process_student()
#     #args shi canshu ming name shi xian cheng ming
# t=threading.Thread(target=process_thread,args=('Alice,'),name='Thead_A')
# t1=threading.Thread(target=process_thread,args=('bob'),name='thread_B')
# t.start()
# t.join()
# t1.start()
# t1.join()
# import random, time, queue
# from multiprocessing.managers import BaseManager
#
# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()
#
# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# # 启动Queue:
# manager.start()
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')



# import time, sys, queue
# from multiprocessing.managers import BaseManager
#
# # 创建类似的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
# # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')
#
# # 连接到服务器，也就是运行task_master.py的机器:
# server_addr = '127.0.0.1'
# print('Connect to server %s...' % server_addr)
# # 端口和验证码注意保持与task_master.py设置的完全一致:
# m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# # 从网络连接:
# m.connect()
# # 获取Queue的对象:
# task = m.get_task_queue()
# result = m.get_result_queue()
# # 从task队列取任务,并把结果写入result队列:
# for i in range(10):
#     try:
#         n = task.get(timeout=1)
#         print('run task %d * %d...' % (n, n))
#         r = '%d * %d = %d' % (n, n, n*n)
#         time.sleep(1)
#         result.put(r)
#     except Queue.Empty:
#         print('task queue is empty.')
# # 处理结束:
# print('worker exit.')
# import re
# if re.match(r'^py$','py'):
#     print('ok')
# import re
# t='19:05:30'
# m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# print(m.groups())
#正则表达式判断邮箱
# import re
# def eamil(eamil):
#     re_eamil=re.compile(r'^(\w+|\d+|\?)(\@)(\w*)(\.com)$')
#     if re_eamil.match(eamil):
#         print('pipei')
#         print(re_eamil.match(eamil).groups())
#         a=re_eamil.match(eamil).group(1)
#         return a
#     else:
#         print('loser')
# em=input('input eamil:')
# name=eamil(em)
# print('the user name is: %s'% name)
# import struct
#
# bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
#
# print(struct.unpack('<ccIIIIIIHH', bmp_header))
#hashlib 加密算法
#hexdigest()是作为十六进制数据字符串
#digest()是作为二进制数据字符串
# md5=hashlib.md5()
# md5.update("it is the first time to use md5 ")
# print(md5.hexdigest())
#根据用户输入的口令，计算出存储在数据库中的MD5口令：
# import hashlib
# def cla_md5(password):
#     pw=hashlib.md5()
#     pw.update(password.encode('utf-8'))
#     return pw.hexdigest()
# password=input("input password")
# passwordmd5=cla_md5(password)
# print(passwordmd5)
#计算圆周率
# list[i].append(jinum)#应该写为list.append(jinum)
# IndexError: list index out of range
# def pi(n):
#     list=[]
#     for i in range(0,n):
#         jinum=2*i+1
#         list.append(jinum)
#     print(list)
#     listn=[]
#     for j in range(0,n+1):
#         listn.append(list.)
#     print(listn)
#     listzf=[]
#     for k in range(0,n):
#         if(k%2==0):
#             listzf[k]=4/(-listn[k])
#         else:
#             listzf[k]=4/listn[k]
#         sum=listzf[k]+sum
#     print(listzf)
#     print('pi=',sum)
# pi(9)
# import itertools
# n=int(input("please input weishu"))
# list1=itertools.count(1,2)
# listnum=itertools.takewhile(lambda x:x<=2*n-1,list1)
# print(list(listnum))
# print(len(list(listnum)))  input 0

# def pi(n):
#     sum = 0
#     natuals = itertools.count(1,2)
#     print(type(natuals))
#     ns = list(itertools.takewhile(lambda x: x <= 2*n-1, natuals))
#     for i in range(n):
#         if i % 2 == 0:
#             sum += (4 / ns[i])
#         else:
#             sum += (-4 / ns[i])
#     return sum
# n=int(input("please input weishu"))
# piis=pi(n)
# print('pi is: %d ',piis)
# def pi(N):
#     natuals = itertools.count(1)
#     ns=itertools.takewhile(lambda x : x<=2*N,natuals)
#     ns_odd=list(filter(lambda x : x%2==1,ns))
#     sum=0
#     #分别除4或-4并求和
#     for i in range(0, len(ns_odd)):
#         if i % 2==0:
#             sum+=4/ns_odd[i]
#         else:
#             sum+=(-4/ns_odd[i])
#     return sum
# print(pi(1000))
# try :
#     f=open('/home/happygirl/桌面/daily','r')
#     f.read()
#     print(f.read())
# finally:
#     f.close()
# for girl/桌面/daily','r') as f:
# from urllib import request
#
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
# from xml.parsers.expat import ParserCreate
# -*- coding:utf-8 -*-
# from xml.parsers.expat import ParserCreate
#
# weather_dict = {}  # 定义天气字典
# which_day = 0  # 哪一天
#
#
# # 定义解析类 这三个函数在廖雪峰老师xml这一节中介绍了
# # 包括三个主要函数：start_element(),end_element(),char_data()
# class WeatherSaxHandler(object):
#     def start_element(self, name, attrs):  # 定义start_element函数
#         global weather_dict, which_day
#
#         if name == 'yweather:location':  # 判断并获取XML文档中地理位置信息
#             weather_dict['city'] = attrs['city']  # 将本行XML代码中'city'属性值赋予字典weather_dict中的'city'
#             weather_dict['country'] = attrs['country']  # 执行结束后此时，weather_dict={'city':'Beijing','country'='China'}
#
#         if name == 'yweather:forecast':  # 同理获取天气预测信息
#             which_day += 1  # 第一天天气，获取气温、天气
#             if which_day == 1:
#                 weather_today = {'text': attrs['text'],
#                            'low': int(attrs['low']),
#                            'high': int(attrs['high'])
#                            }
#                 weather_dict['today'] = weather_today  # 此时weather_dict出现二维字典
#             # weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}}
#
#             elif which_day == 2:    # 第二天相关信息
#                 weather_today = {
#                     'text': attrs['text'],
#                     'low': int(attrs['low']),
#                     'high': int(attrs['high'])
#                 }
#                 weather_dict['tomorrow'] = weather_today
#     # weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}, 'tomorrow': {'text': 'Sunny', 'low': 21, 'high': 34}}
#
#     def end_element(self, name):    # end_element函数
#         pass
#
#     def char_data(self, text):   # char_data函数
#         pass
#
# def parse_weather(xml):
#     handler = WeatherSaxHandler()
#     parser = ParserCreate()
#     parser.StartElementHandler = handler.start_element
#     parser.EndElementHandler = handler.end_element
#     parser.CharacterDataHandler = handler.char_data
#     parser.Parse(xml)
#     return weather_dict
#
#
# # XML文档，输出结果的数据来源
# # 将XML文档赋值给data
#
# data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
# <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
#     <channel>
#         <title>Yahoo! Weather - Beijing, CN</title>
#         <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
#         <yweather:location city="Beijing" region="" country="China"/>
#         <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
#         <yweather:wind chill="28" direction="180" speed="14.48" />
#         <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
#         <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
#         <item>
#             <geo:lat>39.91</geo:lat>
#             <geo:long>116.39</geo:long>
#             <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
#             <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
#             <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
#             <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
#             <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
#             <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
#             <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
#         </item>
#     </channel>
# </rss>
# '''
# # 实例化类
# weather = parse_weather(data)
# # 检查条件是否为True
# assert weather['city'] == 'Beijing', weather['city']
# assert weather['country'] == 'China', weather['country']
# assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
# assert weather['today']['low'] == 20, weather['today']['low']
# assert weather['today']['high'] == 33, weather['today']['high']
# assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
# assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
# assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
# # 打印到屏幕
# print('Weather:', str(weather))
#
#
# class Application(Frame):
#    def _init_(self,master):
#       Frame.__init__(self,master)
#       self.pack()
#       self.creatwindo()
#    def creatwindo(self):
#        self.hellolabel=Label(self,text='hello,world!')
#        self.hellolabel.pack()
#        self.quitButton = Button(self, text='Quit', command=self.quit)
#        self.Button.pack()
# app=Application()
# app.master.title('hello,GUI')
# app.mainloop()


# turtle.width(4)   #设置笔刷宽度
# turtle.forward(200)
# turtle.right(90)
#
# turtle.pencolor('red')
# turtle.forward(100)
# turtle.right(90)
#
# turtle.pencolor('green')
# turtle.forward(200)
# turtle.right(90)
#
# turtle.pencolor('blue')
# turtle.forward(100)
# turtle.right(90)

#绘制星星
# def drawStar(x,y):
#      turtle.pu()
#      turtle.goto(x,y)
#      turtle.pd()
#      turtle.seth(0)
#      for i in range(5):
#          turtle.fd(40)
#          turtle.rt(144)
# for x in range(0,250,250):
#     drawStar(x,0)
# turtle.done()
#绘制星星
# turtle.fillcolor("purple")     #设置填充颜色
# turtle.begin_fill()
# while True:
#     turtle.forward(360)           #每笔前进的长度
#     turtle.right(250)
#     if abs(turtle.pos())<1:            #画笔是不是回到了原点也就是起点
#                break
# turtle.end_fill()
# turtle.done()                           #不加这个绘图结束后将关闭窗口
# 绘制彩色的树
# from tkinter import *
# import turtle
#  #绘制大树彩色
# turtle.colormode(255)#将色彩模式调到RGB
# turtle.lt(90)
# lv=14
# l=120
# s=45
#
# turtle.width(lv)
# r=0
# g=0
# b=0
# turtle.pencolor(r,g,b)
# turtle.penup()
# turtle.bk(l)
# turtle.pendown()
# turtle.fd(l)
#
# def draw_tree(l,level):
#     global r,g,b         #设置全局变量
#     w=turtle.width()
#     turtle.width(w*3.0/4.0)
#     r = r+1
#     g = g+2
#     b = b+3
#     turtle.pencolor(r%200,g%200,b%200)
#     l = 3.0 / 4.0 * l
#
#     turtle.lt(s)
#     turtle.fd(l)
#     if level<lv:
#         draw_tree(l,level+1)
#     turtle.bk(l)
#     turtle.rt(2 * s)
#     turtle.fd(l)
#
#     if level <lv:
#         draw_tree(l,level+1)
#     turtle.bk(l)
#     turtle.lt(s)
#     turtle.width(w)
# turtle.speed('fastest')
# draw_tree(l,4)
# turtle.done()


#########################TCP
# import  socket
# import threading
# import time
#客户端
# #创建一个socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接  这里是一个tuple
# s.connect(('www.baidu.com',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com.cn\r\nConnection: close\r\n\r\n')
# buffer=[]
# while True:
#     #调用recv(max)方法，一次最多接收指定的字节数
#     d=s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data=b''.join(buffer)
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)


# ###############################服务器端#########################
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #设置监听端口
# s.bind(('127.0.0.1',9999))
# s.listen(5)
# print('Waiting for connection')
# def tcplink(sock, addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
# while True:
#     #接受一个新连接
#     sock,addr=s.accept()
#     #创建新线程来处理TCP连接
#     t=threading.Thread(targegt=tcplink,args=(sock,addr))
#     t.strat()
#
#
# ##############################客户端###########################
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('127.0.0.1', 9999))
# # 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()
####################UDP
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定端口
# s.bind(('127.0.0.1',9999))
# print('Bind DP on 9999...')
# while True:
#     data,addr=s.recvfrom(1024)
#     print('Received from %s:%s.'%addr)
#     s.sendto(b'Hello,%s'%data,addr)
# #客户端 四个线程池 7个参数 Spring用到的设计模式
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.sendto(data, ('127.0.0.1', 9999))
#     # 接收数据:
#     print(s.recv(1024).decode('utf-8'))
# s.close()
#############################################
#SMTP发送邮件
# from email.mime.text import MIMEText
# msg=MIMEText('hello ,send by Python','plain','utf-8')
# from_addr=input('From:')
# password=input('password:')
# to_addr=input('To:')
# #shuru  SMTP服务器地址
# smtp_server=input('SMTP  server:')
#
# import smtplib
# server=smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()
#################################
#求解阶乘的问
##################
# l=[]
# def jiecheng(n):
#     sum = 0
#     #在此出声明num出现的结果错误应该
#     #原因是因为num在外米娜每一次的值被改变后就保留了不会回到初始值
#     for i in range(1,n+1):
#        num = 1
#        for j in range(1,i+1):
#            num=num*j
#        l.append(num)
#        sum+=num
#     return sum
# print(len(l))
# print(jiecheng(3))
#遗留的问题  append不进去
#递归方法求阶乘

# def jiecheng (n):
#     if n==0:
#         sum=1
#     else:
#         sum=n*jiecheng(n-1)
#     return sum
# print(jiecheng(3))
#到着输出字符串


# def output(a,l):
#     if l==0:
#         return
#     else:
#         print(a[l-1])
#         output(a,l-1)
# a = input("input:")
# l = len(a)
# output(a,l)

# def age(n):
#     c=10
#     if n==1:
#         c=10
#     else:
#         c=2+age(n-1)
#     return c
# print(age(5))
#人口老龄化医疗保健和老年人晚年的生活,
#留守儿童和孤寡老人一直是中国农村的现状.
#输入不多与5位的整数
# n=int(input("qing shu ru:"))
# a= int(n/10000)
# b=int( n%10000/1000)
# c=int( n%1000/100)
# d= int(n%100/10)
# e= int(n%10)
#
# if a != 0:
#     print("是五位数：%d %d %d %d %d"%(e,d,c,b,a))
# elif b != 0:
#     print("是si位数：%d %d %d %d "%(e, d, c, b))
# elif c!=0:
#     print("是san位数：%d %d %d"%(e, d, c))
# elif d!=0:
#     print("是er位数：%d %d"%(e, d))
# else:
#     print("是yi位数：%d"%(e))
# 两个鸡蛋判断出从那娜层可以摔碎
# class Egg(object):
#     def cmp(self,n):
#         for x in range(1,100):
#             f=1-n/(x*x)
#             if(f==0):
#                 key=x
#                 break
#         F = (n / key - 1) + (key - 1)
#         print(F)
# def main():
#     egg=Egg()
#     egg.cmp(100)
# if __name__=="__main__":
#     main()

#判断回文数
#代码分析字符数组中的数是将顺数位置上的俄数和倒数位置上的数进行比较，看其是否相同，
#
# str=str(input("qingshuru"))
# for i in range(len(str)):
#     flag=True
#     print(str[i],str[-i-1])
#     if str[i]!=str[-i-1]:
#         flag=False
#         break
# if flag==True:
#     print('shi hui wen shu')
# if flag==False:
#     print('bushihuiwenshu ')
# Monday6, Tuesday7, Wednesday9, Thursday8, Friday6
# week=str(input("what day is it"))
# if week[0]=='w'or week[0]=='W':
#     print("today is wednesday")
# elif week[0]=='M'or week[0]=='m':
#     print("today is Monday")
# elif week[0]=='F' or week[0]=='f':
#     print("today is Friday")
# elif week[0]=='t' or week[0]=='T':
#     if week[1]=='u'or week[1]=='U':
#        print("today is Tuesday")
#     else:
#         print("today is Thurday")

#到着输出列表的值
# list=[]
# for i in range (0,5):
#    week=str(input("what day is it"))
#    list.append(week)
# for i in range (len(list)):
#    print(list[-i-1])
###########################
#将字体颜色进行变色
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING= '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print (bcolors.HEADER + "警告的颜"+ bcolors.WARNING+"色字体?" )
#######################
#100内的素数
# num=int(input("data:"))
# list=[]
# for x in range(1,101):
#   flag=True
#   for i in range(2,int(x/2)+1):
#      if x%i == 0:
#         flag=False
#         break
#   if flag==True:
#     list.append(x)
# print(list)
#############################
#对数列进行排序37
# a=[]
# for i in range(10):
#   num=int(input("num:"))
#   a.append(num)
# for
#二维列表
# 外层循环是行数，内层循环是列数
# map = []
# for i in range(0, 10):
#   map += [[]]
#   for j in range(0, 20):
#     map[i] += ['*']
# print(map)
# 实现一个3*3矩阵主对角线元素之和
# a=[]
# sum=0
# for i in range(3):
#     a.append([])#存储的是地下for循环的数据
#     for j in range(3):
#         a[i].append(float(input("input num:")))
# for i in range(3):
#     for j in range(3):
#      sum+=a[i][j]
# print("主对角线和为：",sum)
#数组中数据的插入
#
# a=[1,2,3,4,6]
# b=int(input("num:"))
# a.append(b)
# a.sort()
# print(a)
#法2
# a=[1,2,3,4,6,0]
# print("yuan shi lie biao:",a)
# b=int(input("num:"))
# end=a[len(a)-2]
# if end<b:
#     a[len(a)-1]=b
# else:
#     # len(a)-1比教的是前面的元素而最后的一个元素表示占位,
#     #而rangge 中能访问到的数据到len(a)-1,因为有一个占位符所以在减1从而访问到倒数第二个元素
#  for i in range(len(a)-1):
#      if b<a[i]:
#          c=a[i]
#          a[i]=b
#          for j in range(i+1,(len(a))):
#              temp=a[j]
#              a[j]=c
#              c=temp
#          break
# print(a)
#############################3
#将一个数组逆序输出:
# list=[1,2,3,5,6]
# for i in range(len(list)):
#     print(list[-i-1])
##########################
# 模仿静态变量:在计算机程序执行之前就为之分配的变量,
# 局部变两只是只是在运行时暂时存在
# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
# a=[]
# b=[]
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[j].append(float((input("num:"))))
# print(a)
# for i in range(3):
#     b.append([])
#     for j in range(3):
#         b[j].append(float((input("num:"))))
# print(b)
# """
# Definition of TreeNode:
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None
# """
# class Solution:
#     """
#     @param: root: A Tree
#     @return: Postorder in ArrayList which contains node values.
#     """
#     a = []
#     def postorderTraversal(self, root):
#         # write your code here
#         self.left(root)
#         return self.a
#     def left(self,root):
#         if root == None:
#             return
#         self.left(root.left)
#         self.right(root.right)
#         self.a.append(root.val)
#     def right(self,root):
#         if root == None:
#             return
#         self.left(root.left)
#         self.right(root.right)
#         self.a.append(root.val)
# x=[[1,2,3],[4,5,6],[7,8,9]]
# y=[[7,8,9],[4,5,6],[1,2,3]]
# result=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(x)):#输出他的行len，输出他的列len
#     for j in range(len(x[0])):
#         result[i][j]=x[i][j]+y[i][j]
# #在result中print r 这个厉害了 因为r 在result中，直接输出就可以了
# for r in result:
#     print(r)
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)
# 求输入数字的平方，如果平方运算后小于 50 则退出。
# while True:
#     a=int(input("input num:"))
#     if a*a<50:
#         print("有数小于50")
#         break
#     else:
#         b=a*a
#         print("a的平方根是:",b)
################
# TRUR=1
# FALSE=0
# def q(x):
#    return x*x
# again=1
# while  again:
#     num = int(input("qing shu ru shu zi"))
#     print("the result is:", q(num))
#     # if q(num)<50:
#     #     print("平方小于50程序结束")
#     #     break
#     # print("the result is:",q(num))
#     if q(num)<50:
#         again=FALSE
#         print("平方小于50程序结束")
#     else:
#         again=TRUR
##########################
# import tensorflow as tf
# a=3
# b=6
# str="a*b"
# print(str)
# m1=tf.constant([3,5])
# m2=tf.constant([2,4])
# result=tf.add(m1,m2)
# print(result)
# print(m1)
# sess=tf.Session()
# print(sess.run(result))
# sess.close()


#使用with代码无需显示的调用close释放资源，而是自动地关闭会话
# with tf.Session as sess:
#     res=sess.run([result])
# print(res)
#Tensorflow中使用with…device语句来指定GPU或CPU资源执行操作。
# op在此处指的时常量  一般我们无需显示制定的计算资源tensorflow可以自动识别，如果检测到我们的GPU环境，会有限利用
# GPU环境执行我们的程序，但是当我们的计算机中多于一个可用的GPU这就需要手动指派GPU去执行特定的常量
# with...device 用来制定资源执行的操作
"""Contains a variant of the LeNet model definition."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

slim = tf.contrib.slim


def lenet(images, num_classes=10, is_training=False,
          dropout_keep_prob=0.5,
          prediction_fn=slim.softmax,
          scope='LeNet'):
  """Creates a variant of the LeNet model.
  Note that since the output is a set of 'logits', the values fall in the
  interval of (-infinity, infinity). Consequently, to convert the outputs to a
  probability distribution over the characters, one will need to convert them
  using the softmax function:
        logits = lenet.lenet(images, is_training=False)
        probabilities = tf.nn.softmax(logits)
        predictions = tf.argmax(logits, 1)
  Args:
    images: A batch of `Tensors` of size [batch_size, height, width, channels].
    num_classes: the number of classes in the dataset. If 0 or None, the logits
      layer is omitted and the input features to the logits layer are returned
      instead.
    is_training: specifies whether or not we're currently training the model.
      This variable will determine the behaviour of the dropout layer.
    dropout_keep_prob: the percentage of activation values that are retained.
    prediction_fn: a function to get predictions out of logits.
    scope: Optional variable_scope.
  Returns:
     net: a 2D Tensor with the logits (pre-softmax activations) if num_classes
      is a non-zero integer, or the inon-dropped-out nput to the logits layer
      if num_classes is 0 or None.
    end_points: a dictionary from components of the network to the corresponding
      activation.
  """
  end_points = {}

  with tf.variable_scope(scope, 'LeNet', [images]):
    net = end_points['conv1'] = slim.conv2d(images, 32, [5, 5], scope='conv1')
    net = end_points['pool1'] = slim.max_pool2d(net, [2, 2], 2, scope='pool1')
    net = end_points['conv2'] = slim.conv2d(net, 64, [5, 5], scope='conv2')
    net = end_points['pool2'] = slim.max_pool2d(net, [2, 2], 2, scope='pool2')
    net = slim.flatten(net)
    end_points['Flatten'] = net

    net = end_points['fc3'] = slim.fully_connected(net, 1024, scope='fc3')
    if not num_classes:
      return net, end_points
    net = end_points['dropout3'] = slim.dropout(
        net, dropout_keep_prob, is_training=is_training, scope='dropout3')
    logits = end_points['Logits'] = slim.fully_connected(
        net, num_classes, activation_fn=None, scope='fc4')

  end_points['Predictions'] = prediction_fn(logits, scope='Predictions')

  return logits, end_points
lenet.default_image_size = 28


def lenet_arg_scope(weight_decay=0.0):
  """Defines the default lenet argument scope.
  Args:
    weight_decay: The weight decay to use for regularizing the model.
  Returns:
    An `arg_scope` to use for the inception v3 model.
  """
  with slim.arg_scope(
      [slim.conv2d, slim.fully_connected],
      weights_regularizer=slim.l2_regularizer(weight_decay),
      weights_initializer=tf.truncated_normal_initializer(stddev=0.1),
      activation_fn=tf.nn.relu) as sc:
    return sc





































