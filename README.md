🇨🇦 Canada Economic Data Pipeline (ETL)
Automating Macroeconomic & Business Impact Analysis

This project is a professional-grade ETL (Extract, Transform, Load) pipeline that integrates real-time macroeconomic data from the St. Louis Fed (FRED) with internal business sales data. It demonstrates a Medallion Architecture to provide actionable insights into how inflation and exchange rates correlate with company revenue.

🏗️ Architecture: The Medallion Approach
I implemented a modular design to ensure data integrity and scalability:

Bronze Layer (Raw): Scripts fetch raw JSON/CSV data from external APIs and store them as local audit trails.

Silver Layer (Cleaned): Data is cleaned, typed, and loaded into MySQL using SQLAlchemy schemas.

Gold Layer (Business-Ready): A custom Python processor handles frequency mismatches (Daily Exchange Rates vs. Monthly Inflation) using Pandas Resampling to create a unified analysis table.

🛠️ Tech Stack
Language: Python 3.9+

Libraries: Pandas, NumPy, SQLAlchemy, Fredapi, Streamlit, Plotly

Database: MySQL

DevOps: Git, Dotenv (Environment Security)

📊 Business Case & Insights
The core goal of this project is to answer: "How is the current Canadian inflation trend affecting our local business revenue?"

Key Features:

Automated Data Sourcing: Real-time connection to Canada's Consumer Price Index (CPI) and CAD/USD exchange rates.

Business Correlation: Automatic calculation of the Pearson correlation coefficient between macro indicators and sales.

Interactive Dashboard: A dual-axis visualization that allows stakeholders to compare metrics with different scales (e.g., Currency vs. Revenue).

🚀 How to Run Locally
Clone the repo:

```Bash
git clone https://github.com/YOUR_USERNAME/macroeconomic-etl.git
cd macroeconomic-etl
```
Set up the environment:


python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Configure Secrets:
Create a .env file and add your FRED_API_KEY and DB_PASSWORD.

Execute the Pipeline:

```Bash
python main.py
```
Launch Dashboard:

```Bash
streamlit run src/dashboard.py
```
👨‍💻 About the Author
Jose Cabrera Programmer | Economist Passionate about bridging the gap between data engineering and economic strategy.
