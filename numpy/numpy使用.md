# numpy基本使用

## 1. 安装方法

`pip install numpy`

## 2. 常用操作

### 2.1 数据的初始化

##### numpy.genfromtxt(filename,delimiter,dtype) 通过文件传入数据

- filename：文件名
- delimiter: 文件里每例数据是怎么分割开的
- dtype: 传入的数据是什么类型（一般为str）

```python
import numpy
numpy.genfromtxt('abc.txt',delimiter=',',dtype=str)
```

##### numpy.array(params) 直接传入数据 

此处的params是数据，就是给numpy传递我们要处理的数据，可以是int、float、set、list、dict、obj甚至可以list套list，但是注意，这的list，要求的数据类型统一，说的直白点不是list,而是数组

```Python
data = numpy.array([1,2,3,4,5])
data = numpy.array(['1','2','3','4','5'])
data = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
```

##### numpy.arange(num) 直接生成数据

- num 生成多少个数据

```python
numpy.arange(10)
# 和python里的range一样
[0,1,2,3,4,5,6,7,8,9]
```

##### numpy.zeros((x,y),dtype) 初始化一个空的矩阵

- x 行
- y 列 可省略，若省略 格式为numpy.zeros(x) 生成一个一维矩阵
- dtype 可选项 ，选择生成数据的类型 `dtype = numpy.int32`

```python
numpy.zeros((3,4))
'''
[
[0.,0.,0.],
]
'''
```

> 注意：
>
> 1. 生成的数据类型 默认是：float类型
> 2. 生成多维矩阵，要加括号

##### numpy.ones((x,y),dtype) 初始化一个都是1的矩阵 

> 具体操作和zeros一样

##### numpy.random.random((x,y)) 初始化一个 随意数据 为 x行，y列的数据

生成的数据都是在-1 和 1之间的数据

##### numpy.linspace(start,end,count) 初始化一个指定范围的数据的值 ，且里面的数据平均增长

```python
import numpy
# 生成10个 0 到 3*PI 之间的数
data = numpy.linspace(0,3*numpy.pi,10)
```



### 2.2 数据的操作

#####  数据类型的使用

> 如何查看数据类型呢？数据类型是否可以转换

```python
data = numpy.array([1,2,3,4,5])
# 查看 data 变量是什么类型，一般为ndarray
print(type(data))
# 查看 data 里面数据什么类型
print(data.dtype) #int64
# 上面的是整型，如何我们想让他变成float
data.astype('float')
```



##### 如何取出里面的数据呢？

这个方法会有一个返回值。数据类型为ndarray，我们可以拿一个参数接收。

```python
data = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
‘’‘
1 2 3
4 5 6
7 8 9
’‘’
# 获取里面
# 所有数据
print(data)
# 获取 指定 数据，我们可以通过索引的方式
# 获取 单个 数据，比如：要获取5,也就是第3组第3个数据，我们用逗号隔开
print(data[1,1])
# 获取某行数据，比如：要获取[4,5,6], 此处和我们的切片方法是一样的
print(data[1:2])
# 获取某列列数据，比如：要获取3，6，9
# 格式：data[行切片:第几列的索引] 单列
# 	data[行的切片,列的切片] 单列或多列
print(:,:3)
```

​	获取里面所有数据：直接输入变量

##### 数据的查找

```Python
data = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# 以下操作，会把5拿到这个矩阵中，依次比较，返回Boolean值，而我们可以不在用for遍历
'''
[[F F F],
 [F T F],
 [F F F]]
'''
print(data == 5)
# 以下操作，会把是True所对应的值取出, 如下面，会出输[[1，2，3]，[7，8，9]]
print(data[[True,False,True]])
# 查看指定行有没有想要的数据, 比如：查看第三行没有7
print(data[2:3] == 7)
# 查看指定列有没有想的的数据，比如：查看第一列没有7
print(data[:,0] == 7)

```

##### 数据的常用逻辑

> 常用的逻辑运算符号 & 和 |
>
> & 表示并且
>
> | 表示或者

