import utils

INPUT_FILE_NAME = r"\\wsl$\Ubuntu-20.04\home\lauren\code\advent-of-code21\03\input.txt"

def main():
    input = utils.readInput(INPUT_FILE_NAME)

    gammaEpsilonRates = findGammaEpsilonRates(input)
    print("Gamma " + str(gammaEpsilonRates[0]) + "\n")
    print("Epsilon " + str(gammaEpsilonRates[1]) + "\n")

    powerConsumption = getPowerConsumption(gammaEpsilonRates[0], gammaEpsilonRates[1])
    print(str(powerConsumption))


def findGammaEpsilonRates(input):
    mostCommonBitInColumns = findMostCommonBitInColumns(input)
    gamma = getDecimalGammaRate(mostCommonBitInColumns)
    epsilon = getDecimalEpsilonRate(mostCommonBitInColumns)

    return [gamma, epsilon]


def findMostCommonBitInColumns(input):
    mostCommonBitInColumns = [None] * 12
    numOnesInColumns = dict.fromkeys(range(12), 0)

    for line in input:
        for i in range(len(line)):
            c = int(line[i])
            if (c == 1):
                numOnesInColumns[i] += 1

    for i in numOnesInColumns.keys():
        if (numOnesInColumns[i] > 500):
            mostCommonBitInColumns[i] = 1
        else:
            mostCommonBitInColumns[i] = 0

    return mostCommonBitInColumns


def getDecimalGammaRate(mostCommonBitInColumn):
    gamma = ""

    for column in mostCommonBitInColumn:
        gamma += str(column)

    gamma = utils.binaryToDecimal(gamma)
    return gamma


def getDecimalEpsilonRate(mostCommonBitInColumn):
    gamma = None

    gamma = ""

    for column in mostCommonBitInColumn:
        if (column == 1):
            gamma += str("0")
        else:
            gamma += str("1")

    gamma = utils.binaryToDecimal(gamma)

    return gamma


def getPowerConsumption(gamma, epsilon):
    return gamma * epsilon


if __name__ == "__main__":
    main()