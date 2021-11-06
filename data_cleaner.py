import streamlit as st
import plotly_express as px
import pandas as pd
import io

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("Data Analyzer")

# Add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file. (200MB max)",
                         type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    #print("hello")

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

global numeric_columns
global non_numeric_columns
try:
    # add check box to sidebar
    check_box = st.sidebar.checkbox(label="Display dataset")

    if check_box:
    # lets show the dataset
        st.write(df)
    select = st.sidebar.selectbox('Tools', ['Describe data','Info about datasets',  'Find Missing value', 'Delete Column'], key='1')
    # st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
    # column filter data
    filtered = st.multiselect("Filter columns", options=list(df.columns), default=list(df.columns))
    st.write(df[filtered])
    #graph
    chart_select= st.sidebar.selectbox(
                    label='Select the chart type',
                    
                     options=['Scatterplots','Lineplot','Histogram','Funnel'])

            
    #st.sidebar.title("Analyzer",select)
    select = st.sidebar.selectbox('Tools', ['Info about datasets', 'Describe data', 'Find Missing value', 'Add column', 'Delete Column', 'Sort datasets','Change order'], key='1')
    

    if select == "Info about datasets":  
            buffer = io.StringIO()
            df.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
          
    elif select=='Describe data':
          
           s=df.describe()
           st.text(s)

    elif select=='Find Missing value':
            
             s=df.isnull().sum()
           
             st.text(s)
    # elif select=='Delete Column':
        
    #         s= del[df['id']]      
    #         st.text(s)




except Exception as e:
    print(e)
    st.write("Please upload file to the application.")
