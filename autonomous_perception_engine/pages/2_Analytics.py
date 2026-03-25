import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(layout="wide")

# -------------------------------
# UI
# -------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Analytics Dashboard")

# -------------------------------
# LOAD DATA
# -------------------------------
try:
    df = pd.read_csv("output/data.csv")

    st.subheader("📄 Data")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    # -------------------------------
    # PLOTLY BAR
    # -------------------------------
    with col1:
        fig1 = px.bar(df['label'].value_counts(),
                      title="Object Count")
        st.plotly_chart(fig1, use_container_width=True)

    # -------------------------------
    # PLOTLY PIE
    # -------------------------------
    with col2:
        fig2 = px.pie(df, names='label',
                      title="Distribution")
        st.plotly_chart(fig2, use_container_width=True)

    # -------------------------------
    # SEABORN
    # -------------------------------
    st.subheader("📊 Seaborn Analysis")

    fig, ax = plt.subplots()
    sns.countplot(x='label', data=df, ax=ax)
    st.pyplot(fig)

except:
    st.warning("⚠️ No data found. Please process a video first.")