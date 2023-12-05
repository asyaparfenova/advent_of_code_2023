"""THIS IS A DRAFT FOR DAY05"""

import sys
import numpy as np


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
    data = [line for line in input_data.split("\n\n") if line]
    return data

def parse_data(input_data):
    data = read_data(input_data)
    maps = {}
    seeds = [int(i) for i in data[0].split(' ')[1:]]
    for block in data[1:]:
        key = block.split('\n')[0].split(' ')[0].split('-to-')[0]
        val = block.split('\n')[0].split(' ')[0].split('-to-')[1]
        maps[key] = [val,[]]
        for line in block.split('\n')[1:]:
            [dest_n, start_n, rng] = [int(i) for i in line.split(' ')]
            maps[key][1].append([dest_n, start_n, rng])
    #print(maps)
    return seeds, maps

def get_answer(input_data):
    """
    Calculate the answers for AoC tasks.

    Parameters:
    input_data (str): Multiline string data to be processed.

    Returns:
    tuple: A tuple of two elements, each an integer representing the answer in
           each of the two parts og the daily AoC Task.
    """
    seeds, maps = parse_data(input_data)
    #game1
    locations = []
    for seed in seeds:
        key = 'seed'
        val = seed
        while key != 'location':
            add_to_val = 0
            for rng in maps[key][1]:
                if rng[1] <= val <= (rng[1] + rng[2] - 1):
                    add_to_val = rng[0] - rng[1]
            val += add_to_val
            key = maps[key][0]
        locations.append(val)
    answer1 = min(locations)
    # game2
    answer2 = "To be continued..."
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