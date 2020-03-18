import matplotlib.pyplot as plt
from numpy import zeros, array, flip
from pandas import read_csv

# Your standard range_chart setup to be imported
range_chart = array([['AA','AKo','AQo','AJo','ATo','A9o','A8o','A7o' ,'A6o', 'A5o' ,'A4o', 'A3o', 'A2o'],
                     ['AKs','KK','KQo','KJo','KTo','K9o','K8o','K7o' ,'K6o', 'K5o' ,'K4o', 'K3o', 'K2o'],
                     ['AQs','KQs','QQ','QJo','QTo','Q9o','Q8o','Q7o' ,'Q6o', 'Q5o' ,'Q4o', 'Q3o', 'Q2o'],
                     ['AJs','KJs','QJs','JJ','JTo','J9o','J8o','J7o' ,'J6o', 'J5o' ,'J4o', 'J3o', 'J2o'],
                     ['ATs','KTs','QTs','JTs','TT','T9o', 'T8o', 'T7o' ,'T6o', 'T5o' ,'T4o', 'T3o', 'T2o'],
                     ['A9s','K9s','Q9s','J9s','T9s','99','98o' ,'97o' ,'96o' ,'95o' ,'94o' ,'93o', '92o'],
                     ['A8s','K8s','Q8s','J8s','T8s','98s','88' ,'87o' ,'86o' ,'85o' ,'84o' ,'83o', '82o'],
                     ['A7s','K7s','Q7s','J7s','T7s','97s','87s', '77' ,'76o' ,'75o' ,'74o' ,'73o', '72o'],
                     ['A6s','K6s','Q6s','J6s','T6s','96s','86s', '76s' ,'66' ,'65o' ,'64o' ,'63o', '62o'],
                     ['A5s','K5s','Q5s','J5s','T5s','95s','85s', '75s' ,'65s' ,'55' ,'54o' ,'53o', '52o'],
                     ['A4s','K4s','Q4s','J4s','T4s','94s','84s', '74s' ,'64s' ,'54s', '44' ,'43o', '42o'],
                     ['A3s','K3s','Q3s','J3s','T3s','93s','83s', '73s' ,'63s' ,'53s', '43s', '33', '32o'],
                     ['A2s','K2s','Q2s','J2s','T2s','92s','82s', '72s', '62s' ,'52s', '42s', '32s', '22']])

def gradient_compute(card_equity, title, range_chart=range_chart):
    # Iterating through to find probability distribution
    range_pdensity = zeros((13, 13))
    for row in range(13):
        for col in range(13):
            range_pdensity[row, col] = (
            card_equity.loc[card_equity['hole_cards'] == range_chart[row, col], 'average_equity'])

    # Setting Figure Size
    fig, ax = plt.subplots(figsize=(12.8, 9.6))

    # Flipping data to have gradient table correct
    range_pdensity, range_chart = flip(range_pdensity, 0), flip(range_chart, 0)
    # Using the pcolor with no need to normalize the data
    c = ax.pcolor(range_pdensity, edgecolors='black', cmap='RdYlGn')
    # Overlaying text
    for row in range(13):
        for col in range(13):
            plt.text(0.1 + row, 0.3 + col, range_chart[col][row], fontsize=20)
    ax.set_title(title, fontdict={'fontsize': 20, 'fontweight': 'medium'})
    fig.colorbar(c, ax=ax)
    plt.show()

# Running Tests......
# Average equity vs one unknown player's holecards
card_equity_unknown1 = read_csv('datasets/holecard_equity_unknown1.csv', sep=',', header=0, index_col=0)
gradient_compute(card_equity_unknown1, title="Average Equity VS 1 Unknown Player")

# Equity of specific hand vs unknown players holecards
ace_five_suited = read_csv("unknown1/A5s_vs_unknown1.csv")
ace_five_suited.columns = ['index', 'hero', 'hole_cards', 'average_equity']
gradient_compute(ace_five_suited, title="Average Equity of A5s Vs 1 Unknown Player")

# Average equity vs two unknown player's holecards
card_equity_unknown2 = read_csv('datasets/holecard_equity_unknown2.csv', sep=',', header=0)
gradient_compute(card_equity_unknown2, title="Average Equity VS 2 Unknown Players")

# Average equity vs 3 unknown player's holecards
card_equity_unknown3 = read_csv('datasets/holecard_equity_unknown3.csv', sep=',', header=0)
gradient_compute(card_equity_unknown3, title="Average Equity VS 3 Unknown Players")