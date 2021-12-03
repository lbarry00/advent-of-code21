import utils

def main():
    input = utils.readInput(utils.INPUT_FILE_NAME)

    print(countIncreases(input))


def countIncreases(input):
    numIncreases = 0
    prev = input[0]
    
    for current in input:
        if (current > prev):
            numIncreases += 1
        prev = current
        timesRan += 1

    return numIncreases


if __name__ == "__main__":
    main()