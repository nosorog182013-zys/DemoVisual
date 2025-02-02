import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
(
sns.barplot(
   data=tips, x="day", y="tip",
   estimator="mean", errorbar=None,
       )
    .set(title="Daily Tips ($)")
)
plt.show()
