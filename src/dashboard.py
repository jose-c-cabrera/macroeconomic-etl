import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objects as go
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Database Connection
engine = create_engine(f"mysql+pymysql://root:{os.getenv('DB_PASSWORD')}@127.0.0.1:3306/macro_etl_db")

def load_gold_data():
    try:
        return pd.read_sql("SELECT * FROM gold_macro_trends ORDER BY date ASC", engine)
    except Exception as e:
        st.error("⚠️ Database Error: Ensure you ran main.py or processor.py first!")
        st.stop()

# 2. Page Config
st.set_page_config(page_title="Canada Economic Pulse", layout="wide")
st.title("🇨🇦 Canada Economic Insight Dashboard")
st.markdown("### Comparing Internal Sales vs. National Macro Trends")

# 3. Load Data
df = load_gold_data()

# 4. Create the Dual-Axis Chart
fig = go.Figure()

# --- THE THREE LINES ---

# A. Inflation (CPI) - Primary Y-Axis
fig.add_trace(go.Scatter(
    x=df['date'], y=df['inflation_index'],
    name="Canada CPI (Inflation)",
    line=dict(color='royalblue', width=4)
))

# B. Company Revenue - Primary Y-Axis
fig.add_trace(go.Scatter(
    x=df['date'], y=df['company_revenue_cad'],
    name="Company Revenue (CAD)",
    line=dict(color='forestgreen', width=3, dash='solid')
))

# C. Exchange Rate - Secondary Y-Axis 
fig.add_trace(go.Scatter(
    x=df['date'], y=df['exchange_rate'],
    name="CAD/USD Rate",
    line=dict(color='firebrick', width=3, dash='dot'),
    yaxis="y2"
))

# 5. Layout Styling 
fig.update_layout(
    xaxis_title="Timeline",
    yaxis=dict(
        title=dict(text="CPI & Revenue Scale", font=dict(color="royalblue")), 
        tickfont=dict(color="royalblue")
    ),
    yaxis2=dict(
        title=dict(text="Exchange Rate (CAD per 1 USD)", font=dict(color="firebrick")), 
        tickfont=dict(color="firebrick"), 
        anchor="x", 
        overlaying="y", 
        side="right"
    ),
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig, use_container_width=True)

# 6. Data Table Audit
with st.expander("🔍 See Raw Merged Data"):
    st.dataframe(df)

# 7. Economic Correlation Analysis
st.subheader("📊 Economic Correlation Analysis")
correlation = df['inflation_index'].corr(df['exchange_rate'])

col1, col2 = st.columns(2)
with col1:
    st.metric("Correlation (CPI vs CAD/USD)", f"{correlation:.2f}")
    
with col2:
    if correlation > 0.5:
        st.write("✅ **Strong Positive Correlation:** As inflation rises, the CAD tends to weaken against the USD.")
    elif correlation < -0.5:
        st.write("📉 **Strong Negative Correlation:** The CAD strengthens as inflation rises.")
    else:
        st.write("⚖️ **Weak Correlation:** These two factors are currently moving independently.")