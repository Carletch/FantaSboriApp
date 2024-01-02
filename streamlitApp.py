#!/usr/bin/env python
# coding: utf-8

# In[]:

import os
import pandas as pd

import altair as alt
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
    
st.title('FantaSbori App :soccer:')



# In[ ]:
    

# with st.sidebar:
    
#     Squad_filter = st.selectbox(label = 'Squad',
#                                 options = data['Squad'].drop_duplicates().sort_values()),
# 
#     Club_filter = st.selectbox(label = 'Club',
#                                  options = data['Club Name'].drop_duplicates().sort_values()),
#     
#     Role_filter = st.multiselect(label = 'Role',
#                             options = data['Role'].unique(),
#                             default = data['Role'].unique())
#     
#     # Player_filter = st.selectbox(label = 'Player',
#                                   # options = data['Player'].drop_duplicates().sort_values())



# In[ ]:
    


data_slice = data

# data_slice = data.query('Role == @Role_filter & Club == @Club_filter & Squad == @Squad_filter') # & Player == @Player_filter')

# total1, total2, total3,total4,total5 = st.columns(5,gap='large')




# In[ ]:


def splitByOwner(data, measure, data_type = float):

    data = data.groupby(['Owner'], as_index = False)[measure].sum()

    x = {}

    for owner in data['Owner'].drop_duplicates():
        x[owner] = data[data['Owner'] == owner][measure].astype(data_type)
    
    return x

gain_loss_standings = splitByOwner(data_slice, 'Current Gain/Loss', int)
del gain_loss_standings['Free Agent']

# data_c, data_n, data_s, data_m, data_f, data_d = st.columns(6)
# Row A

a1, a2, a3, a4, a5, a6 = st.columns(6)

a1.metric('Carle', f"{gain_loss_standings['Carle'].item()}")
a2.metric('Damian', f"{gain_loss_standings['Damian'].item()}")
a3.metric('Fracca', f"{gain_loss_standings['Fracca'].item()}")
a4.metric('Marce', f"{gain_loss_standings['Marce'].item()}")
a5.metric('Nippon', f"{gain_loss_standings['Nippon'].item()}")
a6.metric('Scap', f"{gain_loss_standings['Scap'].item()}")

# with data_c:
    # st.image('images/impression.png',use_column_width='Auto')
#     st.metric(label = 'Carle', value = data_c)




# In[ ]:


data_1 = data_slice.sort_values('Current Quote', ascending = False).head(10)
# print(data_bar.head())
# fig = px.bar(data_bar, x = 'Player', y = 'Goals Scored')
# fig.show()
# st.bar_chart(data_1,
#              x = 'Player',
#              y = 'Current Quote'
             # color = "#FF0000"
             # sort = None,
             # use_container_width = False
#              ) 

def altairBarPlotFlipped(data, x_axis, y_axis, color_axis, chart_title):

    source = data

    base = alt.Chart(source).encode(
        y = alt.Y(
            y_axis, 
            scale = alt.Scale(reverse = False), 
            sort = alt.EncodingSortField(field = 'Current Quote', order = 'descending'),
            axis = alt.Axis(title = None),
            ),
        x = alt.X(
            x_axis,
            axis = alt.Axis(title = None, labels = False),
            # axis = alt.Axis(labels = False)),
            ),
        # color = color_axis
    )
    
    bars = base.mark_bar().encode(
        color = color_axis,
    ).properties(
        title = chart_title,
        # width = 300, 
        # height = 200
    )

    text = bars.mark_text(
        align = 'center',
        baseline = 'middle',
        color = 'white',
        dx = 12,
    ).encode(
        text = x_axis,
    )

    return (bars + text).interactive()


top10_quotes_chart = altairBarPlotFlipped(data_1, 'Current Quote', 'Player', 'Role', 'Top 10 Current Quotes')
st.altair_chart(top10_quotes_chart, use_container_width = True, theme = 'streamlit')



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




