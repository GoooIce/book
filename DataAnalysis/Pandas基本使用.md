# Pandas基本使用

## 1. 安装方法

`pip install pandas`

## 2. 常用操作

### 2.1 数据的初始化

Pandas数据的初始化分为以下几种

- 通过Object初始化
- 通过文件初始化
- 通过SQL查询结果初始化
- 通过NoSQL数据库查询结果初始化

##### 通过object初始化

```python
import pandas as pd
# columns参数是通过一个list参数来指定column labels
df = pd.DataFrame([['a1', 1], ['a2', 4]], columns=['uid', 'score'])
# 通过字典初始化，key 做列名，值可以通过list数据初始化
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': ['a', 'b', 'c', 'd']})
# 通过字典初始化，key 做列名，值可以通过numpy的数据初始化
df = pd.DataFrame({'col1': np.arange(3), 'col2': np.arange(5, 8)})
# 可以不等长，缺失值自动设为NaN
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)
# 通过字典初始化，key 做列名，值可以通过Series过初始化
s = pd.Series(range(5))
d = pd.Series(range(8, 13))
df = pd.DataFrame({'a': s, 'b': p})
# 直接通过numpy数据来初始化
df = pd.DataFrame(np.arange(16).reshape((4,4)), columns=['one', 'two', 'three','four'], index=['a', 'b', 'c','d'])
```

DataFrame 

- columns 用来设置 列名，也可以通过columns来决定显示几个字段
- index 没行的序号显示 

##### 通过文件初始化

```python
import pandas as pd
csv_path = "./test.csv"
columns = ['id', 'name', 'age']
dtype = {'id': int, 'name': object, 'age': int}
pd.read_csv(csv_path, header=None, names=columns, dtype=dtype)
```

- path  必须参数，用以指明文件的路，也可以是URL(可以是http,ftp,socket3)

- header 可选参数 这个参数用于设置第几行为column names, 默认是'infer'，即Pandas会自动推断哪一行是column names。当文件中没有column names时，相当于设定header=0。很多时候想要忽略原始的column names而自己设定column names，那么可以将这个参数设置为None, 然后通过names参数来设定column names
- names 可选参数 用于设定column names
- dtype 可选参数 用于设定每一列对应的数据类型，需要注意的是对string类型需要设置为object
- nrows 要读取多少行，通过这个参数我们可以部分读取文件
- usecols 用于选定列，即指定哪些列load进DataFrame中，通过这个参数可以只读取我们需要的数据，从而减少内存占用，加快load速度

##### 通过SQL查询结果初始化

```python
import pandas.io.sql as sql
# conn是数据库的连接对象
sql.read_frame('select * from test', conn)

```

##### 通过NoSQL查询结果初始化

```python
# 从MongoDB中查询年龄大于20岁的用户，查询返回一个cursor对象
user_results = user.find({"age": {"$gt": 20}})

# 将cursor对象转化为list，然后初始化
# columns可以用于选取相应的field的数据，只有在这个列表中的field才会被load进DataFrame对象当中，如果没有对应的数据，会被填入NaN
df = pd.DataFrame(list(user_results), columns=['id', 'age', 'name']
```

这里需要注意的是如果不指定columns参数，有可能导致某些为空的field没有对应的列，如果指定了列名称，则如果相对应的域没有数据的话，就会自动置为NaN

### 2.2 数据类型

> 数据 初始化后默认是`DataFrame`

