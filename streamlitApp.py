#!/usr/bin/env python
# coding: utf-8

# In[]:

import os
import pandas as pd

import streamlit as st

import plotly.express as px
from numerize.numerize import numerize


# In[ ]:


source_dir = os.path.join(os.getcwd(), 'reports/')


# In[ ]:


data = pd.read_csv(source_dir + 'players_db.csv', sep = ',')

print(data.shape)
print(data.head())


# In[ ]:


st.set_page_config(page_title = 'FantaSbori App',
                   layout = 'wide',
                   initial_sidebar_state = 'collapsed')

# st.cache


# In[ ]:


header_left, header_mid, header_right = st.columns([1, 2, 1], gap = 'large')


# In[ ]:


with header_mid:
    
    st.title('FantaSbori APP')

with st.sidebar:
    
    Role_filter = st.multiselect(label = 'Role',
                             options = data['Role'].unique(),
                             default = data['Role'].unique())
    
    Club_filter = st.multiselect(label = 'Club',
                                 options = data['Club'].unique(),
                                 default = data['Club'].unique())

    Squad_filter = st.multiselect(label = 'Squad',
                                  options = data['Squad'].unique(),
                                  default = data['Squad'].unique())
    
    Player_filter = st.selectbox(label = 'Player',
                                   options = data['Player'].drop_duplicates().sort_values(),
                                   placeholder = 'Select player')


# In[ ]:


data1 = data.query('Role == @Role_filter & Club == @Club_filter & Squad == @Squad_filter & Player == @Player_filter')

# total_impressions = float(df1['Impressions'].sum())
# total_clicks = float(df1['Clicks'].sum())
# total_spent = float(df1['Spent'].sum())
# total_conversions= float(df1['Total_Conversion'].sum()) 
# total_approved_conversions = float(df1['Approved_Conversion'].sum())

# total1, total2, total3,total4,total5 = st.columns(5,gap='large')


# In[ ]:





# In[ ]:


# Obtain information from tag <table>
# stats_table = soup.find(‘table’, id = ’main_table_countries_today’)
# stats_table


# In[ ]:


# Obtain every title of columns with tag <th>
# stats_tableheaders = []

# for i in stats_table.find_all(‘th’):
# #  title = i.text
#  headers.append(title)


# In[ ]:


# Create a dataframe
# stats = pd.DataFrame(columns = headers)

# Create a for loop to fill mydata
# for j in stats_table.find_all(‘tr’)[1:]:
#  row_data = j.find_all(‘td’)
#  row = [i.text for i in row_data]
#  length = len(stats)
#  stats.loc[length] = row


# In[ ]:


# from selenium import webdriver

# import time
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# download_dir = "/Users/carletch/Downloads/"

# options = Options()
# options.add_experimental_option('prefs',  {
#     "download.default_directory": download_dir,
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "plugins.always_open_pdf_externally": True
#     }
# )
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service = service, options = options)

# driver.get('https://www.fanta.soccer/it/archivioquotazioni/A/2023-2024/')
# time.sleep(3)
# driver.quit()


# In[ ]:




