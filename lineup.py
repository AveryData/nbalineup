# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:42:49 2022

@author: avery
"""

# Libraries 
from nba_api.stats.endpoints import teamdashlineups
import pandas as pd

# get_teams returns a list of 30 dictionaries, each an NBA team.
from nba_api.stats.static import teams
nba_teams = teams.get_teams()

# Create a dictionary that maps team name to team id
team_dict = {}
for i in nba_teams:
    team_name = i['full_name']
    team_id = i['id']
    team_dict[team_name]= team_id
    

# Function to get the lineups given a team id for the 2021-22 season
def get_lineups(team_id_i):

    lineup = teamdashlineups.TeamDashLineups(
      date_from_nullable = "",
      date_to_nullable = "",
      game_id_nullable = "",
      game_segment_nullable = "",
      group_quantity = 5,
      last_n_games = 0,
      league_id_nullable = "00",
      location_nullable = "",
      measure_type_detailed_defense = "Base",
      month = 0,
      opponent_team_id = 0,
      outcome_nullable = "",
      pace_adjust = "N",
      plus_minus = "N",
      po_round_nullable = "",
      per_mode_detailed = "Totals",
      period = 0,
      rank = "N",
      season = "2021-22",
      season_segment_nullable = "",
      season_type_all_star = "Regular Season",
      shot_clock_range_nullable = "",
      team_id = team_id_i,
      vs_conference_nullable = "",
      vs_division_nullable = ""
      )
    
    df = lineup.get_data_frames() # get the data 
    all_lineups = df[1] # grab all possible lineups
    
    return all_lineups 


# Important loop that gets all league lineups
league_lineup = pd.DataFrame()
for i in team_dict:
    team_id_i = team_dict[i]
    team_lineup = get_lineups(team_id_i)
    team_lineup['team'] = i # adding team name column
    team_lineup['team_id'] = team_id_i  # adding team id column
    league_lineup = league_lineup.append(team_lineup)

league_lineup['players_list'] = league_lineup['GROUP_NAME'].str.split(' - ')
league_lineup = league_lineup.sort_values(by='team')
league_lineup.to_csv('NBALineup2021.csv')
