import yfinance as yf

msft = yf.Ticker("MSFT")

# obter todas as informações da ação
msft.info

# obter dados de mercado históricos
hist = msft.history(period="50y")
hist.head()

# mostrar informações meta sobre o histórico (necessita que history() seja chamado primeiro)
msft.history_metadata

# mostrar ações 
#(dividendos, desdobramentos, ganhos de capital)
msft.actions
msft.dividends
msft.splits
msft.capital_gains  # apenas para fundos mútuos e ETFs

# mostrar contagem de ações
msft.get_shares_full(start="2022-01-01", end=None)

# mostrar dados financeiros:
# - demonstração de resultado
msft.income_stmt
msft.quarterly_income_stmt
# - balanço patrimonial
msft.balance_sheet
msft.quarterly_balance_sheet
# - demonstração de fluxo de caixa
msft.cashflow
msft.quarterly_cashflow
# veja `Ticker.get_income_stmt()` para mais opções

# mostrar detentores
msft.major_holders
msft.institutional_holders
msft.mutualfund_holders
msft.insider_transactions
msft.insider_purchases
msft.insider_roster_holders

# mostrar recomendações
msft.recommendations
msft.recommendations_summary
msft.upgrades_downgrades

# Mostrar datas de ganhos futuros e históricos, retornos para no máximo os próximos 4 trimestres e últimos 8 trimestres por padrão.
# Nota: Se mais forem necessários, use msft.get_earnings_dates(limit=XX) com argumento de limite aumentado.
msft.earnings_dates

# mostrar código ISIN - *experimental*
# ISIN = Número de Identificação de Valores Mobiliários Internacional
msft.isin

# mostrar expirações de opções
msft.options

# mostrar notícias
msft.news

# obter cadeia de opções para uma expiração específica
opt = msft.option_chain('YYYY-MM-DD')
# dados disponíveis através de: opt.calls, opt.puts
