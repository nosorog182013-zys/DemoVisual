import matplotlib.pyplot as plt

# пустая фигура без координат
fig = plt.figure()
# фигура с координатами
fig, ax = plt.subplots()
# фигура с сеткой координат 2х2
fig, axs = plt.subplots(2, 2)
# фигура с одной координатой слева и двумя координатами справа
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                              ['left', 'right_bottom']])
plt.show()

