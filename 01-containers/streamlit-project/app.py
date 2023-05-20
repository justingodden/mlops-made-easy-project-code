import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/justingodden/mlops-made-easy-project-code/master/01-containers/streamlit-project/vgsales.csv"


@st.cache_data
def load_data(url):
    dataset = pd.read_csv(url)
    return dataset


data = load_data(url)

st.title("Video Game Data App")
n = st.slider("Top N Companies", 1, 20, 5)
st.header(f"Total Sales Broken by Regious for top {n} Companies")
st.bar_chart(
    data.groupby("Publisher")[
        ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
    ]
    .sum()
    .sort_values(ascending=False, by="Global_Sales")
    .drop("Global_Sales", axis=1)
    .head(n)
)

st.header("Total Sales per Year")
st.line_chart(data.groupby("Year")["Global_Sales"].sum())
