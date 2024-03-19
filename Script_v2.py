import yfinance as yf

def carregar_dados(ticker):
    df = yf.Ticker(ticker).history("10y")
    df.reset_index(inplace=True)
    df['ticker'] = ticker.split(".")[0]
    return df

# Tickers dos 10 principais bancos brasileiros
tickers = ["BBAS3.SA", "ITUB4.SA", "BBDC4.SA", "SANB11.SA", "BBDC3.SA", 
           "SANB3.SA", "BPAC11.SA", "BIDI11.SA", "ABCB4.SA", "SAFR3.SA"]

# Carregar dados para cada ticker
dados_bancos = {}
for ticker in tickers:
    dados_bancos[ticker.split(".")[0]] = carregar_dados(ticker)

# Exibir informações para um dos bancos
print(dados_bancos["BBAS3"].head())
print(dados_bancos["BBAS3"].info())