import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv2
from st_aggrid import AgGrid
import plotly.express as px
import io 
import time
online = pd.read_csv('onlinefraudMin.csv')
with st.sidebar:
    choose = option_menu("Online Fraud Payment", ["Home", "Controls1","Controls2", "Data View","Contact Us"],
                         icons=['house', 'gear', 'gear', 'list','phone'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "green", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#A3BFF2"},
        "nav-link-selected": {"background-color": "#56E0F6"},
    }
    )

if choose == "Home":
              
              col1, col2 = st.columns( [0.9, 0.1])
              with col1:              
                  st.markdown(""" <style> .font {
                  font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
                  </style> """, unsafe_allow_html=True)
                  st.markdown('<p class="font">About the App</p>', unsafe_allow_html=True)    
              with col2:              
                  st.write("")
                        
              st.write("A dataset is a collection of information concerning online payment")
              st.write("fraud that enables us to identify the transactions that are most likely to result in fraud.")
              st.write("In order to identify fraud in online payments, we will present historical data regarding fraudulent transactions.")
              st.write("We obtained the dataset for this work from Kaggle.com and made necessary modifications to it.") 


              col1, col2 = st.columns( [0.9, 0.1])
              with col1:              
                  st.markdown(""" <style> .font {
                  font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
                  </style> """, unsafe_allow_html=True)
                  st.markdown('<p class="font">Findings</p>', unsafe_allow_html=True)    
              with col2:              
                  st.write("")
                        
              st.write("Payment: According to the findings, the majority of the Old Balance organization spent less than $40,000 in payments.")
              st.write("Transfer: As the chart shows, the amount transferred has skyrocketed in the old balance organization. ")
              st.write("Cash_out: The chart depicts cash out, which has reached a nadir in the old balance organization.")
              st.write("Debit: In the old balance organization, the chart depicts the highest amount in debit of less than 45,000.")
              st.write("Cash_in: The chart shows that the majority of the cash in the old balance organization was less than $1,000,000.")

              
elif choose == "Data View":
      
      st.markdown(""" <style> .font {
          font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
          </style> """, unsafe_allow_html=True)
      st.markdown('<p class="font">View Your Data</p>', unsafe_allow_html=True)
      
      df = pd.DataFrame(online)
      @st.cache
      def convert_df(df):
          return df.to_csv().encode('utf-8')

      csv = convert_df(df)

      st.download_button(
          label="Download data as CSV",
          data=csv,
          file_name='download.csv',
          mime='text/csv',
      )
      st.dataframe(df)
      

elif choose == "Controls1":
      st.markdown(""" <style> .font {
          font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
          </style> """, unsafe_allow_html=True)
      st.markdown('<p class="font">Work with Controls</p>', unsafe_allow_html=True)
      new = st.selectbox("Select Pyment type", online['type'].unique())

      plot_type = st.radio("select the plot type", ['scatter', 'bar','area'])
      if plot_type == 'scatter':

          pl = alt.Chart(online[online['type'] == new]).mark_circle().encode(
              x='oldbalanceOrg',
              y='amount',
              tooltip=['oldbalanceOrg', 'amount']
          ).interactive()
          st.altair_chart(pl)
      elif plot_type == 'bar':
          pl = alt.Chart(online[online['type'] == new]).mark_bar().encode(
              x='oldbalanceOrg',
              y='amount',
              tooltip=['oldbalanceOrg', 'amount']
          ).interactive()
          st.altair_chart(pl)
      elif plot_type == 'area':
           pl = alt.Chart(online[online['type'] == new]).mark_area().encode(
              x='oldbalanceOrg',
              y='amount',
              tooltip=['oldbalanceOrg', 'amount']
           ).interactive()
           st.altair_chart(pl)
elif choose == "Controls2":
      with st.spinner('Wait for it...'):
           time.sleep(5)
           st.success('Done!')
           
      st.markdown(""" <style> .font {
          font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
          </style> """, unsafe_allow_html=True)
      st.markdown('<p class="font">Work with Controls</p>', unsafe_allow_html=True)
      new =st.multiselect('Type Of Payment',online['type'].unique())
      if len(new) > 0:
          plot_type = st.radio("select the plot type", ['line','rect'])
          if plot_type == 'line':
              pl = alt.Chart(online[online['type'] == new[0]]).mark_line().encode(
                  x='oldbalanceOrg',
                  y='amount',
                  tooltip=['oldbalanceOrg', 'amount']
              ).interactive()
              st.altair_chart(pl)
          elif plot_type == 'rect':
              pl = alt.Chart(online[online['type'] == new[0]]).mark_rect().encode(
                  x='oldbalanceOrg',
                  y='amount',
                  tooltip=['oldbalanceOrg', 'amount']
              ).interactive()
              st.altair_chart(pl)
elif choose == "Contact Us":
      st.markdown(""" <style> .font {
      font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
      </style> """, unsafe_allow_html=True)
      st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
      with st.form(key='columns_in_form2',clear_on_submit=True): 
                  st.write('Please Contact Us In Case Of Any Query!')
                  st.text_input(label='Please Enter Your Name') 
                  st.text_input(label='Please Enter Email') 
                  st.text_area('Please Enter Your Message')
                  st.multiselect('Subject',['Need Help', 'Data Correction', 'Feedback', 'Wrong Data'])
                  st.checkbox('I agree to send me promotional emails') 
                  submitted = st.form_submit_button('SEND')
                  if submitted:
                      st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
      

      
      
     
