## Matplotlib的使用

>Matplotlib 是一个 [Python](https://baike.baidu.com/item/Python) 的 2D绘图库。通过 Matplotlib，开发者可以仅需要几行代码，便可以生成绘图，直方图，功率谱，条形图，错误图，散点图等。

### Matplotlib的安装

`pip install matplotlib`

### Matplotlib的基本使用

```Python
import numpy as np 
from matplotlib import pyplot as plt 
 
x = np.arange(1,11) 
y =  2  * x +  5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y)
plt.show()
```

以上代码中，我们方法说明:

- plt.title() 设置图表的名称
- plt.xlabel() 设置x轴名称
- plt.ylabel() 设置y轴名称
- plt.plot()  绘制线性图表
- plt.show() 显示图表

### 图表中文显示

Matplotlib 默认情况不支持中文，我们可以使用以下简单的方法来解决：

首先下载字体（注意系统）：<https://www.fontpalace.com/font-details/SimHei/>

#### 方法1：引入字体文件

```python
zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")
plt.title("图表 - 测试",fontproperties=zhfont1)
```

#### 方法2：使用系统文字

```python
# 查看系统支持的字体
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
for i in a:
    print(i)
```

在上面的代码中找到可以使用的字体，使用

```python
plt.rcParams['font.family']=['SimHei']
```



### 线性图表

- plt.plot(x,y,type)

  - x 显示的数据

  - y y轴的值

  - type 值显示的方式  具体值如下

    | 字符       | 描述         |
    | ---------- | ------------ |
    | `'-'`      | 实线样式     |
    | `'--'`     | 短横线样式   |
    | `'-.'`     | 点划线样式   |
    | `':'`      | 虚线样式     |
    | `'.'`      | 点标记       |
    | `','`      | 像素标记     |
    | `'o'`      | 圆标记       |
    | `'v'`      | 倒三角标记   |
    | `'^'`      | 正三角标记   |
    | `'&lt;'`   | 左三角标记   |
    | `'&gt;'`   | 右三角标记   |
    | `'1'`      | 下箭头标记   |
    | `'2'`      | 上箭头标记   |
    | `'3'`      | 左箭头标记   |
    | `'4'`      | 右箭头标记   |
    | `'s'`      | 正方形标记   |
    | `'p'`      | 五边形标记   |
    | `'*'`      | 星形标记     |
    | `'h'`      | 六边形标记 1 |
    | `'H'`      | 六边形标记 2 |
    | `'+'`      | 加号标记     |
    | `'x'`      | X 标记       |
    | `'D'`      | 菱形标记     |
    | `'d'`      | 窄菱形标记   |
    | `'&#124;'` | 竖直线标记   |
    | `'_'`      | 水平线标记   |

    颜色如下：

    | 字符  | 颜色   |
    | ----- | ------ |
    | `'b'` | 蓝色   |
    | `'g'` | 绿色   |
    | `'r'` | 红色   |
    | `'c'` | 青色   |
    | `'m'` | 品红色 |
    | `'y'` | 黄色   |
    | `'k'` | 黑色   |
    | `'w'` | 白色   |

    ```
    plt.plot(x, y,'*m')
    ```

### 绘画条状图

 bar(x,y,color) 函数来生成条形图

- x 条装显示位置
- y 显示的值
- color 显示的颜色

```python
from matplotlib import pyplot as plt 
x =  [5,8,10] 
y =  [12,16,6] 
x2 =  [6,9,11] 
y2 =  [6,15,7] 
plt.bar(x, y, align =  'center') 
plt.bar(x2, y2, color =  'g', align =  'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis') 
plt.show()
```







### 绘画子图

subplot() 函数允许你在同一图中绘制不同的东西

``` python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(7, 7))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()
```