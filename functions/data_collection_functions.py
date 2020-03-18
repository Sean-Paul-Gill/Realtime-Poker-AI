"""
data_collection_functions: This script includes all of the data_collection functions for the real-time data collection
"""

# Import necessary libraries
from functions.speech_functions import speech_to_text
from jellyfish import soundex

# Phonetic Dictionary for actions
fold_p = ['B430', 'F430', 'F433']
call_p = ['C400', 'C430', 'K460', 'C640']
check_p = ['C200', 'C230', 'C252', 'A220', 'A226']
raise_p = ['R200', 'R230', 'R252', 'R260', 'R233']

def number_of_players():
    print("How many players are playing?")
    while True:
        text = speech_to_text()
        try:
            num_players = int(text)
            if (num_players > 1) and (num_players < 10):
                print("\n============= Initializing game for", num_players, "players =============")
                break
            else:
                print("Players must be between 2 and 9. How many players?")
                continue
        except:
            print("Integer expected. How many players?")
    return num_players

def first_to_act(players_names, phonetic_names):
    input("Please deal for button and when ready..")
    print("Who is first to act?")
    while True:
        text = speech_to_text()
        if soundex(text) in phonetic_names:
            player_first = players_names[phonetic_names.index(soundex(text))]
            print(player_first, "is first to act, denoting positions based on this..")
            break
        else:
            print("That is not a recognized name, who is first to act?")
    starting_player_index = players_names.index(player_first)
    return players_names[starting_player_index:] + players_names[:starting_player_index]

def round_initialize(round, num_players, players_names, players_cards, gameplay_state):
    for index in range(num_players):
        # Appending round number
        gameplay_state.loc[index + (num_players*(round-1)), 'ROUND'] = round

        # Appending names of player
        gameplay_state.loc[index + (num_players*(round-1)), 'PLAYER'] = players_names[index]

        # Appending positions
        if index % num_players == 0:
            gameplay_state.loc[index + (num_players*(round-1)), 'POSITION'] = 'D'
        elif index % (num_players - 1) == 0:
            gameplay_state.loc[index + (num_players*(round-1)), 'POSITION'] = 'BB'
        else:
            gameplay_state.loc[index + (num_players*(round-1)), 'POSITION'] = 'SB'

        # Appending Hole-Cards if Hero
        gameplay_state.loc[index + (num_players*(round-1)), 'HOLE_CARDS'] = players_cards[index]

def position_rearranger(players_names):
    return players_names[1:] + players_names[:1]
