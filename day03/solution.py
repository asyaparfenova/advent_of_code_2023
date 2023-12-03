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
    mtrx = np.array([list(a) for a in data])
    return mtrx

def check_surroundings(arr, row, start_num, end_num):
    """
    Check the surroundings of a horizontal sequence of elements within a NumPy array whether these surrounding cells
    are all dots ('.'). Additionally, it identifies any cells with stars ('*') in
    the surrounding area.

    Parameters:
    arr (numpy.ndarray): The 2D NumPy array to be checked.
    row (int): The row index of the sequence within the array.
    start_num (int): The starting column index of the sequence.
    end_num (int): The ending column index of the sequence.

    Returns:
    tuple of (bool, list of tuples):
    - A boolean indicating whether the surrounding cells are all dots.
    - A list of tuples - coordinates of a cell containing a star in the surrounding area.
    """
    rows, cols = arr.shape
    surrounded_by_dots = True
    stars = []
    for i in range(row - 1, row + 2):
        for j in range(start_num - 1, end_num + 2):
            if 0 <= i < rows and 0 <= j < cols:
                if i == row and start_num <= j <= end_num:
                    continue
                elif arr[i, j] != '.':
                    if arr[i, j] == '*':
                        stars.append((i, j))
                    surrounded_by_dots = False
    return surrounded_by_dots, stars

def get_answer(input_data):
    """
    Calculate the answers for AoC tasks.

    Parameters:
    input_data (str): Multiline string data to be processed.

    Returns:
    tuple: A tuple of two elements, each an integer representing the answer in
           each of the two parts og the daily AoC Task.
    """
    arr = read_data(input_data)
    rows, cols = arr.shape
    part_numbers = []
    gears = {}

    for i in range(rows):
        for j in range(cols):
            if arr[i, j].isdigit():
                if j == 0 or not arr[i, j - 1].isdigit():
                    num = arr[i, j]
                    k = j + 1
                    while k < cols and arr[i, k].isdigit():
                        num += arr[i, k]
                        k += 1
                    surrounded_by_dots, stars = check_surroundings(arr, i, j, k - 1)
                    if not surrounded_by_dots:
                        part_numbers.append(int(num))
                        for star in stars:
                            if star not in gears.keys():
                                gears[star] = [int(num)]
                            else:
                                gears[star].append(int(num))
        sum_part_numbers = sum(part_numbers)
        sum_gear_ration = 0
        for k in gears.keys():
            if len(gears[k]) == 2:
                sum_gear_ration += gears[k][0]*gears[k][1]
    return sum_part_numbers, sum_gear_ration

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1]:
            filename = f"{sys.argv[1]}.txt"
    data = get_data(filename)
    answer = get_answer(data)
    print(f"The answer for the 1st task is: {answer[0]}")
    print(f"The answer for the 2nd task is: {answer[1]}")