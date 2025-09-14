import matplotlib.pyplot as plt
import numpy as np


samples = ['GPT-4o', 'Claude 3.7 Sonnet', 'GLM-4V-Plus', 'Qwen-VL-Plus']
methods = ['FS', 'MM', 'PRISM']  


values = {
    'FS':  [5.5, 6.0, 5.8, 4.7],
    'MM': [8.9, 6.5, 6.0, 7.2],
    'PRISM': [9.1, 7.2, 6.8, 7.5]
}


colors = {
    'FS':  '#3d5488',
    'MM': '#9ac9db',
    'PRISM': '#d3e2b7'
}


x = np.arange(len(samples))


width = 0.2


fig, ax = plt.subplots(figsize=(10, 6))


for i, method in enumerate(methods):
    offset = (i - 1) * width  
    bars = ax.bar(x + offset, values[method], width=width, label=method, color=colors[method])
    
 
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.1,
                f'{height:.1f}', ha='center', va='bottom', fontsize=10)


ax.set_xticks(x)
ax.set_xticklabels(samples)


ax.set_ylabel('ASR')


ax.legend()


ax.grid(axis='y', linestyle='--', alpha=0.7)


plt.tight_layout()


plt.show()
plt.savefig('./cm.pdf', format='pdf', bbox_inches='tight')
