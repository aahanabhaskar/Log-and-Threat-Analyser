import pandas as pd
df=pd.read_csv("log_report.csv")
import streamlit as st
st.title("Log And Threat Detector")
st.subheader("Detect :red[Threats] and brute force attempts by :red[suspicious] IPs")
st.markdown("All logs are classified into three categories which are : safe log-ins,suspicious logs and logs which need attention")
st.markdown(
    ":red-badge[Suspicious 🚨] :orange-badge[Attention Needed ⚠️] :green-badge[Safe Log-ins ✔️]"
)
st.write("Data Breakdown:")
n_sus = (df["Status"] == "Suspicious").sum()
n_att = (df["Status"] == "Attention Needed").sum()
n_safe = (df["Status"] == "Safe").sum()
def card(label, count, color):
    st.markdown(
        f"""
        <div style="background-color:{color}; padding:5px;
                    border-radius:12px; text-align:center; color:white;">
            <div style="font-size:16px;">{label}</div>
            <div style="font-size:36px; font-weight:bold;">{count}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
col1, col2, col3 = st.columns(3)
with col1:
    card("Suspicious 🚨", n_sus, "#d62828")
with col2:
    card("Attention Needed ⚠️", n_att, "#f77f00")
with col3:
    card("Safe ✔️", n_safe, "#17a34d")
st.divider()
st.write("Data Metrics:")
chart_df = pd.DataFrame({
    "Type": ["Suspicious", "Attention Needed", "Safe"],
    "Count": [n_sus, n_att, n_safe],
})
colu1,colu2=st.columns(2)
with colu1:
    st.dataframe(df)
with colu2:
    st.bar_chart(chart_df, x="Type", y="Count")
st.sidebar.title("Disclaimer:")
st.sidebar.markdown("All the IP addresses taken here are fictional and are not linked to any real IP address.This app is a tool to demonstrate suspicious and harmful IP addresses which can cause potential harm.")
st.sidebar.button("Got it!")
