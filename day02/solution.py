""" --- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2"""

import sys
import re

LIMIT = [12,13,14] # red, green, blue

def get_data(filename):
    """
    Read and return the content of a file.

    Parameters:
    filename (str): The path to the file to be read.

    Returns:
    str: The entire content of the file as a string.
    """
    with open(filename, "r") as file:
        data = file.read()
        return data

def read_data(input_data):
    """
    Split the input data into a list of lines.

    Parameters:
    input_data (str): A string containing the data to be split into lines.

    Returns:
    list: A list of strings, where each string is a line from the input data.
    """
    return [line for line in input_data.split("\n") if line]

def count_colour(colour, game):
    """
    Counts max cubes of given colour inside one game.

    Parameters:
    colour (str): A colour of the cubes number of which we should know,
    game (str): A game output (all reveals).

    Returns:
    int: Max of cubes of given colour that were revealed in the game.
    """
    rgx = rf"(\d+) {colour}"
    rgx_res = (re.findall(rgx, game))
    if len(rgx_res) > 0:
        return max([int(s) for s in rgx_res])

def get_answer(input_data):
    """
    Calculate the answers for AoC tasks.

    Parameters:
    input_data (str): Multiline string data to be processed.

    Returns:
    tuple: A tuple of two elements, each an integer representing the answer in
           each of the two parts og the daily AoC Task.
    """
    data = read_data(input_data)
    possible_games = []
    limit = LIMIT
    # play game 1
    for game in data:
        num_re = r"Game (\d+):"
        game_n = int(re.findall(num_re, game)[0])
        rn = count_colour('red', game)
        gn = count_colour('green', game)
        bn = count_colour('blue', game)
        if rn <= limit[0] and gn <= limit[1] and bn <= limit[2]:
            possible_games.append(game_n)
    answer1 = sum(possible_games)
    # play game 2
    game_powers = []
    for game in data:
        rn = count_colour('red', game)
        gn = count_colour('green', game)
        bn = count_colour('blue', game)
        game_powers.append(rn * gn * bn)
    answer2 = sum(game_powers)
    return answer1, answer2

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1]:
            filename = f"{sys.argv[1]}.txt"
    data = get_data(filename)
    answer = get_answer(data)
    print(f"The answer for the 1st task is: {answer[0]}")
    print(f"The answer for the 2nd task is: {answer[1]}")