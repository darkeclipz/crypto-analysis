import sys
sys.path.append('analysis')

from datetime import datetime
import coinmarketcap
import percentage_change_charts as pcc
import btc_chart as btc


print('Retrieving data...')
limit = 100
data = coinmarketcap.retrieve_data()

# Creating the plots
plot1 = pcc.create_change_in_percentage_chart(data, 'cbct50', 'percent_change_1h', 'percent_change_24h', 'Change in % by Top '+str(limit)+' Coins (1H/24H)', '% Change (1H)', '% Change (24H)', limit)
plot2 = pcc.create_change_in_percentage_chart(data, 'cbc2t50', 'percent_change_24h', 'percent_change_7d', 'Change in % by Top '+str(limit)+' Coins (24H/7D)', '% Change (24H)', '% Change (7D)', limit)
plot3 = btc.create_chart()

# Fetch the HTML template file
template = ''
with open('template.html', 'r') as f:
    template = f.read()

# Insert the HTML
template = template.replace('{{Plot1}}', plot1)
template = template.replace('{{Plot2}}', plot2)
template = template.replace('{{Plot3}}', plot3)
template = template.replace('{{LastUpdate}}', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Write to file
f = open('index.html', 'w')
f.write(template)
f.close()

