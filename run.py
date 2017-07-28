import sys
sys.path.append('analysis')

import coinmarketcap
import percentage_change_charts as pcc


print('Retrieving data...')
limit = 100
data = coinmarketcap.retrieve_data()
pcc.create_change_in_percentage_chart(data, 'cbct50', 'percent_change_1h', 'percent_change_24h', 'Change in % by Top '+str(limit)+' Coins (1H/24H)', '% Change (1H)', '% Change (24H)', limit)
pcc.create_change_in_percentage_chart(data, 'cbc2t50', 'percent_change_24h', 'percent_change_7d', 'Change in % by Top '+str(limit)+' Coins (24H/7D)', '% Change (24H)', '% Change (7D)', limit)

print('Done :-)')
