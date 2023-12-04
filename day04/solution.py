""" --- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4"""

import sys

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
    numpy.ndarray: 2D NumPy array where each element is a character from the
                   input string.
    """
    lines = [line for line in input_data.split("\n") if line]
    card_lines = [l.split(': ')[1].split(' | ') for l in lines]
    cards = [[[int(s) for s in c.split(' ') if s] for c in cl] for cl in card_lines]
    return cards

def count_wins(card):
    """
    Calculate the winning numbers by finding the intersection of two lists of numbers.

    Parameters:
    cart (list of lists): Multiline string data to be processed.

    Returns:
    int: A number of winning points.
    """
    return len([c for c in card[0] if c in card[1]])

def get_answer(input_data):
    """
    Calculate the answers for AoC tasks.

    Parameters:
    input_data (str): Multiline string data to be processed.

    Returns:
    tuple: A tuple of two elements, each an integer representing the answer in
           each of the two parts og the daily AoC Task.
    """
    cards = read_data(input_data)
    # game 1
    total_points = sum(pow(2, count_wins(card) - 1) for card in cards if count_wins(card) > 0)
    # game 2
    cards_count = [1]*len(cards)
    for i,card in enumerate(cards):
        n = count_wins(card)
        cards_count[i + 1:i + n + 1] = [x + cards_count[i] for x in cards_count[i + 1:i + n + 1]]
    total_cards = sum(cards_count)
    return total_points, total_cards


if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1]:
            filename = f"{sys.argv[1]}.txt"
    data = get_data(filename)
    answer = get_answer(data)
    print(f"The answer for the 1st task is: {answer[0]}")
    print(f"The answer for the 2nd task is: {answer[1]}")