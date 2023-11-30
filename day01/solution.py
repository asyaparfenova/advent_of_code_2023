import sys

def get_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        return data

def read_data(input_data):
    input_lines = input_data.split("\n")
    result = []
    subres = []
    for il in input_lines:
        if il != "":
            subres.append(int(il))
        else:
            result.append(subres)
            subres = []
    result.append(subres)
    return result


def get_answer(input_data):
    data = read_data(input_data)
    return data, False


if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            filename = "test.txt"
    data = get_data(filename)
    answer = get_answer(data)
    print(f"The answer for the 1st task is: {answer[0]}")
    print(f"The answer for the 2nd task is: {answer[1]}")