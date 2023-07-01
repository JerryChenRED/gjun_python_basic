# from matplotlib import pyplot as plt

# # 1
# list_y = [2, 4, 6, 8]
# plt.plot(list_y)
# # plt.show()
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.legend(["First Line"])
# plt.title("First Plot")
# plt.savefig("./plot_image/first_plot.jpg")

# plt.cla()

# # 2
# list_x_y = [(1,2), (2,4), (9,6), (7,10)]
# list_x_y.sort()
# print(list_x_y)
# plt.plot([x for x, y in list_x_y], [y for x, y in list_x_y], marker='^')
# #plt.show()
# plt.savefig("./plot_image/second_plot.jpg")
# plt.cla()

# # 3 
# n = range(1,30)
# plt.plot(n, n, marker='o', linestyle='--', color='y')   #Yellow Dash 
# plt.plot(n, [i*i for i in n], "rs") #Red Square
# plt.plot(n, [i**3 for i in n], "g^") #Green Triangle
# # plt.plot(n, n, "y--", n, n**2, "rs", n, n**3, "g^")
# plt.legend(["n", "n*n", "n*n*n"])
# plt.savefig("./plot_image/third_plot.jpg")

# # 4
# n = range(1,30)
# plt.scatter(n, n, c ='y') #Yellow Dash 
# plt.scatter(n, [i*i for i in n], c="r")
# plt.scatter(n, [i**3 for i in n], c='g')
# plt.legend(["n", "n*n", "n*n*n"])
# plt.savefig("./plot_image/forth_plot.jpg")
# plt.cla()

# import matplotlib.pyplot as plt
# import numpy as np

# # 設定圖形大小和解析度
# fig, ax = plt.subplots(figsize=(6, 6), dpi=80)

# # 設定x的範圍和數量
# x = np.linspace(-2, 2, 1000)

# # 定義愛心曲線的方程式
# y1 = np.sqrt(1 - np.power(np.abs(x) - 1, 2))
# y2 = -3 * np.sqrt(1 - np.power(np.abs(x) / 2, 0.5))

# # 繪製愛心曲線
# ax.plot(x, y1, color='pink', linewidth=2)
# ax.plot(x, y2, color='pink', linewidth=2)

# # 設定座標軸範圍
# ax.set_xlim(-2.5, 2.5)
# ax.set_ylim(-2.5, 2.5)

# # 隱藏座標軸
# ax.axis('off')

# # 顯示愛心圖形
# plt.show()


# # 5
# import numpy as np
# x = np.random.randint(1, 100, 20)
# y = np.linspace(1, 100, 20)
# plt.scatter(sorted(x), y, c='y')
# plt.savefig("./plot_image/fifth_random_scatter.jpg")

# # 6
# x = np.random.randint(1, 100, 10000)
# plt.hist(x, bins=80)
# plt.savefig("./plot_image/sixth_histogram.jpg")
# plt.cla()

# # 7
# x = [1, 2, 3, 4]
# plt.pie(x, explode=[0, 0, 0.1, 0.1], labels=['1', '2', '3', '4'])
# plt.savefig("./plot_image/seventh_pie.jpg")
# plt.cla()

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)  # 參數t的範圍（0到2π）
x = 2 * np.cos(t)                # x坐標
y = 3 * np.sin(t)                # y坐標

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cartesian Curve')
plt.axis('equal')  # 設定x和y軸的比例相等，以確保圖形呈現正確的形狀
plt.grid(True)
plt.show()
