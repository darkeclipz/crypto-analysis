import poloniex
import helpers
import plotly
import plotly.graph_objs as go

def create_chart():
    
    raw = poloniex.get_chart('USDT_BTC', helpers.get_unix_time_minus_days(3), poloniex._30MIN)
    series = [(helpers.parse_unix_date(d['date']),float(d['open']),float(d['high']),float(d['low']),float(d['close'])) for d in raw]

    """
    trace0 = go.Candlestick(
        x=[z[0] for z in series],
        open=[z[1] for z in series],
        high=[z[2] for z in series],
        low=[z[3] for z in series],
        close=[z[4] for z in series],
        increasing=dict(line=dict(color= '#17BECF')),
        decreasing=dict(line=dict(color= '#7F7F7F'))
    )
    """
    trace0 = go.Scatter(
        x=[z[0] for z in series],
        y=[z[4] for z in series],
        name='Close',
        line = dict(
        color = ('rgba(0,0,0,0.6)'),
        width = 4)
    )

    trace1 = go.Scatter(
        x=[z[0] for z in series],
        y=[z[2] for z in series],
        name='High',
        line = dict(
            color = ('rgba(12, 200, 24, 0.3)'),
            width = 4,
            dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'
    )

    trace2 = go.Scatter(
        x=[z[0] for z in series],
        y=[z[3] for z in series],
        name='Low',
        line = dict(
            color = ('rgba(205, 12, 24, 0.3)'),
            width = 4,
            dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'
    )


    data = [trace0,trace1,trace2]

    layout = dict(title = 'USDT/BTC, PLNX, 30',titlefont = dict(size=28), showlegend=True)
    fig = dict(data=data, layout=layout)
    
    #plotly.offline.plot(fig, filename='usdt_btc_plnx.html')
    return plotly.offline.plot(fig, include_plotlyjs=False, output_type='div').replace('"showLink": true', '"showLink": false')

