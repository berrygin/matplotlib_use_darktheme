import matplotlib.pyplot as plt

"""dark background
https://github.com/matplotlib/matplotlib/blob/main/lib/matplotlib/mpl-data/stylelib/dark_background.mplstyle

lines.color: white
patch.edgecolor: white

text.color: white

axes.facecolor: black
axes.edgecolor: white
axes.labelcolor: white
axes.prop_cycle: cycler('color', ['8dd3c7', 'feffb3', 'bfbbd9', 'fa8174', '81b1d2', 'fdb462', 'b3de69', 'bc82bd', 'ccebc4', 'ffed6f'])
...
"""

# plt.style.use('dark_background')

colors_d = {
    'bluegreen': '#8dd3c7',
    'lemon': '#feffb3',
    'lilac': '#bfbbd9',
    'salmon': '#fa8174',
    'aero': '#81b1d2',
    'orange': '#fdb462',
    'junebud': '#b3de69',
    'violet': '#bc82bd',
    'mint': '#ccebc4',
    'yellow': '#ffed6f'
}

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

fig.set_facecolor('black')
ax.set_facecolor('black')
ax.set_title('Matplotlib Dark Theme', color='white')

ax.spines['top'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

num = len(colors_d)
x = range(num)
y = [1.0] * num

ax.bar(x, y, color=colors_d.values())
ax.set_xticks(x, labels=colors_d.keys(), rotation=90)

plt.show()