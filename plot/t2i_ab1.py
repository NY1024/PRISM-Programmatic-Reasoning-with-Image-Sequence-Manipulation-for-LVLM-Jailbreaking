import matplotlib.pyplot as plt
import numpy as np

models = ['Qwen2-VL-7B-Instruct', 'GPT-4o']
t2i_models = ['SD 3', 'SD 1.4', 'Seedream 3.0', 'DALL·E 3']


scores = {
    'Qwen2-VL-7B-Instruct': [0.91, 0.89, 0.91, 0.91],
    'GPT-4o': [0.59, 0.61, 0.65, 0.64]
}


group_distance = 0.8 
x = np.array([0, group_distance])


bar_width = 0.15
font_size = 17
plt.rcParams.update({'font.size': font_size})

fig, ax = plt.subplots(figsize=(9, 5))


offsets = np.array([-1.5, -0.5, 0.5, 1.5]) * bar_width

colors = ['#94b5d7', '#83b5b5', '#bbd5d4', '#d7eaec']

for i, (t2i, color) in enumerate(zip(t2i_models, colors)):
    vals = [scores[model][i] for model in models]
    bars = ax.bar(x + offsets[i], vals, width=bar_width, label=t2i, color=color)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.01, f'{height:.2f}',
                ha='center', va='bottom', fontsize=font_size - 1)

ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(0, 1.05)
ax.set_ylabel('ASR', fontsize=font_size)
ax.legend(title='T2I Model', fontsize=font_size - 1, title_fontsize=font_size)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()




plt.savefig('./t2i_ab1.pdf', format='pdf', bbox_inches='tight')