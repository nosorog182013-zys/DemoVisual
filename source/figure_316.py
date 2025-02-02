import matplotlib.pyplot as plt
import numpy as np

# Вспомогательная функция
def my_plotter(ax, data1, data2, param_dict):
   out = ax.plot(data1, data2, **param_dict)
   return out
# 4 произвольных набора данных
data1, data2 = np.random.randn(2, 100)

fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')
plt.show()
