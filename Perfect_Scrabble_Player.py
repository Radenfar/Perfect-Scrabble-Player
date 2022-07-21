from displayboard import board as Board
from itertools import chain, combinations

#initialises a list of all the possible scrabble words to make.
all_words = []
f = open("new_scrabble_words.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line[:-1]
    all_words.append(line)
f.close()

def make_scrabble_board():
    board = Board(15, 15, "*")
    triple_words = [(1, 1), (8, 1), (15, 1), (1, 8), (15, 8), (1, 15), (8, 15), (15, 15)]
    double_words = [(2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (5, 5), (11, 5), (5, 11), (11, 11), (4, 12), (12, 12), (3, 13), (13, 13), (2, 14), (14, 14)]
    triple_letters = [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
    double_letters = [(4, 1), (12, 1), (7, 3), (9, 3), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 8), (12, 8), (3, 9), (7, 9), (9, 9), (13, 9), (1, 12), (8, 12), (15, 12), (7, 13), (9, 13), (4, 15), (12, 15)]
    for tw in triple_words:
        cur_x = tw[0]
        cur_y = tw[1]
        board.fill(cur_x, cur_y, 'O')
    for dw in double_words:
        cur_x = dw[0]
        cur_y = dw[1]
        board.fill(cur_x, cur_y, 'P')
    for tl in triple_letters:
        cur_x = tl[0]
        cur_y = tl[1]
        board.fill(cur_x, cur_y, 'B')
    for dl in double_letters:
        cur_x = dl[0]
        cur_y = dl[1]
        board.fill(cur_x, cur_y, 'C')
    board.fill(8, 8, "@")
    return board

def is_valid(word, all_words):
    return (word in all_words)

def is_connected(board, word, root, direction):
    word_len = len(word)
    next_plots = []
    x = root[0]
    y = root[1]
    y_check = root[1]
    x_check = root[1]
    next_plots.append(board.at_coord(x, y))
    for char in word:
        if direction == 'down':
            x -= 1
            y_check -= 1
            if y_check == -1:
                return False
                break
            next_plots.append(board.at_coord(x, y))
        elif direction == 'right':
            y += 1
            x_check += 1
            if x_check > 16:
                return False
                break
            next_plots.append(board.at_coord(x, y))
    next_plots.pop()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in alphabet:
        if char in next_plots:
            return True
    return False

def add_word(board, word, root, direction):
    x = root[0]
    y = root[1]
    board.fill(x, y, word[0])
    word = word[1:]
    for char in word:
        if direction == 'down':
            x -= 1
            board.fill(x, y, char)
        elif direction == 'right':
            y += 1
            board.fill(x, y, char)

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def all_letters_used(board):
    all_coord_tuples = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15)]
    chars = []
    for coord in all_coord_tuples:
        cur_char = board.at_coord(coord[0], coord[1])
        if cur_char == 'O':
            pass
        elif cur_char == 'P':
            pass
        elif cur_char == 'B':
            pass
        elif cur_char == '@':
            pass
        elif cur_char == 'C':
            pass
        elif cur_char == '*':
            pass
        else:
            if cur_char not in chars:
                chars.append(cur_char)
    return chars
    
def find_word(board, all_words):
    in_hand = []
    print("How many letters do you have in hand?")
    let_num = int(input("-: "))
    for num in range(let_num):
        in_hand.append(input("Enter letter -: "))
    print("Current hand:")
    print(in_hand)
    hand_from_board = all_letters_used(board)
    for char in hand_from_board:
        if char not in in_hand:
            in_hand.append(char)
    combinations = list(map(''.join, powerset(in_hand)))[1:]
    for string in combinations:
        reverse = string[::-1]
        if reverse in combinations:
            pass
        else:
            combinations.append(reverse)
    options = []
    for string in combinations:
        if string in all_words:
            options.append(string)
    options.sort(key = len, reverse = True)
    print("Here are all of your options:")
    down_options_dict = {}
    right_options_dict = {}
    all_coord_tuples = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15)]
    #HERE LOOP FOR X,Y so that it covers the entire board to check every tile
    max_down_coords = 'Null'
    max_right_coords = 'Null'
    for option in options:
        down_options_dict[option] = get_score(board, option, (1, 1), 'down')
        right_options_dict[option] = get_score(board, option, (1, 1), 'down')
        for coord_tuple in all_coord_tuples:
            new_down_score = get_score(board, option, coord_tuple, 'down')
            new_right_score = get_score(board, option, coord_tuple, 'right')
            if new_down_score > down_options_dict[option] and is_connected(board, option, coord_tuple, 'down') == True:
                down_options_dict[option] = new_down_score
                max_down_coords = coord_tuple
            if new_right_score > right_options_dict[option] and is_connected(board, option, coord_tuple, 'right') == True:
                right_options_dict[option] = new_right_score
                max_right_coords = coord_tuple
    down_options_dict = {k: v for k, v in down_options_dict.items() if v is not False}
    right_options_dict = {k: v for k, v in right_options_dict.items() if v is not False}
    print("Down:")
    sorted_down_dict = sorted(down_options_dict.items(), key=lambda x: int(x[1]), reverse = True)
    print(sorted_down_dict)
    print("Root of max: ", max_down_coords)
    print("Right:")
    sorted_right_dict = sorted(right_options_dict.items(), key=lambda x: int(x[1]), reverse = True)
    print(sorted_right_dict)
    print("Root of max: ", max_right_coords)

