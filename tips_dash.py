import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
df=pd.read_csv('data.csv')
#sidebar
st.sidebar.header("Data Dashboard")
st.sidebar.image('1.jpeg')
st.sidebar.write('This an EDA for data set of gym babay')
st.sidebar.write("")
st.sidebar.markdown('made with :heart: by :star2: :star2:[DR Yasmeen Abdelmohsen](https://www.linkedin.com/in/yasmeinabdelmohsen/)')
st.sidebar.write("")
filter1=st.sidebar.selectbox("Categorical",['Sex','Smoker','Color'])
filter2=st.sidebar.selectbox("Numerical",[None,'Pulse','Duration'])
st.sidebar.write("")
st.sidebar.write(filter1)
#body
# row a
a1,a2,a3=st.columns(3)
a1.metric("Maximum Calories Burn",df['Calories'].max())
a2.metric("Maximum Pulse ",df['Pulse'].max())
a3.metric("Maximum Duration ",df['Duration'].max())
# row b
fig=px.scatter(data_frame=df,x='Calories',y='Duration',size=filter2)
st.plotly_chart(fig,use_container_width=True)