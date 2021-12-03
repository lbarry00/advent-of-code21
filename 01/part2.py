import utils

def main():
    input = utils.readInput(utils.INPUT_FILE_NAME)

    numIncreases = countIncreasesSum(input)
    print("Num increases: " + str(numIncreases))


def countIncreasesSum(input):
    numIncreases = 0
    prevSum = 0
    
    for i in range(len(input[:-3])):
        currentSum = int(input[i]) + int(input[i + 1]) + int(input[i + 2])

        if (currentSum > prevSum):
            numIncreases += 1

        prevSum = currentSum

    return numIncreases


if __name__ == "__main__":
    main()