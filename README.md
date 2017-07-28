# Analysis of Cryptocurrencies
Analyzing the top cryptocurrencies with Python. 

The result can be seen at <https://darkeclipz.github.io/crypto-analysis/>.

## Installation
1. Clone the project `git clone https://github.com/darkeclipz/crypto-analysis`
2. Install Python 3.x
3. Install required libraries (`requests`, `plotly`)
4. Set up the Plotly API key `plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')`.

## Usage
Execute `run.py` to generate the plots, the result can be found in the `index.html` file. It is generated from the `template.html` file. 

## Hosting
Currently the website is hosted at this GitHub. A Linux VPS is updating the `index.html` file every five minutes and pushes the changes to GitHub.

## Data
Using data from publicly available API's:
* <http://www.coinmarketcap.com>
* <http://www.poloniex.com>

## License
MIT