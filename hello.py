# print('hello world')

# a,b,c=1,2.2,"nihao"
# print(type(a),type(b),type(c))

# import math

# print ("math.modf(100.12) : ", math.modf(100.12))


# print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")


# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句
# for letter in 'Runoob': 
#    if letter == 'o':
#       pass
#       print ('执行 pass 块')
#    print ('当前字母 :', letter)
# print ("Good bye!")


# # 普通参数也叫位置参数，因为这种参数跟参数位置有关
# # 不定长参数
# # arg1为普通参数，*vartuple为可变长元组参数，**vardict为可变长字典参数
# def printinfo( arg1, *vartuple, **vardict ):
#    "打印任何传入的参数"
#    print ("普通参数："+f'{arg1}')#f-string
#    if vartuple:
#         print ("元组参数:"+f'{vartuple}')
#         for var in vartuple:
#             print (var,end=" ")
#         print ("")

#    if vardict:
#         print ("字典参数"+f'{vardict}')
#         for var in vardict:
#             print(var+":"+str(vardict[var]))
#    return
# # 调用printinfo 函数
# printinfo( 10 )
# printinfo( 70, 60, 50 , name='lizhanxu',age=18)


# # 如果单独出现星号 * 后的参数必须用关键字传入
# # 形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参
# def f(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)

# # 元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的
# t = 12345, 54321, 'hello!'
# print(t)


# 注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典

# a=True
# print(a)

# # zip使用      使用zip()可以进行并行迭代
# m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
# print('m:  ',m)
# n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
# print('list(zip(m,n)):  ',list(zip(m,n)))
# print("*zip(m, n):  ", *zip(m, n))###################################    *zip(m, n)得到的是什么对象？
# print("list(zip(*zip(m, n))):  ", list(zip(*zip(m, n))))
# a1,a2=zip(*zip(m, n))
# print("a1:  ",list(a1))
# print("a2:  ",list(a2))


# # python遍历技巧
# # 遍历字典
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)
# # 遍历序列
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)
# # 并行遍历序列，使用zip()
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))
