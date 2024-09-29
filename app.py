from flask import Flask, render_template, request
from market_data import get_market_data
from gaia_client import GaiaClient

app = Flask(__name__)

# Initialize GaiaClient with your GaiaNet node URL
gaia_client = GaiaClient(node_url='https://llama.us.gaianet.network/v1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/market_data', methods=['POST'])
def market_data():
    symbol = request.form.get('symbol', 'BTCUSDT')
    data = get_market_data(symbol)
    
    # Posting data to GaiaNet
    response = gaia_client.post_data('https://llama.us.gaianet.network/v1', data)
    
    return render_template('market_data.html', data=data)

@app.route('/retrieve_data', methods=['GET'])
def retrieve_data():
    endpoint = 'your-retrieve-endpoint'
    data = gaia_client.get_data(endpoint)
    return render_template('retrieve_data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
