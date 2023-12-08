import re
from helpers import get_input, get_test_input

maximum_dice = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def parse_game_rounds(lines):

    games = {}

    for line in lines:

        highest = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        lowest = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        game_id = int(re.search(r"^Game (?P<game_id>\d+):", line)[1])

        rounds = [round.strip() for round in line.split(":")[1].strip().split(';')]

        for round in rounds:
            cubes = round.split(', ')

            for cube in cubes:

                count, color = cube.split(' ')

                if int(count) > highest[color]:
                    highest[color] = int(count)

        games[game_id] = highest

    return games


def get_possible_games(games):

    possible_games = []

    for game_id, highest in games.items():

        possible_game = True

        for color, count in highest.items():

            if count > maximum_dice[color]:
                possible_game = False

        if possible_game:
            possible_games.append(game_id)

    return possible_games


def power_of_games(games):

    power_of_games = []

    for game_id, highest in games.items():

        power_of_game = highest.get('blue') * highest.get('green') * highest.get('red')

        power_of_games.append(power_of_game)

    return power_of_games


print(sum(get_possible_games(parse_game_rounds(get_input(2)))))
print(sum(power_of_games(parse_game_rounds(get_input(2)))))