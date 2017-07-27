import plotly.plotly as py
import plotly.graph_objs as go
import coinmarketcap

data = coinmarketcap.retrieve_data()
series = [(d["percent_change_24h"], d["percent_change_7d"], d["symbol"]) for d in data if d["percent_change_24h"] != None and d["percent_change_7d"] != None and int(d["rank"]) < 50]
x, y, z = zip(*series)

trace0 = go.Scatter(
    x = x,
    y = y,
    mode = 'markers+text',
    name = 'Symbols',
    text = z,
    marker = dict(size=14,line=dict(width=1,color='rgba(0,0,0,.8)'), color='rgba(0,0,0,.2)'),
    textposition='top'
)

data = [trace0]

layout = go.Layout(
    title = 'Change in % by Coin (top: 50)',
    hovermode='closest',
    xaxis=dict(
        title='% Change (24-hours)'
    ),
    yaxis=dict(
        title='% Change (7-days)'
    ),
    showlegend = False
)

fig = go.Figure(data=data, layout=layout)
#py.image.save_as(fig, filename='plot.png')
py.plot(fig, filename='cbc2t50')


