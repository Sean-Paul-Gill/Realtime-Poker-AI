"""
This script is listing all of the best starting hands for a given number of players
 - This will be useful for constructing ranges as percentage of hands
"""

import eval7
import numpy as np
import pandas as pd

# Cards for range appending
all_combos = ['AA', 'AKo', 'AQo', 'AJo', 'ATo', 'A9o', 'A8o', 'A7o', 'A6o', 'A5o', 'A4o', 'A3o', 'A2o',
              'AKs', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s',
              'KK', 'KQo', 'KJo', 'KTo', 'K9o', 'K8o', 'K7o', 'K6o', 'K5o', 'K4o', 'K3o', 'K2o',
              'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s',
              'QQ', 'QJo', 'QTo', 'Q9o', 'Q8o', 'Q7o', 'Q6o', 'Q5o', 'Q4o', 'Q3o', 'Q2o',
              'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s',
              'JJ', 'JTo', 'J9o', 'J8o', 'J7o', 'J6o', 'J5o', 'J4o', 'J3o', 'J2o',
              'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s',
              'TT', 'T9o', 'T8o', 'T7o', 'T6o', 'T5o', 'T4o', 'T3o', 'T2o',
              'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s',
              '99', '98o', '97o', '96o', '95o', '94o', '93o', '92o',
              '98s', '97s', '96s', '95s', '94s', '93s', '92s',
              '88', '87o', '86o', '85o', '84o', '83o', '82o',
              '87s', '86s', '85s', '84s', '83s', '82s',
              '77', '76o', '75o', '74o', '73o', '72o',
              '76s', '75s', '74s', '73s', '72s',
              '66', '65o', '64o', '63o', '62o',
              '65s', '64s', '63s', '62s',
              '55', '54o', '53o', '52o',
              '54s', '53s', '52s',
              '44', '43o', '42o',
              '43s', '42s',
              '33', '32o',
              '32s',
              '22']

# Making a Hand-range Class for each hand combination
all_class_combos = []
for current_combo in all_combos:
     all_class_combos.append(eval7.HandRange(current_combo))

# Declaring Dataframe to store hand-strength
holecard_equity = pd.DataFrame(columns=['hole_cards', 'average_equity'])

# Testing all the combinations
board = []
hero_index = 0
for test_hand in all_class_combos:
    # Declaring Data-Frame to store equity for current hand
    test_hand_df = pd.DataFrame(columns=['hero', 'villain', 'equity'])
    hero_cards = all_combos[hero_index]
    villain_index = 0
    for villain_hand in all_class_combos:
        villain_cards = all_combos[villain_index]
        equity_map = eval7.py_all_hands_vs_range(test_hand, villain_hand, board, 800000)
        average_equity = np.average(list(equity_map.values()))

        # Appending necessary info to Dataframe
        print(hero_cards+" vs "+villain_cards+" : "+str(average_equity))
        test_hand_df.loc[villain_index, 'hero'] = hero_cards
        test_hand_df.loc[villain_index, 'villain'] = villain_cards
        test_hand_df.loc[villain_index, 'equity'] = average_equity

        # Adding counters
        villain_index = villain_index +1

    # Exporting current Hands
    holecard_equity.loc[hero_index, 'hole_cards'] = hero_cards
    holecard_equity.loc[hero_index, 'average_equity'] = test_hand_df['equity'].mean()
    test_hand_df.to_csv(hero_cards+'_vs_unknown1.csv')
    hero_index = hero_index+1

#Exporting the final csv
holecard_equity.to_csv('holecard_equity_unknown1.csv')