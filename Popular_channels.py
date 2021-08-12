import pandas as pd

country_list = ['CA', 'DE', 'IN', 'FR', 'GB', 'JP', 'KR', 'MX', 'RU', 'US']
df = pd.DataFrame()

for country in country_list:
    country_df = pd.read_csv('{}videos.csv'.format(country))
    country_df_grouped = country_df.groupby('channel_title').channel_title.count()
    df = df.join(country_df_grouped, how='outer', lsuffix='left')

df['sum']= df.sum(axis=1)
df.columns = country_list + ['sum']
df.sort_values('sum', ascending=False).to_excel('rating.xlsx')
df.sort_values('sum', ascending=False).dropna().to_excel('rating_na.xlsx')
print('sdfgsdgsfdhrhrh','\n', df.sort_values('sum', ascending=False).head(100).to_string())
