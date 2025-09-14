import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6]


model_scores = {
    'Qwen2-VL-7B-Instruct':         [0.49, 0.55, 0.80, 0.91, 0.88, 0.90],
    'LlaVA-v1.6-Mistral-7B':        [0.62, 0.70, 0.82, 0.91, 0.90, 0.92],
    'Llama-3.2-11B-Vision-Instruct':[0.41, 0.53, 0.78, 0.92, 0.90, 0.92],
    'GPT-4o':                        [0.17, 0.31, 0.49, 0.59, 0.65, 0.65],
    'Claude 3.7 Sonnet':            [0.15, 0.26, 0.46, 0.60, 0.61, 0.62],
    'GLM-4V-Plus':                  [0.32, 0.37, 0.75, 0.93, 0.93, 0.94],
    'Qwen-Vl-Plus':                 [0.28, 0.37, 0.69, 0.95, 0.95, 0.97]
}


colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2']
markers = ['o', 's', '^', 'v', 'D', '*', 'P']  


font_size = 17
plt.rcParams.update({'font.size': font_size})


plt.figure(figsize=(9, 5))

for i, (model, scores) in enumerate(model_scores.items()):
    plt.plot(
        x, scores,
        label=model,
        color=colors[i % len(colors)],
        marker=markers[i % len(markers)],
        linewidth=2
    )


plt.xlabel('Number of Visual Gadgets', fontsize=font_size)
plt.ylabel('ASR', fontsize=font_size)
plt.xticks(x)
plt.ylim(0, 1.0)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower right', fontsize=font_size - 1)

plt.tight_layout()
plt.show()

plt.savefig('./nof.pdf', format='pdf', bbox_inches='tight')