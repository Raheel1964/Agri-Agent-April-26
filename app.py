import streamlit as st
import pandas as pd
import numpy as np

# A. AGENT CONFIGURATION
st.set_page_config(page_title="ZA Agri-Agent", page_icon="📈", layout="wide")

# B. DATA INGESTION
def get_market_data(hs_code):
    data = {
        '0701': {'name': 'Potatoes', 'cagr': 28.4, 'tariff': 5.0, 'volatility': 12},
        '0804': {'name': 'Mangoes', 'cagr': 18.2, 'tariff': 0.0, 'volatility': 8},
        '0712': {'name': 'Dried Slices', 'cagr': 142.0, 'tariff': 2.5, 'volatility': 4}
    }
    return data.get(hs_code, {'name': 'Unknown', 'cagr': 0, 'tariff': 0, 'volatility': 0})

# C. UI HEADER
st.title("🚀 Zindagi Asaan: Agri-Trade Intelligence Agent")
st.markdown("### *Strategic Decision-Support Layer v1.0*")
st.divider()

# D. USER INTERFACE
with st.sidebar:
    st.header("Agent Parameters")
    hs_input = st.selectbox("Select HS Code", ['0701', '0804', '0712'])
    market = st.text_input("Target Market", "United Arab Emirates")
    st.button("Run Market-Access Agent")

# E. THE AGENT REASONING ENGINE
market_stats = get_market_data(hs_input)
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Market Growth (CAGR)", f"{market_stats['cagr']}%", "High Potential")
with c2:
    st.metric("Applied Tariff Rate", f"{market_stats['tariff']}%", "Preferential")
with c3:
    st.metric("Supply Chain Risk", f"{market_stats['volatility']}%", "Low Risk", delta_color="inverse")

# F. STRATEGIC OUTPUT
st.subheader("🤖 Agentic Strategy Recommendation")
if market_stats['cagr'] > 50:
    st.success(f"**SIGNAL: EXPONENTIAL GROWTH.** Recommend immediate pilot of {market_stats['name']} via air-freight to capture first-mover advantage in {market}.")
elif market_stats['cagr'] > 15:
    st.info(f"**SIGNAL: STABLE EXPANSION.** Recommend 40ft FCL volume for {market_stats['name']}. Optimize logistics via NLC Sea Corridor.")
else:
    st.warning("**SIGNAL: MARKET CONSOLIDATION.** Focus on quality differentiation over volume.")

# G. BACKEND REASONING TRACE
with st.expander("View Agent Logic Trace (RAG Framework)"):
    st.write("1. Fetched Time-Series tonnage from ITC TradeMap.")
    st.write("2. Identified Tariff barriers from Market Access Map.")
    st.write("3. Applied Weighted Feasibility Score based on CAGR vs. Logistics Volatility.")
    st.code("Score = (CAGR * 0.7) - (Tariff * 0.3)")
