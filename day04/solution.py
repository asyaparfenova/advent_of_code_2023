"""THIS IS A DRAFT FOR DAY04"""

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
    data = [line for line in input_data.split("\n") if line]
    mtrx = np.array([list(a) for a in data]) #.astype(int) - in case we want matrix
    return mtrx

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
    return data, 0

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1]:
            filename = f"{sys.argv[1]}.txt"
    data = get_data(filename)
    answer = get_answer(data)
    print(f"The answer for the 1st task is: {answer[0]}")
    print(f"The answer for the 2nd task is: {answer[1]}")