```Python
data=numpy.array([1,2,3,4,5])
# 表示是否有等于1又等于3的
print((data == 1) & (data == 3)
# 表示是否有等于1或者等于3的
print((data==1)|(data==3))
```

#####数据的聚合使用

> 常用的聚合有 max() 、min() 与 sum()
>
> 如果是矩阵，我们可以通过`axis`属性选择维度为一个整体筛选 1代表：横向 0代表：纵向

```Python
 	data = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# 查找数据里的总和
print(data.sum())
# 查找数据里的最大值
print(data.max())
# 查找数据里的最小值
print(data.min())
# 查找每一行数据里最小值
print(data.min(axis=1))
# 查找每一列数据里最小值
print(data.min(axis=0))
```

##### 数据的简单运算

```python
import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
# 使用矩阵之间相运算
print(a-b)
'''
10，19，27，37
'''
# 使用矩阵与单一数据运算
print(a-1)
'''
9，19，29，39
'''
# 自增n方**2
print(b**2)
'''
0，1，4，9
'''
# 比较运算
print(a<30)
'''
F,F,F,T
'''
# 矩阵乘法
print(a.dot(b))
print(np.dot(a,b))
'''
200
'''
a = np.array([[1,2],[3,4]])
b = np.array([[4,3],[2,1]])
'''
8 5
20 13
'''
```



> 注意：
>
> 1. 使用 矩阵 之 矩阵 相运算，是对应位置运算
> 2. 使用 矩阵 与 单一  数据运算，是逐一运算
> 3. 使用比较运算符，返回Boolean值



> 提示：
>
> 矩阵乘法就是 左边第i行,j列数 乘以 右边 i列的 ，使用左边i先一个数据

### 2.3 数据结构的操作

##### data.reshape(num1,num2) 修改数据结构

- num1 :修改为几行
- num2 :修改为几列，值为-1表示让其自动计算

> 注意： num1 *num2 一定要和原来数据的总个数是一致，不然报错

```python
import numpy
# 生成一个一维数组 0-9
data = numpy.arange(10)
# 转成一个二维矩阵
data = data.reshape(2,5)
```

#####data.shape 查看整体结构，也可当修改结构

```python
data.shape=(2,5)
```

##### data.ravel() 向矩阵转成1维的，也就是向量

##### data.ndim 查看数据维度

##### data.size 查看数据的大小

##### data.T 行转列

###2.4 Numpy的数学计算

| 矩阵函数     | 说明                                 |
| ------------ | ------------------------------------ |
| np.exp(a)    | 对矩阵a中每个元素取指数函数,多少次幂 |
| np.sqrt(a)   | 对矩阵a中每个元素开根号√x            |
| np.sin(a)    | 对矩阵a中每个元素取正弦,sin(x)       |
| np.cos(a)    | 对矩阵a中每个元素取余弦,cos(x)       |
| np.tan(a)    | 对矩阵a中每个元素取正切,tan(x)       |
| np.arcsin(a) | 对矩阵a中每个元素取反正弦,arcsin(x)  |
| np.arccos(a) | 对矩阵a中每个元素取反余弦,arccos(x)  |
| np.arctan(a) | 对矩阵a中每个元素取反正切,arctan(x)  |

举例：

```python
import numpy
data = numpy.arange(3)
print(data)
#[0，1，2]
print(numpy.exp(data))
#[1.        , 2.71828183, 7.3890561 ]
print(numpy.sqrt(data))
#[0.        , 1.        , 1.41421356]
print(numpy.sin(data))
#[0.        , 0.84147098, 0.90929743] 
print(num.arctan(data))
#[0.        , 0.78539816, 1.10714872]
```

### 2.5 Numpy 其他的拼接

| 矩阵函数                   | 含义                                                         |
| -------------------------- | ------------------------------------------------------------ |
| np.floor(a)                | 对矩阵a向下取整                                              |
| np.hstack((a,b))           | 将矩阵a与b横向拼接,合并数组                                  |
| np.vstack((a,b))           | 将矩阵a与b纵向拼接,增加数组                                  |
| np.hsplit(a,num)           | 将矩阵a横向切割成num份,平均分配（注意：如果不能平均分，报错） |
| np.hsplit(a,(num,num....)) | 将矩阵a横向切割,根据后成元组的数字决定切割位置               |
| np.vsplit(a,num)           | 将矩阵a纵向切割成num份，平均分配                             |
| np.title(a,(num1,num2))    | 将矩阵a整体扩展复制num1行，一行num2个的数据                  |

