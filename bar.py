import pandas as pd
import matplotlib.pyplot as plt

file_path = "bar_assignment.csv"
data = pd.read_csv(file_path)

data['COUNT'] = data['COUNT'].replace({1: "Yes", 0: "No"})

bar_data = data.groupby('LABEL')['COUNT'].value_counts().unstack(fill_value=0)

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(10, 6))

bar_data.plot(kind="barh", stacked=True, color=["red", "blue"], ax=ax)

ax.set_title("Bar Plot", fontsize=16, loc="left", color="black", fontweight="bold")
ax.set_xlabel("COUNT", fontsize=10, fontweight="bold", color="black")
ax.set_ylabel("LABEL", fontsize=10, fontweight="bold", color="black")
ax.legend(["No", "Yes"], title="LEGEND", loc="upper right", fontsize=10)

for i, (index, row) in enumerate(bar_data.iterrows()):
    no_count = row["No"]
    yes_count = row["Yes"]
    if no_count > 0:
        ax.text(no_count / 2, i, int(no_count), va='center', ha='center', fontsize=10, color="white", fontweight="bold")
    if yes_count > 0:
        ax.text(no_count + yes_count / 2, i, int(yes_count), va='center', ha='center', fontsize=10, color="white", fontweight="bold")

plt.tight_layout()
plt.show()
