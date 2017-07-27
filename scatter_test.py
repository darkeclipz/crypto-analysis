import plotly.plotly as py
import plotly.graph_objs as go
import coinmarketcap

print('Retrieving data...')
data = coinmarketcap.retrieve_data()

print('Generating plot...')
series = [(-1.5,-5.6,'DGB'), (10,-5,'XRP'), (5,3,'BTC'), (12,-3,'PIVX')]
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
        title='% Change (1-hour)'
    ),
    yaxis=dict(
        title='% Change (24-hour)'
    ),
    showlegend = False
)

fig = go.Figure(data=data, layout=layout)

print('Saving to file...')
py.image.save_as(fig, filename='plot.png')

print('Saved as plot.png')
