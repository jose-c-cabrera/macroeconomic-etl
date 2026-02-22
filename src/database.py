from sqlalchemy import create_engine, Column, Date, Float, String
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()

# --- REGISTRATION STEP ---
class MacroIndicator(Base):
    __tablename__ = 'silver_macro_data'
    date = Column(Date, primary_key=True)
    indicator_name = Column(String(50), primary_key=True)
    value = Column(Float)

# Connection string
engine = create_engine(f"mysql+pymysql://root:{os.getenv('DB_PASSWORD')}@127.0.0.1:3306/macro_etl_db")

def init_db():

    Base.metadata.create_all(engine)
    print("Table 'silver_macro_data' created in MySQL!")