def get_score(board, word, root, direction):
    letter_value = {'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}
    word_len = len(word)
    next_plots = []
    x = root[0]
    y = root[1]
    y_check = root[1]
    x_check = root[1]
    next_plots.append(board.at_coord(x, y))
    for char in word:
        if direction == 'down':
            x -= 1
            y_check -= 1
            if y_check == -1:
                return False
                break
            next_plots.append(board.at_coord(x, y))
        elif direction == 'right':
            y += 1
            x_check += 1
            if x_check > 16:
                return False
                break
            next_plots.append(board.at_coord(x, y))
    next_plots.pop()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(next_plots)):
        if next_plots[i] in alphabet:
            if word[i] == next_plots[i]:
                pass
            else:
                return False
                break
    score = 0
    double = False
    triple = False
    for x in range(len(word)):
        if next_plots[x] == 'C':
            cur_value = letter_value[word[x]]
            cur_value *= 2
            score += cur_value
        elif next_plots[x] == 'B':
            cur_value = letter_value[word[x]]
            cur_value *= 3
            score += cur_value
        elif next_plots[x] == 'P':
            score += letter_value[word[x]]
            double = True
        elif next_plots[x] == 'O':
            score += letter_value[word[x]]
            triple = True
        else:
            score += letter_value[word[x]]
    if double == True:
        score *= 2
    if triple == True:
        score *= 3
    return score

def get_letter_value(letter):
    letter_value = {'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}
    keys_list = list(letter_value.keys())
    if letter not in keys_list:
        return ("Letter not valid!")
    else:
        return letter_value[letter]

def starting_turn(board):
    in_hand = []
    print("How many letters do you have in hand?")
    let_num = int(input("-: "))
    for num in range(let_num):
        in_hand.append(input("Enter letter -: "))
    combinations = list(map(''.join, powerset(in_hand)))[1:]
    for string in combinations:
        reverse = string[::-1]
        if reverse in combinations:
            pass
        else:
            combinations.append(reverse)
    options = []
    for string in combinations:
        if string in all_words:
            options.append(string)
    options.sort(key = len, reverse = True)
    print(options)

board = make_scrabble_board()
while True:
    print("-"*50)
    print(board)
    print("-"*50)
    print("Either:")
    print("1 - Add word onto board")
    print("2 - Find word on existing board (perfect play finder)")
    print("3 - Check if a word is a valid word or not")
    print("4 - Get what score a word would be")
    print("5 - Get the value of a letter")
    print("6 - Create a starting word")
    ui = input("-: ")
    if ui == '1':
        print("Type the word you would like to add: ")
        new_word = input("-: ")
        print("Root coords:")
        new_y = int(input("x = "))
        new_x = int(input("y = "))
        new_coords = (new_x, new_y)
        print("Is it going 'down' or 'right'?")
        new_direction = input("-: ")
        if 'd' in new_direction:
            new_direction = 'down'
        else:
            new_direction = 'right'
        add_word(board, new_word, new_coords, new_direction)
    elif ui == '2':
        find_word(board, all_words)
    elif ui == '3':
        print("Enter the word you would like to challenge")
        word_to_test = input("-: ").lower()
        challenge = (is_valid(word_to_test, all_words))
        print("-"*50)
        if challenge == True:
            print(word_to_test + " is a valid scrabble word.")
        else:
            print(word_to_test + " is not a valid scrabble word.")
    elif ui == '4':
        print("Type the word you would like to check: ")
        new_word = input("-: ")
        print("Root coords:")
        new_y = int(input("x = "))
        new_x = int(input("y = "))
        new_coords = (new_x, new_y)
        print("Is it going 'down' or 'right'?")
        new_direction = input("-: ")
        if 'd' in new_direction:
            new_direction = 'down'
        else:
            new_direction = 'right'
        print("-"*50)
        print(get_score(board, new_word, new_coords, new_direction))
    elif ui == '5':
        letter = input("What letter's score do you need? -: ").lower()
        value = str(get_letter_value(letter))
        print("-"*50)
        print("The value of " + letter + " is: " + value + ".")
    elif ui == '6':
        starting_turn(board)
    else:
        print("I N V A L I D I N P U T")
