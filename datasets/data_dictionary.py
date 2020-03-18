# Phoenetic Dictionary for actions
fold_p = ['B430', 'F430', 'F433']
call_p = ['C400', 'C430', 'K460', 'C640']
check_p = ['C200', 'C230', 'C252', 'A220', 'A226']
raise_p = ['R200', 'R230', 'R252', 'R260', 'R233']

# Cards to randomly append
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
offsuit_or_suited = ['o', 's']

# Uncomment below if you want to train for phoenetic words
"""temp, phoenetic = [], []
while True:
    print("Please enter an option")
    text = speech_to_text()
    if text == 'break':
        break
    temp.append(text)
    phoenetic.append(soundex(text))"""

