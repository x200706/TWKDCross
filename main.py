import pandas as pd
from talib import abstract
import twstock # 沒有加權指數
import lxml

sid = '0050'

data=twstock.Stock(sid)
df = pd.DataFrame(data.fetch_from(2022, 1))

df.set_index('date', inplace = True)
df_month = df.resample('M').agg({'high':'max', 'low':'min', 'close':'last'})
print(df_month)

t = abstract.STOCH(df_month, fastk_period=9, slowk_period=3, slowd_period=3).tail(10)
print(t)

# cross