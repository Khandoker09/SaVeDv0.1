'''
Author: Khandoker Tanjim Ahammad
Date: 16/09/2023
puropose: implement vlookup, hlookup and compare in streamlit
'''
import pandas as pd
import io
import streamlit as st


st.markdown(f"""

This page work with multiple datasets. 
Finding the mismached data in both data sets or appending new data in the existing database
and drop duplicates are the main function of this page.

Important Notes:
* Support both .csv or both .xlsx file

   """)

#st.title("Append/drop duplicates on Multiple Datasets")

# Create file upload widgets for two datasets
uploaded_file_1 = st.file_uploader("Upload the first dataset (CSV or Excel)", type=["csv", "xlsx"])
uploaded_file_2 = st.file_uploader("Upload the second dataset (CSV or Excel)", type=["csv", "xlsx"])

def loadfile():
    # Load and display the first dataset
    if uploaded_file_1 is not None: 
        if uploaded_file_1.name.endswith('.csv'):
            df1 = pd.read_csv(uploaded_file_1)
        elif uploaded_file_1.name.endswith('.xlsx'):
            df1 = pd.read_excel(uploaded_file_1, engine='openpyxl')
    if uploaded_file_2 is not None:
        if uploaded_file_2.name.endswith('.csv'):
            df2 = pd.read_csv(uploaded_file_2)
        elif uploaded_file_2.name.endswith('.xlsx'):
            df2 = pd.read_excel(uploaded_file_2, engine='openpyxl')  
    return df1, df2
def compare():
    df1,df2=loadfile()
    change=df1.compare(df2,align_axis=1)
    return change

def append_hlookdropdup():
     df1,df2 = loadfile()
     merge_df = pd.concat([df1,df2], axis=0, ignore_index=True)
     merge = list(merge_df) # Creates list of all column headers
     merge_df[merge] = merge_df[merge].astype(str)
     m=merge_df.drop_duplicates(keep='first')
     return m

if st.button("Compare DataFrames"):
    result = compare()
    st.write("Comparison Result:")
    st.write(result)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
       result.to_excel(writer)
    output.seek(0)
    st.download_button(
        label="Download mismatched data(xlsx)",
        data=output,
        file_name="mismatched.xlsx",
        key="download-button"
    )

if st.button("Apped/Extent Datasets"):
    result2 = append_hlookdropdup()
    st.write("After Append:")
    st.write(result2)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        result2.to_excel(writer, index=False)
    output.seek(0)
    st.download_button(
        label="Download Merged Data (xlsx)",
        data=output,
        file_name="appended_dataset.xlsx",
        key="download-button"
    )

from streamlit_extras.buy_me_a_coffee import button

button(username="alttanjimx ", floating=False, width=221)