"""
clean_data_collection: This is a tidied version of poker_realtime_data_colllection.py
"""
from functions.data_collection_functions import number_of_players, first_to_act, round_initialize, position_rearranger
import pandas as pd
import numpy as np
from jellyfish import soundex
from functions.speech_functions import speech_to_text
from datasets.data_dictionary import fold_p, call_p, raise_p, cards, offsuit_or_suited

# Number of players
num_players = number_of_players()

# Name of players
players_names, phonetic_names = ['Alpha', 'Beta', 'Charlie'], []
for name in players_names:
    phonetic_names.append(soundex(name))

# Tournament structure
small_blind, starting_stack = 1, 200

# Importing the gameplay state template and appending structure
gameplay_state = pd.read_csv('../datasets/gameplay_template.csv', header=0)
for index in range(num_players):
    gameplay_state.loc[index, 'STACK'] = starting_stack
    gameplay_state.loc[index, 'N_BB'] = starting_stack / (small_blind*2)

# Dealing for button and requesting who is first to act
players_names = first_to_act(players_names, phonetic_names)

# Starting the first round
for round in range(1,3):
    # This is the big-blind
    current_bet = small_blind*2

    # Initializing gameplay state
    players_cards = []
    for player_name in range(num_players):
        if round > 1:
            gameplay_state.loc[player_name + (num_players*(round-1)), 'STACK'] = gameplay_state.loc[player_name + (num_players*(round-2)), 'STACK'] - gameplay_state.loc[player_name + (num_players * (round - 2)), 'IN_PLAY']
            gameplay_state.loc[player_name + (num_players*(round-1)), 'N_BB'] = gameplay_state.loc[player_name + (num_players*(round-1)), 'STACK'] / (current_bet)
        card_one, card_two = cards[np.random.randint(0,13)], cards[np.random.randint(0,13)]
        if card_one == card_two:
            temp_hole_cards = card_one+card_two
        else:
            temp_hole_cards = card_one+card_two+offsuit_or_suited[np.random.randint(0,2)]
        players_cards.append(temp_hole_cards)
    round_initialize(round, num_players, players_names, players_cards, gameplay_state)

    # Collecting the gameplay
    print("\n============= Beginning Round "+str(round)+" =============\n")
    text = ''
    position_index = 0
    betting_streets, street_index = ['BB_', '2BET_', '3BET_', '4BET_', '5BET_', 'PLUSBET_'], 0
    player_states = [True, True, True]
    while (player_states != [False, False, False]):
        # Resetting position index
        #print(player_states, street_index)
        if position_index > num_players - 1:
            position_index = 0
            if (street_index == 0):
                break
            # if ((gameplay_state.loc[round * position_index, betting_streets[street_index]+'CALL'] == np.nan) or (gameplay_state.loc[round * position_index, betting_streets[street_index]+'FOLD'] == np.nan)) and player_states[position_index]:
            #    player_states[position_index] = False
            #    print("All player states")

        if (street_index > 0):
            if (sum(player_states) <= 1):
                player_states[position_index] = False
                position_index = position_index + 1
                continue
            elif (gameplay_state.loc[position_index + (num_players*(round-1)), betting_streets[street_index] + 'RAISE'] >= 2) and (
                    sum(player_states) > 1):
                position_index = position_index + 1
                continue
            elif not (gameplay_state.loc[position_index + (num_players*(round-1)), betting_streets[street_index] + 'CALL'] >= 2) or (
                    gameplay_state.loc[position_index + (num_players*(round-1)), betting_streets[street_index] + 'FOLD'] == np.nan):
                print(players_names[position_index], " still has to act on this street")
            else:
                player_states[position_index] = False
                position_index = position_index + 1
                continue

        print("Action on", players_names[position_index], "... What is the current action?")
        print("Hole Cards:", players_cards[position_index])

        while player_states[position_index]:
            text = speech_to_text()
            if soundex(text) in fold_p:
                gameplay_state.loc[position_index + (num_players*(round-1)), betting_streets[street_index] + 'FOLD'] = 1
                if (street_index == 0):
                    if (gameplay_state.loc[position_index + (num_players*(round-1)), 'POSITION'] == 'SB'):
                        gameplay_state.loc[position_index + (num_players * (round - 1)), 'IN_PLAY'] = small_blind
                    elif (gameplay_state.loc[position_index + (num_players*(round-1)), 'POSITION'] == 'BB'):
                        gameplay_state.loc[position_index + (num_players * (round - 1)), 'IN_PLAY'] = small_blind*2
                    else:
                        print(gameplay_state.loc[position_index + (num_players * (round - 1)), 'IN_PLAY'])
                player_states[position_index] = False
            elif soundex(text) in call_p:
                gameplay_state.loc[position_index + (num_players*(round-1)), betting_streets[street_index] + 'CALL'] = current_bet
                gameplay_state.loc[position_index + (num_players * (round - 1)), 'IN_PLAY'] = current_bet
                break
            elif soundex(text) in raise_p:
                try:
                    current_bet = [int(s) for s in text.split() if s.isdigit()][0]
                    print(current_bet)
                except:
                    current_bet = 2*current_bet
                gameplay_state.loc[position_index + (num_players*(round-1)), betting_streets[street_index + 1] + 'RAISE'] = current_bet
                gameplay_state.loc[position_index + (num_players * (round - 1)), 'IN_PLAY'] = current_bet
                street_index = street_index + 1
                break
            else:
                print("Please announce a valid action..")
        position_index = position_index + 1
        print("Action received and moving onto next player..\n")


    # Moving the dealers button one ahead
    players_names = position_rearranger(players_names)
    gameplay_state = gameplay_state.fillna(0)
