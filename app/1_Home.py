import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Open_Pubs",
    page_icon = "🎑",
)

st.title("Welcome!!!")

st.write("🎇County Durham has highest number of pubs in London")
st.write("🎇The Red Lion Pub has 193 branches all over London")
st.write("🎇The most popular pubs in london are")
p = ["The Red Lion","The Royal Oak","The Crown Inn"]
df = pd.DataFrame(p)
df.columns = ["Top 3 Pubs"]
st.write(df)
#st.sidebar.success("Select a page above.")
