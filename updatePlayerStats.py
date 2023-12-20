#!/usr/bin/env python
# coding: utf-8

# In[28]:


from datetime import datetime

import os

import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup as bs


# In[29]:


source_dir = os.path.join(os.getcwd(), 'data/')
target_dir = os.path.join(os.getcwd(), 'reports/')

print(f'Source directory: {source_dir}')
print(f'Target directory: {target_dir}')


# In[30]:


quotes_url = 'https://www.fantapazz.com/fantacalcio/listone-e-quotazioni'
stats_url = 'https://www.fantapazz.com/fantacalcio/statistiche'

print(f'Quotes source: {quotes_url}')
print(f'Stats source: {stats_url}')


# In[31]:


run_timestamp = datetime.now()
print(f'Run timestamp: {str(run_timestamp)}')


# In[32]:


def getSoup(url):
    
    page = requests.get(url)
    soup = bs(page.text, features = 'lxml')
    
    return soup


# In[33]:


def filterSoup(soup):
    
    items = []

    for row in soup.findAll('tr'):
        cols = row.findAll('td')
        cols = [element.text.strip() for element in cols]

        items.append(cols)
    
    items = [item for item in items if item != []]
    
    return items


# In[34]:


quotes_soup = getSoup(quotes_url)
quotes = filterSoup(quotes_soup)

quotes = pd.DataFrame(quotes, columns = ['Role', 'Player', 'Current Quote', 'Jersey', 'Club'])
quotes = quotes.drop('Jersey', axis = 1)
quotes = quotes.drop_duplicates()

quotes['Current Quote'] = quotes['Current Quote'].astype(int)
quotes = quotes[['Role', 'Player', 'Club', 'Current Quote']]

print(f'Quotes shape: {quotes.shape}')
print('Quotes head:')
print(quotes.head())


# In[35]:


stats_soup = getSoup(stats_url)
stats = filterSoup(stats_soup)

stats = pd.DataFrame(stats, columns = ['Rank', 'Role', 'Player', 'Jersey', 'Club', 
                                       'FM FP', 'MV FP', 'FM GdS', 'MV GdS', 'FM Sud', 'MV Sud',
                                       'Games', 'Yellow Cards', 'Red Cards',
                                       'Assists', 'Goals Scored', 'Penalties Scored', 'Missed Penalties',
                                       'Goals Conceded', 'Penalties Saved', 'All Clean-Sheets'])
stats = stats.drop(['Rank', 'Jersey', 'All Clean-Sheets'], axis = 1)
stats = stats.drop_duplicates()

stats = stats.replace('', np.NaN)
stats[stats.columns[3:]] = stats[stats.columns[3:]].fillna(0)

stats[stats.columns[3:9]] = stats[stats.columns[3:9]].astype(float)
stats[stats.columns[10:]] = stats[stats.columns[10:]].astype(int)

stats = stats.dropna(subset = ['Club'])

print(f'Stats shape: {stats.shape}')
print('Stats head:')
print(stats.head())


# In[37]:


squads = pd.read_csv(source_dir + 'auctions_history.csv', sep = ',')
squads = squads.drop_duplicates()

squads[['Initial Quote', 'Purchase Price']] = squads[['Initial Quote', 'Purchase Price']].astype(int)

print(f'Squads shape: {squads.shape}')
print('Squads head:')
print(squads.head())


# In[38]:


data = quotes.merge(stats, how = 'right', on = ['Role', 'Player', 'Club'])
data = data.merge(squads, how = 'outer', on = ['Role', 'Player', 'Club'])

data['Current Gain/Loss'] = data['Current Quote'] - data['Purchase Price']
data.loc[data['Purchase Price'] == 0, 'Current Gain/Loss'] = 0

data['Role'] = data['Role'].str.replace('P', 'Portiere')                            .str.replace('D', 'Difensore')                            .str.replace('C', 'Centrocampista')                            .str.replace('A', 'Attaccante')

data = data[['Role', 'Player', 'Club', 'Club Name',
             'Squad', 'Owner', 'Purchase Price', 'Initial Quote', 'Current Quote', 'Current Gain/Loss',
             'Games', 'Yellow Cards', 'Red Cards',
             'Assists', 'Goals Scored', 'Penalties Scored', 'Missed Penalties',
             'Goals Conceded', 'Penalties Saved',
             'FM FP', 'MV FP', 'FM GdS', 'MV GdS', 'FM Sud', 'MV Sud']].copy()

print(f'Final data shape: {data.shape}')
print('Final data head:')
print(data.head())


# In[40]:


data.to_csv(target_dir + 'players_db.csv', sep = ',', encoding = 'utf-8', index = False)

# print(f'::set-output name=test_report::{result}')

