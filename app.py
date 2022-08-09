# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:30:07 2022

@author: avery
"""

import pandas as pd
import streamlit as st
import plotly.express as px


# import data
df = pd.read_csv('NBALineup2021.csv')

# Title for app
st.set_page_config(layout="wide")
st.title('NBA Lineup Analysis Tool ')


# User chooses team 
team = st.selectbox(
     'Choose Your Team:',
     df['team'].unique())

# Get just the selected team 
df_team = df[df['team'] == team].reset_index(drop=True)
# Get players on roster
df_team['players_list'] = df_team['players_list'].str.replace(r"[\"\' \[\]]", '').str.split(',')
duplicate_roster = df_team['players_list'].apply(pd.Series).stack()
roster = duplicate_roster.unique()


players = st.multiselect(
     'Select your players',
     roster,
     roster[0:5])


# Find the right line up
df_lineup = df_team[df_team['players_list'].apply(lambda x: set(x)==set(players))]

df_important = df_lineup[['MIN', 'PLUS_MINUS','FG_PCT', 'FG3_PCT']]

st.dataframe(df_important)

col1, col2, col3, col4 = st.columns(4)

with col1: 
    fig_min = px.histogram(df_team, x="MIN")
    fig_min.add_vline(x=df_important['MIN'].values[0],line_color='red')
    st.plotly_chart(fig_min, use_container_width=True)

with col2: 
    fig_2 = px.histogram(df_team, x="PLUS_MINUS")
    fig_2.add_vline(x=df_important['PLUS_MINUS'].values[0],line_color='red')
    st.plotly_chart(fig_2, use_container_width=True)
    
with col3: 
    fig_3 = px.histogram(df_team, x="FG_PCT")
    fig_3.add_vline(x=df_important['FG_PCT'].values[0],line_color='red')
    st.plotly_chart(fig_3, use_container_width=True)
    
with col4: 
    fig_4 = px.histogram(df_team, x="FG3_PCT")
    fig_4.add_vline(x=df_important['FG3_PCT'].values[0],line_color='red')
    st.plotly_chart(fig_4, use_container_width=True)
