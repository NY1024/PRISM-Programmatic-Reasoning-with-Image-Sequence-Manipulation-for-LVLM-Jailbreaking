import matplotlib.pyplot as plt
import numpy as np

models = ['Qwen2-VL-7B-Instruct', 'GPT-4o']
llms = ['GPT-4', 'Grok 3', 'Qwen3', 'Gemini 2.5']

scores = {
    'Qwen2-VL-7B-Instruct': [0.91, 0.93, 0.90, 0.86],
    'GPT-4o': [0.59, 0.65, 0.61, 0.59]
}


group_distance = 0.8  
x = np.array([0, group_distance])

bar_width = 0.15
font_size = 17
plt.rcParams.update({'font.size': font_size})

fig, ax = plt.subplots(figsize=(9, 5))

offsets = np.array([-1.5, -0.5, 0.5, 1.5]) * bar_width
colors = ['#94b5d7', '#83b5b5', '#bbd5d4', '#d7eaec']

for i, (llm, color) in enumerate(zip(llms, colors)):
    vals = [scores[model][i] for model in models]
    bars = ax.bar(x + offsets[i], vals, width=bar_width, label=llm, color=color)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.01,
                f'{height:.2f}', ha='center', va='bottom', fontsize=font_size - 1)

ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(0, 1.0)
ax.set_ylabel('Score', fontsize=font_size)
ax.legend(title='Auxiliary LLM', fontsize=font_size - 1, title_fontsize=font_size)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

plt.savefig('./llm_ab.pdf', format='pdf', bbox_inches='tight')