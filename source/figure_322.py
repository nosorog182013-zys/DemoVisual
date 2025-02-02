import seaborn as sns
import matplotlib.pyplot as plt
# Применяем тему картинок по умолчанию.
sns.set_theme()
# Загружаем набор данных.
tips = sns.load_dataset("tips")
# Создаем визуализацию
sns.relplot(
   data=tips,
   x="total_bill", y="tip", col="time",
   hue="smoker", style="smoker", size="size",
)
plt.show()
