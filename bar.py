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
ax.set_xlabel("COUNT", fontsize=10, fontweight="bold", color="black", labelpad=10)
ax.set_ylabel("LABEL", fontsize=10, fontweight="bold", color="black", rotation=0, labelpad=40)

ax.yaxis.set_tick_params(labelsize=12)
ax.set_yticks(ax.get_yticks())
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='right')

legend_labels = ["No", "Yes"]
legend_colors = ["red", "blue"]
legend_handles = [plt.Line2D([0], [0], color=color, lw=8) for color in legend_colors]
ax.legend(legend_handles, legend_labels, title="LEGEND", loc="lower right", fontsize=8, title_fontsize=10)

ax.grid(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

padding = 0.2
for i, (index, row) in enumerate(bar_data.iterrows()):
    no_count = row["No"]
    yes_count = row["Yes"]
    if no_count > 0:
        ax.text(no_count - padding, i, int(no_count), va='center', ha='right', fontsize=10, color="white", fontweight="bold")
    if yes_count > 0:
        ax.text(no_count + yes_count - padding, i, int(yes_count), va='center', ha='right', fontsize=10, color="white", fontweight="bold")

plt.subplots_adjust(left=0.2)

plt.tight_layout()
plt.show()
