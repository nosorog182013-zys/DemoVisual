import seaborn as sns
import matplotlib.pyplot as plt
# применяем тему картинок по умолчанию
sns.set_theme()
# загружаем набор данных
tips = sns.load_dataset("tips")
# создаем визуализацию
sns.relplot(
   data=tips,
   x="total_bill", y="tip", col="time",
   hue="smoker", style="smoker", size="size",
)
plt.show()
