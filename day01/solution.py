import sys

NUMBERS = ['one','two','three','four','five','six','seven','eight','nine']

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

def check_number(line, position):
    """
    Check and return the numeric representation of a spelled-out number in a given line.

    Parameters:
    line (str): The string to be searched.
    position (int): The starting index in 'line' from where the search should begin.

    Returns:
    str: The numeric representation (as a string) of the spelled-out number if a match is found,
         otherwise an empty string. If the provided position is out of range or leads to an error,
         an empty string is returned.
    """
    try:
        if line[position:position+3] in NUMBERS:
            return str(NUMBERS.index(line[position:position+3])+1)
        elif line[position:position+4] in NUMBERS:
            return str(NUMBERS.index(line[position:position+4])+1)
        elif line[position:position+5] in NUMBERS:
            return str(NUMBERS.index(line[position:position+5])+1)
        else:
            return ""
    except:
        pass
    return ""

def get_answer(input_data):
    """
    Calculate the answers for AoC tasks.
    If answer1 can not be calculated for test01 data - returns "No Answer Available".

    Parameters:
    input_data (str): Multiline string data to be processed.

    Returns:
    tuple: A tuple of two elements, each an integer representing the sum calculated in
           each of the two cases.
    """
    data = read_data(input_data)
    try:
        answer1 = 0
        for l in data:
            s,f = "",""
            i,j = 0,len(l)
            while s=="":
                if l[i].isdigit():
                    s = (l[i])
                i += 1
            while f=="":
                if l[j-1].isdigit():
                    f = (l[j-1])
                j -= 1
            answer1 += int(s+f)
    except:
        answer1 = "No Answer Available"
    answer2 = 0
    for l in data:
        s,f = "",""
        i,j = 0,len(l)
        while s=="":
            if l[i].isdigit():
                s = (l[i])
            else:
                s = check_number(l, i)
            i += 1
        while f=="":
            if l[j-1].isdigit():
                f = (l[j-1])
            else:
                f = check_number(l, j-1)
            j -= 1
        answer2 += int(s+f)
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