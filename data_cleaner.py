'''
Name :SaVed
Created by Khandoker Tanjim Ahammad
Date: 11/11/21
updated: 13/11/21

Purpose: Analyze any data sets using streamlit
Limitations: often datasets contain too much text does not work

'''

import streamlit as st
import plotly_express as px
import pandas as pd
import io
import seaborn as sns


# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("SaVeD")
st.title("A simple tools to analyze excel data and also to visualize data to find out the relation between the columns in datasets")
# Add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file. (200MB max)",
                         type=['csv', 'xlsx'])
st.sidebar.markdown("Maintained by: [Khandoker Tanjim Ahammad](https://github.com/Khandoker09)")
# Defining data set as global variable 
global df
if uploaded_file is not None:
    print(uploaded_file)
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)
try:

    # add check box to sidebar
    check_box = st.sidebar.checkbox(label="Display dataset")
    # Make a tic box to decide we want to see the data or not 
    if check_box:
    # lets show the dataset
        st.write(df)
    # 1st Sidebar Select Box for analyze data sets 
    select = st.sidebar.selectbox('Analyze', ['Info about datasets', 'Describe data',  'Find Missing value','Correlation Matrix'])
    #2nd sidebar-- filtering all the column 
    filtered = st.multiselect("Overall columns", options=list(df.columns), default=list(df.columns))
    st.write(df[filtered])
    # Generate output using bunch of If else 
    if select == "Info about datasets":  
            buffer = io.StringIO()
            df.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
    
    elif select=='Describe data':
        
        buffer = io.StringIO()
        s= df.describe()
        st.table(s)

    elif select== 'Find Missing value':
        buffer = io.StringIO()
        s= df.isnull().sum()
        st.table(s)

    elif select == 'Correlation Matrix':
        fig, ax = plt.subplots(figsize=(10,10))
        sns.heatmap(df.corr(), annot=True, ax=ax)
        st.pyplot(fig)
    #3rd side bar to decide which graph to show 
    chart_select= st.sidebar.selectbox(
                    label='Select the chart type',
                     options=['Scatterplots','Lineplot','Histogram','Boxplot','Barchart','Funnel'])
    # Generate output using bunch of If else to show proper graph 
    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Scatterplot Settings")
        x_values = st.sidebar.selectbox('X axis', options= df.columns)
        y_values = st.sidebar.selectbox('Y axis', options= df.columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        #Display the chart
        st.plotly_chart(plot)


    elif chart_select == 'Lineplot':
        st.sidebar.subheader("Line Plot Settings")
        x_values = st.sidebar.selectbox('X axis', options=df.columns )
        y_values = st.sidebar.selectbox('Y axis', options=df.columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)

    elif chart_select == 'Histogram':
        st.sidebar.subheader("Histogram Settings")
        x = st.sidebar.selectbox('Feature', options=df.columns)
        bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                     max_value=100, value=40)
        plot = px.histogram(x=x, data_frame=df)
        st.plotly_chart(plot)



    elif chart_select == 'Boxplot':
        st.sidebar.subheader("Boxplot Settings")
        x = st.sidebar.selectbox("X axis", options=df.columns)
        y = st.sidebar.selectbox("Y axis", options=df.columns)
        plot = px.box(data_frame=df, x=x, y=y)
        st.plotly_chart(plot)
    
    elif chart_select == 'Barchart':
        st.sidebar.subheader("Barchart Settings")
        x = st.sidebar.selectbox("X axis", options=df.columns)
        y = st.sidebar.selectbox("Y axis", options=df.columns)
        plot = px.bar(data_frame=df, x=x, y=y)
        st.plotly_chart(plot)

    elif chart_select == 'Funnel':
        st.sidebar.subheader("Funnel Settings")
        x = st.sidebar.selectbox("X axis", options=df.columns)
        y = st.sidebar.selectbox("Y axis", options=df.columns)
        plot = px.funnel(data_frame=df, x=x, y=y)
        st.plotly_chart(plot)
    elif chart_select == 'Funnel':
        st.sidebar.subheader("Funnel Settings")
        x = st.sidebar.selectbox("X axis", options=df.columns)
        y = st.sidebar.selectbox("Y axis", options=df.columns)
        plot = px.wis(data_frame=df, x=x, y=y)
        st.plotly_chart(plot)


except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

