def main():
    INPUT_FILE_NAME = r"\\wsl$\Ubuntu-20.04\home\lauren\code\advent-of-code21\01\input.txt"

    input = readInput(INPUT_FILE_NAME)

    print(countIncreases(input))


def readInput(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def countIncreases(input):
    numIncreases = 0
    prev = input[0]
    timesRan = 0
    for current in input:
        if (current > prev):
            numIncreases += 1
        prev = current
        timesRan += 1

    print(timesRan)

    return numIncreases


if __name__ == "__main__":
    main()