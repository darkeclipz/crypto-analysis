import plotly
import plotly.graph_objs as go
import numpy as np

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

print( plotly.offline.plot(data, include_plotlyjs=False, output_type='div') )
#py.offline.plot(data, include_plotlyjs=False, output_type='div')
