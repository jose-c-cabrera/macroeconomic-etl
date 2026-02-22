from src.fetcher import DataFetcher
from src.database import init_db
from src.processor import DataProcessor

def run_pipeline():
    print('---Starting Economic Data Pipeline---')

    #1 Fetch from FRED
    fetcher = DataFetcher()
    fetcher.fetch_macro_data()

    #2 Initialize database
    init_db()

    #3 Process and merge 
    processor = DataProcessor()
    processor.process_data()

    print("Pipeline Complete!")

if __name__ == '__main__':
    run_pipeline()