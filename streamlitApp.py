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


st.set_page_config(page_title = 'FantaSbori App',
                   layout = 'wide',
                   # initial_sidebar_state = 'collapsed'
                   )

# st.cache



# header_left, header_mid, header_right = st.columns([1, 2, 1], gap = 'large')



# with header_mid:
    
st.title('FantaSbori App :soccer:')


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
    

# data_slice = data.query('Role == @Role_filter & Club == @Club_filter & Squad == @Squad_filter') # & Player == @Player_filter')

# total1, total2, total3,total4,total5 = st.columns(5,gap='large')



def splitByAttribute(data, attribute, measure, data_type = float):

    data = data.groupby([attribute], as_index = False)[measure].sum()

    x = {}

    for owner in data[attribute].drop_duplicates():
        x[owner] = data[data[attribute] == owner][measure].astype(data_type)
    
    return x


st.header('Current Gain/Loss Standings')

gain_loss_standings = splitByAttribute(data, 'Owner', 'Current Gain/Loss', int)
del gain_loss_standings['Free Agent']

a1, a2, a3, a4, a5, a6 = st.columns(6)

# cols = [a1, a2, a3, a4, a5, a6]

a1.metric('Carle', f"{gain_loss_standings['Carle'].item()}")
a2.metric('Damian', f"{gain_loss_standings['Damian'].item()}")
a3.metric('Fracca', f"{gain_loss_standings['Fracca'].item()}")
a4.metric('Marce', f"{gain_loss_standings['Marce'].item()}")
a5.metric('Nippon', f"{gain_loss_standings['Nippon'].item()}")
a6.metric('Scap', f"{gain_loss_standings['Scap'].item()}")



def altairBarPlotFlipped(data, x_axis, y_axis, color_axis, reverse_scale = False, chart_title = ''):

    source = data

    base = alt.Chart(source).encode(
        y = alt.Y(
            y_axis, 
            scale = alt.Scale(reverse = reverse_scale), 
            sort = alt.EncodingSortField(field = x_axis, order = 'descending'),
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
    # ).properties(
    #     title = chart_title,
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


st.header("Hot Top 10's")

b1, b2, b3 = st.columns(3)

with b1:
    st.subheader('Players by Current Quote')

    top10_quotes = data.sort_values('Current Quote', ascending = False).head(10)
    top10_quotes_chart = altairBarPlotFlipped(top10_quotes, 'Current Quote', 'Player', 'Role')

    st.altair_chart(top10_quotes_chart, use_container_width = True, theme = 'streamlit')

with b2:

    st.subheader('Deals')

    top10_gains = data.sort_values('Current Gain/Loss', ascending = False).head(10)
    top10_gains_chart = altairBarPlotFlipped(top10_gains, 'Current Gain/Loss', 'Player', 'Role')

    st.altair_chart(top10_gains_chart, use_container_width = True, theme = 'streamlit')
  
with b3:

    st.subheader('Most Improved')

    top10_mimp = data
    top10_mimp['Improvement'] = top10_mimp['Current Quote'] - top10_mimp['Initial Quote']

    top10_mimp = top10_mimp.sort_values('Improvement', ascending = False).head(10)
    top10_mimp_chart = altairBarPlotFlipped(top10_mimp, 'Improvement', 'Player', 'Role')

    st.altair_chart(top10_mimp_chart, use_container_width = True, theme = 'streamlit')  