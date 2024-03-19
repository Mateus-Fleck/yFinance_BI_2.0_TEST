import yfinance as yf

def carregar_dados(ticker):
    df = yf.Ticker(ticker).history("10y")
    df.reset_index(inplace=True)
    df['ticker'] = ticker.split(".")[0]
    return df

b3braislbolsabalcao = carregar_dados("B3SA3.SA")
caixaeconomica = carregar_dados("CXSE3.SA")
bancodobrasil = carregar_dados("BBAS3.SA")
itau = carregar_dados("ITUB4.SA")

b3braislbolsabalcao.head()
b3braislbolsabalcao.info()
caixaeconomica.head()
bancodobrasil.head()
itau.head()



