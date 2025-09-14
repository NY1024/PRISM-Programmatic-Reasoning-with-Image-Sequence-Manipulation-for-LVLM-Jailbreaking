import matplotlib.pyplot as plt
import numpy as np


methods = ['No Defense', 'CIDER', 'AdaShield-S', 'AdaShield-A', 'JailGuard', 'ECSO']
models = ['Qwen2-VL-7B-Instruct', 'GPT-4o']


values = {
    'Qwen2-VL-7B-Instruct': [0.91, 0.90, 0.83, 0.75, 0.85, 0.70],
    'GPT-4o': [0.59, 0.58, 0.52, 0.48, 0.55, 0.43]
}


colors = ['#94b5d7','#83b5b5', '#bbd5d4', '#d7eaec', '#efe9d3', '#bfc5d5']


font_size = 17
plt.rcParams.update({'font.size': font_size})

x = np.arange(len(models))
bar_width = 0.12
offsets = np.linspace(-2.5, 2.5, len(methods)) * bar_width

fig, ax = plt.subplots(figsize=(9, 5))

for i, (method, color) in enumerate(zip(methods, colors)):
    scores = [values[model][i] for model in models]
    bars = ax.bar(x + offsets[i], scores, width=bar_width, label=method, color=color)

    
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.01,
            f'{height:.2f}',
            ha='center', va='bottom',
            fontsize=font_size
        )


ax.set_ylabel('ASR', fontsize=font_size)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=font_size)
ax.legend(title='Defense Method', fontsize=font_size - 1, title_fontsize=font_size)
ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

plt.savefig('./defense.pdf', format='pdf', bbox_inches='tight')