举例：

```python
import numpy as np
a = np.floor(10*np.random.random((2,2)))
'''
[[1,2],
 [3,4]]
'''
b = np.floor(10*np.random.random((2,2)))
'''
[[5,6],
[7,8]]
'''
print(np.hstack((a,b)))
'''
[[1,2,5,6],
[3,4,7,8]
]
'''
print(np.vstack((a,b)))
'''
[[1，2]，
[3，4]，
[5，6]，
[7,8]
]
'''
c = np.hstack((a,b))
'''
[[1,2,5,6],
[3,4,7,8]
'''
np.hsplit(c,2)
'''
[array([[1, 2],
        [3, 4]]), array([[5, 6],
        [7, 8]])]
'''
np.hsplit(c,(1,2))
'''
[array([[1],
        [3]]), array([[2],
        [4]]), array([[5, 6],
        [7, 8]])]
'''
np.vsplit(c.T,2)
'''
[array([[1, 3],
        [2, 4]]), array([[5, 7],
        [6, 8]])]
'''
a= np.arange(0,6)
a.shape=2,3
'''
[[0, 1, 2],
[3, 4, 5]]
'''
np.tile(a,(2,3))
'''
[[0, 1, 2, 0, 1, 2, 0, 1, 2],
 [3, 4, 5, 3, 4, 5, 3, 4, 5],
 [0, 1, 2, 0, 1, 2, 0, 1, 2],
 [3, 4, 5, 3, 4, 5, 3, 4, 5]]
'''
```

### 2.6 数据的复制

##### 方法1：直接赋值 = 

```python
import numpy as np
a = np.arange(10)
b = a
print( b is a ) # True
b.shape = (2,5)
print(a.shape) #(2,5)
print(id(a) ==id(b)) # True
```

> 结论：实际是同一块区域有2个不同变量名

##### 方法2： 通过方法view()

```python
import numpy as np
a = np.arange(10)
b = a.view()
print( b is a ) # False
b.shape = 2,5
print(a.shape) #(10,)
print(id(a) ==id(b)) # False
b[1,1] =666
print(a) # [ 0,  1,  2,  3,  4,  5, 66,  7,  8,  9]
```

> 结论：变量不是同一个空间，但是共享同一套值

##### 方法3：通过方法copy()

```python
import numpy as np
a = np.arange(10)
b = a.copy()
print( b is a ) # False
b[6] =666
print(a) # [ 0,  1,  2,  3,  4,  5, 6,  7,  8,  9]
```

> 结论：变量完全是两个东西

### 2.7 综合使用

##### 查找每列最大值

```python
import numpy as np
a = np.sin(np.arange(20)).reshape(5,4)
print(data)
'''
	  [[ 0.        ,  0.84147098,  0.90929743,  0.14112001],
       [-0.7568025 , -0.95892427, -0.2794155 ,  0.6569866 ],
       [ 0.98935825,  0.41211849, -0.54402111, -0.99999021],
       [-0.53657292,  0.42016704,  0.99060736,  0.65028784],
       [-0.28790332, -0.96139749, -0.75098725,  0.14987721]]
'''
# 获取每一列最大的值的索引
index = a.argmax(axis=0)
’‘’
[2，0，3，1]
‘’‘
# 根据索引查找最大的值
data_max = a[index,range(data.shape[1])]

```

#####给数据排序

```python
import numpy as np
a= np.array([[6,4,5],[7,5,3]])
'''
[[6，4，5]
 [7，5，3]]
'''
# 按行排序
b = np.sort(a,axis=1)
'''
[[4，5，6]，
 [3，5，7]]
'''
a=np.array([3,5,6,2,3])
# 将数据的索引排序，返回的是索引
c = np.argsort(a) # [3, 0, 4, 1, 2]
print(a[c]) #[2, 3, 3, 5, 6]
```

