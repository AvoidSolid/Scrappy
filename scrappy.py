input_string_start = 'Hello and welcome to python scrabble!\nCreate a list with "-U"\nExit with "q"\n'
input_string = f'Add to the list with "-U"\nExit with "q"\n'

# These are the lists that get zipped to create the dictionary that Uses the "letters" as keys and "points" as values
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]


letter_to_points = dict(zip(letters, points))

# player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordnerd": ["EARTH", "EYES", "MACHINE"], 
# "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_words = {}
player_to_points = {}


def player_word(update_dict):
    return player_to_words.update(update_dict)
    

def score_word(word):
    point_total = 0
    word = word.upper()
    for letter in word:
        point_total += letter_to_points[letter]
    return point_total


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

loop = True
while loop:
    if player_to_words == {}:
        userinput = input(input_string_start)
    else:
        userinput = input(input_string)
    if userinput == "q":
        loop = False
    elif userinput == "-U":
        userinput = input('What is the players name?')
        if userinput == "-Q" or userinput == "-q":
            continue
        name = userinput
        words = input("What words did they play?\n").split(", ")
        print(name, words)
        player_to_words.update({name: words})
        print(player_to_words)

  
    # else:
    #     userinput = input(input_string)
    #     if userinput == "q":
    #         loop = False
    #     elif userinput == "-U":
    #         userinput = input('Exit with "q"\nWhat is the players name?')
    #         if userinput == "-Q" or userinput == "-q":
    #             continue
    #         name = userinput
    #         words = input("What words did they play?\n").split(", ")
    #         print(name, words)
    #         player_to_words.update({name: words})
    #         print(player_to_words)
    print()