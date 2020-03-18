from pandas import read_csv

def percentage_of_hands(x_percent, n_players):
    """
    This function will take x % as input and return the top x % of poker hands against n players
    :return: str list (containing all hands in that given percentage)
    """
    if n_players == 1:
        equity_df = read_csv('datasets/holecard_equity_unknown1.csv', sep=',', header=0)
    elif n_players == 2:
        equity_df = read_csv('datasets/holecard_equity_unknown2.csv', sep=',', header=0)
    else:
        equity_df = read_csv('datasets/holecard_equity_unknown3.csv', sep=',', header=0)


    hole_cards = equity_df['hole_cards']

    # Testing to make sure that x_percent is a number between
    if (x_percent > 100) or (x_percent < 0):
        raise ValueError("x_percent must a float/integer between 0 and 100!")
    if (type(n_players) != int):
        raise TypeError("n_players must be a integer value!")

    # Finding how many hands correspond to that percentage
    n_toslice = round(len(hole_cards) * (x_percent/100))

    return hole_cards[:n_toslice].to_numpy()


print(percentage_of_hands(10, 2))