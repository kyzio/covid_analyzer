import pandas as pd
import glob

path = './csse_covid_19_data/csse_covid_19_daily_reports_us/*.csv'
all_files = glob.glob(path)
df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)
df = df.sort_values(by=['Province_State', 'Last_Update'])
print(df.head(30))