from matplotlib import pyplot as plt
from random import randint


def test1():
    x = range(2, 26, 2)
    y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
    plt.rcParams['font.family'] = ['SimHei']
    plt.figure('a', figsize=(8, 8), dpi=160)
    plt.xlabel('时间')
    plt.ylabel('温度')
    plt.title('当天温度变化图')
    plt.xticks(range(0, 25))
    plt.yticks(range(min(y), max(y) + 1))
    plt.plot(x, y, 'r')
    plt.show()
    plt.savefig('./a.png')


def test2():
    x = range(0, 120)
    y = [randint(20, 35) for i in range(120)]
    _xticks = ['10点{}分'.format(i) for i in range(60)]
    _xticks += ['11点{}分'.format(i) for i in range(60)]
    plt.rcParams['font.family'] = ['SimHei']
    plt.xlabel('时间')
    plt.ylabel('温度')
    plt.title('当天温度变化图')
    plt.xticks(x[::5], _xticks[::5], rotation=70)
    plt.yticks(range(min(y), max(y) + 1))
    plt.plot(x[::5], y[::5], )
    plt.show()


def test3():
    info1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
    info2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    x = range(11, 31)
    plt.figure('走势图', figsize=(8, 8), dpi=80)
    plt.rcParams['font.family'] = ['SimHei']
    plt.ylabel('人数(位)')
    plt.xlabel('年龄')
    plt.xticks(x, ['{}岁'.format(i) for i in x], rotation=270)
    plt.title('交往人数走势图')
    plt.plot(x, info1, label='同桌')
    plt.plot(x, info2, label='自己')
    plt.legend(loc=3)
    plt.show()


def test4():
    a = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
         22, 23]
    b = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
         12, 13, 16]
    x = range(0, 31)
    x2 = range(40, 71)
    plt.scatter(x, a)

    plt.scatter(x2, b)
    # plt.plot(x,a,'o')
    # plt.plot(x2,b,'o')
    plt.show()


def test5():
    names = ['战狼2', '红海行动', '美人鱼', '唐人街探案2', '流浪地球', '我不是药神', '速度与激情8', '西虹市首富', '速度与激情7', '捉妖记', '复仇者联盟3：无限战争', '捉妖记2',
             '羞羞的铁拳', '海王', '变形金刚4：绝迹重生', '前任3：再见前任', '毒液：致命守护者', '疯狂的外星人', '功夫瑜伽', '侏罗纪世界2']
    nums = [56.39, 36.22, 33.9, 33.71, 31.8, 30.75, 26.49, 25.27, 24.26, 24.21, 23.7, 22.19, 21.9, 19.97, 19.79, 19.26,
            18.56, 17.96, 17.53, 16.82]
    plt.rcParams['font.family'] = ['SimHei']
    plt.figure(figsize=(15, 8), dpi=90)
    plt.barh(range(len(names)), nums)
    plt.yticks(range(len(names)), names)
    for a, b in zip(range(len(names)), nums):
        plt.text(b + 1, a, b)
    plt.show()


def test6():
    b_16 = [15746, 312, 4497, 319]
    b_15 = [12357, 156, 2045, 168]
    b_14 = [2358, 399, 2358, 362]
    a = ['终极之战', '郭刻尔克', '蜘蛛侠:英雄归来', '战狼2']

    plt.figure(figsize=(15, 8), dpi=80)
    bar_width = 0.3

    # p1 =[i for i in range(len(a))]
    # p2 =[i+bar_width*2 for i in range(len(a))]
    # p3 =[i+bar_width*3 for i in range(len(a))]

    p1 = list(range(len(a)))
    p2 = [i + bar_width for i in p1]
    p3 = [i + bar_width * 2 for i in p1]

    plt.rcParams['font.family'] = ['SimHei']
    plt.bar(p1, b_14, width=bar_width, label='第一天')
    plt.bar(p2, b_15, width=bar_width, label='第二天')
    plt.bar(p3, b_16, width=bar_width, label='第三天')
    plt.xticks(p2, a)
    plt.legend(loc=2)
    plt.show()


def test7():
    a = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130,
         124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 136, 126, 134, 95, 138, 117, 111, 78, 132, 124, 113, 150, 110,
         117, 86, 95, 144, 105, 126, 130, 126, 130, 126, 116, 123, 106, 112, 138, 123, 86, 101, 99, 136, 123, 117, 119,
         105, 137, 123, 128, 125, 104, 109, 134, 125, 127, 105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120,
         114, 105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134, 156, 106, 117, 127, 144, 139, 139, 119,
         140, 83, 110, 102, 123, 107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133, 112, 114, 122, 109,
         106, 123, 116, 131, 127, 115, 118, 112, 135, 115, 146, 137, 116, 103, 144, 83, 123, 111, 110, 111, 100, 154,
         136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141, 120, 117, 106, 149, 122, 122, 110, 118, 127,
         121, 114, 125, 126, 114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137, 92, 121, 112, 146, 97, 137,
         105, 98, 117, 112, 81, 97, 139, 113, 134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110, 105, 129,
         137, 112, 120, 113, 133, 112, 83, 94, 146, 133, 101, 131, 116, 111, 84, 137, 115, 122, 106, 144, 109, 123, 116,
         111, 111, 133, 150]
    b = 2
    bins = (max(a) - min(a)) // b
    plt.figure(figsize=(16, 8), dpi=80)
    plt.hist(a, bins=bins, normed=True)
    plt.xticks(range(min(a), max(a) + b, b))
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # test3()
    # test5()
    test7()
