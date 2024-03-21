import yfinance as yf

petr4 = yf.Ticker("PETR4.SA")

# obter todas as informações da ação da Petrobras
petr4.info

# obter dados de mercado históricos (50 anos)
hist = petr4.history(period="50y")

# Ler Dataset
hist.head()

# mostrar informações meta sobre o histórico (necessita que history() seja chamado primeiro)
petr4.history_metadata

# mostrar ações 
#(dividendos, desdobramentos, ganhos de capital)
petr4.actions
petr4.dividends
petr4.splits
petr4.capital_gains  # apenas para fundos mútuos e ETFs

# mostrar contagem de ações
petr4.get_shares_full(start="2022-01-01", end=None)

# mostrar dados financeiros:
# - demonstração de resultado
petr4.income_stmt
petr4.quarterly_income_stmt
# - balanço patrimonial
petr4.balance_sheet
petr4.quarterly_balance_sheet
# - demonstração de fluxo de caixa
petr4.cashflow
petr4.quarterly_cashflow
# veja `Ticker.get_income_stmt()` para mais opções

# mostrar detentores
petr4.major_holders
petr4.institutional_holders
petr4.mutualfund_holders
petr4.insider_transactions
petr4.insider_purchases
petr4.insider_roster_holders

# mostrar recomendações
petr4.recommendations
petr4.recommendations_summary
petr4.upgrades_downgrades

# Mostrar datas de ganhos futuros e históricos, retornos para no máximo os próximos 4 trimestres e últimos 8 trimestres por padrão.
# Nota: Se mais forem necessários, use petr4.get_earnings_dates(limit=XX) com argumento de limite aumentado.
petr4.earnings_dates

# mostrar código ISIN - *experimental*
# ISIN = Número de Identificação de Valores Mobiliários Internacional
petr4.isin

# mostrar expirações de opções
petr4.options

# mostrar notícias
petr4.news

# obter cadeia de opções para uma expiração específica
opt = petr4.option_chain('YYYY-MM-DD')
# dados disponíveis através de: opt.calls, opt.puts
