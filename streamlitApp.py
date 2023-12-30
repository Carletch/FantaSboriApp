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


# header_left, header_mid, header_right = st.columns([1, 2, 1], gap = 'large')


# In[ ]:


# with header_mid:
    
st.title('FantaSbori APP')

with st.sidebar:
    
    Squad_filter = st.selectbox(label = 'Squad',
                                options = data['Squad'].drop_duplicates().sort_values()),

    Club_filter = st.selectbox(label = 'Club',
                                 options = data['Club Name'].drop_duplicates().sort_values()),
    
    Role_filter = st.multiselect(label = 'Role',
                            options = data['Role'].unique(),
                            default = data['Role'].unique())
    
    # Player_filter = st.selectbox(label = 'Player',
                                  # options = data['Player'].drop_duplicates().sort_values())


# In[ ]:

data_slice = data
# data_slice = data.query('Role == @Role_filter & Club == @Club_filter & Squad == @Squad_filter') # & Player == @Player_filter')

# total1, total2, total3,total4,total5 = st.columns(5,gap='large')

data_1 = data_slice.sort_values('Current Quote', ascending = False).head(10)
# print(data_bar.head())
# fig = px.bar(data_bar, x = 'Player', y = 'Goals Scored')
# fig.show()
st.bar_chart(data_1,
             x = 'Player',
             y = 'Current Quote') #,
             # color = 'Role',
             # sort = None,
             # use_container_width = False) 

data_c = int(data_slice[data_slice['Owner'] != 'Carle']['Current Gain/Loss'].sum())
data_n = int(data_slice[data_slice['Owner'] != 'Nippon']['Current Gain/Loss'].sum())
data_s = int(data_slice[data_slice['Owner'] != 'Scap']['Current Gain/Loss'].sum())
data_m = int(data_slice[data_slice['Owner'] != 'Marce']['Current Gain/Loss'].sum())
data_f = int(data_slice[data_slice['Owner'] != 'Fracca']['Current Gain/Loss'].sum())
data_d = int(data_slice[data_slice['Owner'] != 'Demian']['Current Gain/Loss'].sum())
# st.bar_chart(data_2, x = 'Owner', y = 'Current Gain/Loss', use_container_width = False) #, color = 'Role')

# data_c, data_n, data_s, data_m, data_f, data_d = st.columns(6)
# Row A
a1, a2, a3 = st.columns(3)
a1.metric("Carle", f"{data_c}")
a2.metric("Nippon", f"{data_n}")
a2.metric("Scap", f"{data_s}")

# with data_c:
    # st.image('images/impression.png',use_column_width='Auto')
#     st.metric(label = 'Carle', vapip install talue = data_c)
    
# with data_n:
#     # st.image('images/tap.png',use_column_width='Auto')
#     st.metric(label = 'Nippon', value = data_n)

# with data_s:
    # st.image('images/hand.png',use_column_width='Auto')
#     st.metric(label = 'Scap', value = data_s)

# with data_m:
    # st.image('images/conversion.png',use_column_width='Auto')
#     st.metric(label = 'Marce', value = data_m)

# with data_f:
     # st.image('images/app_conversion.png',use_column_width='Auto')
#     st.metric(label = 'Fracca', value = data_f)

# with data_d:
    # st.image('images/app_conversion.png',use_column_width='Auto')
#     st.metric(label = 'Demian', value = data_d)


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




