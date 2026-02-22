import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

class DataProcessor:
    def __init__(self):
        self.engine = create_engine(f"mysql+pymysql://root:{os.getenv('DB_PASSWORD')}@127.0.0.1:3306/macro_etl_db")

    def process_data(self):
        print("🍳 Starting the 'Gold' transformation with Business Integration...")
        
        # 1. Load Macro Data
        cpi = pd.read_csv('data/raw/canada_cpi.csv')
        rates = pd.read_csv('data/raw/cad_usd_rate.csv')

        # 2. Rename & Clean
        cpi.columns = ['date', 'inflation_index']
        rates.columns = ['date', 'exchange_rate']
        cpi['date'] = pd.to_datetime(cpi['date'])
        rates['date'] = pd.to_datetime(rates['date'])

        # 3. Resample Daily Rates to Monthly Average
        rates.set_index('date', inplace=True)
        monthly_rates = rates.resample('MS').mean().reset_index()

        # 4. Merge Macro Data (CPI + Rates)
        macro_df = pd.merge(cpi, monthly_rates, on='date', how='inner')

        # 5. MOCK COMPANY DATA 
        # We generate sales that are loosely influenced by the inflation index
        np.random.seed(42)
        sales_dates = macro_df['date']
        
        # Base sales + a random factor + a slight 'inflationary' boost
        base_sales = 50000 
        noise = np.random.normal(0, 5000, len(sales_dates))
        mock_sales = base_sales + (macro_df['inflation_index'] * 100) + noise
        
        sales_df = pd.DataFrame({
            'date': sales_dates,
            'company_revenue_cad': mock_sales.round(2)
        })

        # 6. Macro Data + Company Data
        gold_df = pd.merge(macro_df, sales_df, on='date', how='inner')
        
        # 7. Save to MySQL "Gold" Table
        gold_df.to_sql('gold_macro_trends', self.engine, if_exists='replace', index=False)
        print(f"🏆 Gold Data Ready! Merged Macro Indicators with Company Sales ({len(gold_df)} months).")

if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_data()