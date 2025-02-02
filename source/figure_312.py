import matplotlib.pyplot as plt
# Пустая фигура без координат.
fig = plt.figure()
plt.show()
# Фигура с координатами.
fig, ax = plt.subplots()
plt.show()
# Фигура с сеткой координат 2х2.
fig, axs = plt.subplots(2, 2)
plt.show()
# Фигура с одной координатой слева и двумя координатами справа.
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                              ['left', 'right_bottom']])
plt.show()

