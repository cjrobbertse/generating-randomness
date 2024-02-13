from random import randint

MINIMUM_STRING_LENGTH = 100

user_string_final = ''

print('Please provide AI some data to learn...')
print('The current data length is 0, 100 symbols left')

# Get user input until total 1s and 0s are met
while len(user_string_final) < MINIMUM_STRING_LENGTH:
    print('Print a random string containing 0 or 1:')
    # Get user input
    user_input = input()
    filtered_input = ''
    # Add only 1 and 0 characters
    for char in user_input:
        if char == '0' or char == '1':
            filtered_input += char

    user_string_final += filtered_input

    if len(user_string_final) < MINIMUM_STRING_LENGTH:
        print('Current data length is', len(user_string_final), ',', MINIMUM_STRING_LENGTH - len(user_string_final),
              'symbols left')

print('Final data string:')
print(user_string_final)

triad_dict = dict()

for i in range(len(user_string_final) - 3):
    triad = user_string_final[i:i + 3]
    following_value = user_string_final[i + 3]
    # print(triad, following_value)
    if triad not in triad_dict:
        triad_dict[triad] = 0, 0

    if following_value == '0':
        triad_dict[triad] = triad_dict.get(triad)[0] + 1, triad_dict.get(triad)[1]
    else:
        triad_dict[triad] = triad_dict.get(triad)[0], triad_dict.get(triad)[1] + 1

triad_dict = dict(sorted(triad_dict.items()))

print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')

end_game = False
balance = 1000

while not end_game:
    valid_input = False

    filtered_input = ''

    while not valid_input:
        filtered_input = ''
        print('Print a random string containing 0 or 1:')
        user_input = input()
        if user_input == 'enough':
            end_game = True
            break

        for char in user_input:
            if char == '0' or char == '1':
                filtered_input += char

        if len(filtered_input) < 4:
            continue

        valid_input = True

    if end_game:
        break

    predictions = []
    following_values = []

    for i in range(len(filtered_input) - 3):
        triad = filtered_input[i:i + 3]
        following_value = filtered_input[i + 3]
        following_values.append(following_value)

        if triad not in triad_dict:
            triad_dict[triad] = 0, 0

        if triad_dict[triad][0] > triad_dict[triad][1]:
            predictions.append('0')
        elif triad_dict[triad][0] < triad_dict[triad][1]:
            predictions.append('1')
        else:
            predictions.append(str(randint(0, 1)))

    print('predictions:')
    print(''.join(predictions))

    correct_predictions = 0

    for i in range(len(predictions)):
        if predictions[i] == following_values[i]:
            correct_predictions += 1

    accuracy = correct_predictions / len(predictions) * 100

    print(f'Computer guessed {correct_predictions} out of {len(predictions)} symbols ({accuracy:.2f} %)')

    player_score = len(predictions) - correct_predictions
    ai_score = correct_predictions

    balance = balance + player_score
    balance = balance - ai_score

    print(f'Your balance is now ${balance}')

    # train the AI
    for i in range(len(filtered_input) - 3):
        triad = filtered_input[i:i + 3]
        following_value = filtered_input[i + 3]

        if following_value == '0':
            triad_dict[triad] = triad_dict.get(triad)[0] + 1, triad_dict.get(triad)[1]
        else:
            triad_dict[triad] = triad_dict.get(triad)[0], triad_dict.get(triad)[1] + 1


print('Game over!')