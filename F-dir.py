#使用dir()函数查看一个模块，看看它里面有什么变量、函数、类、类方法
#这种方式自学：dir(x)，可以查询到x相关的函数，x可以是模块，也可以是任意一种对象

#举例
import random,csv  # 调用random,csv模块
print('random模块:')
print(dir(random))
# for i in dir(csv):
#     print(i)


a = ''  # 设置一个字符串
print('字符串：')
print(dir(a))    # 把字符串相关的函数展示出来

a = []  # 设置一个列表
print('列表：')
print(dir(a))    # 把列表相关的函数展示出来

a = {}  # 设置一个字典
print('字典：')
print(dir(a))  # 把字典相关的函数展示出来