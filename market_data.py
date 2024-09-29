import requests

def get_market_data(symbol='BTCUSDT'):
    url = f'https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    return {
        'symbol': data['symbol'],
        'price': float(data['lastPrice']),
        'high': float(data['highPrice']),
        'low': float(data['lowPrice']),
        'volume': float(data['volume']),
    }
