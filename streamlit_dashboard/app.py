import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import warnings

st.set_page_config(page_title="Layoffs Dashboard", page_icon=":bar_chart:", layout="wide")
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)
df = pd.read_csv("C:\\Users\\saravaj\\Desktop\\college\\currentproject\\final_data.csv")

# Decorative heading
st.write("<h1 style='text-align: center; color: #ff5733;'>Layoffs Dashboard</h1>", unsafe_allow_html=True)

# Filter by company
st.header("Filter Laid Off Count By Company:")
company = st.multiselect(
    "Select the Company:",
    options=df["Company"].unique(),
    default=[]
)

# Display table and chart side by side
if company:
    df_selection = df[df["Company"].isin(company)]

    # Display chart
    st.write("### Laid Off Count Chart")

    # Define the layout with two columns
    col1, col2 = st.columns([2, 3])

    # Display the chart in the first column
    with col1:
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(df_selection["Company"], df_selection["Laid_Off_Count"])
        ax.set_xlabel('Company', fontsize=14)
        ax.set_ylabel('Laid_Off_Count', fontsize=14)
        ax.set_title('Laid Off Count by Company', fontsize=16)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    # Display the table in the second column
    with col2:
        # Display table
        table_html = df_selection[["Company", "Laid_Off_Count"]].to_html(index=False, escape=False)
        st.write(table_html, unsafe_allow_html=True)

st.header("Filter Laid Off Count By Country:")
country = st.multiselect(
    "Select the Country:",
    options=df["Country"].unique(),
    default=[]
)
# Display table and chart side by side
if country:
    df_selection = df[df["Country"].isin(country)]
    df_grouped = df_selection.groupby("Country").agg({"Laid_Off_Count": "sum"}).reset_index()

    # Display table
    st.write("### Total Laid Off Count by Country")
    st.write(df_grouped)

    # Display chart
    st.write("### Laid Off Count Chart by Country")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(df_grouped["Country"], df_grouped["Laid_Off_Count"])
    ax.set_xlabel('Country', fontsize=14)
    ax.set_ylabel('Total Laid_Off_Count', fontsize=14)
    ax.set_title('Total Laid Off Count by Country', fontsize=16)
    plt.xticks(rotation=90)
    st.pyplot(fig)