import os
from fredapi import Fred
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class DataFetcher:
    def __init__(self):
        self.fred = Fred(api_key = os.getenv('FRED_API_KEY'))

    def fetch_macro_data(self): 
        #To fetch Inflation and Exchange Rate
        series = {
            'canada_cpi':'CPALTT01CAM659N',
            'cad_usd_rate' : 'DEXCAUS'
        }

        for name, s_id in series.items():
            print(f'Fetching {name}...')
            data = self.fred.get_series(s_id)
            df = pd.DataFrame(data, columns=[name])
            df.to_csv(f'data/raw/{name}.csv')
            print(f'Saved raw data {name} to data/raw')

if __name__ == "__main__":
    fetcher = DataFetcher()
    fetcher.fetch_macro_data()