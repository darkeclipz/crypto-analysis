import coinmarketcap
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py

data = coinmarketcap.retrieve_data()

limit = 50

lbl_symbol = "symbol"
lbl_1h = "percent_change_1h"
lbl_24h = "percent_change_24h"
lbl_rank = "rank"
    
series = [(d[lbl_1h], d[lbl_24h], d[lbl_symbol]) for d in data if d[lbl_1h] != None and d[lbl_24h] != None and int(d[lbl_rank]) <= limit]

x = [s[0] for s in series]
y = [s[1] for s in series]
z = [s[2] for s in series]


fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(z):
    ax.annotate(txt, (x[i], y[i]), fontsize=8)

fig.suptitle('Percentage Change by Symbol (Top: ' + str(limit) +')')
plt.xlabel('% Change (1-hour)')
plt.ylabel('% Change (24-hour)')

py.image.save_as(plt, filename='test.png')

"""
fig, ax = plt.subplots()
ax.scatter(x, y)

for i, pt in enumerate(series):
    ax.annotate(z[i], (x[i], y[i]))

plot_url = py.plot_mpl(fig, filename="mpl-scatter")
"""
