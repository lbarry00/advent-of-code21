import utils

INPUT_FILE_NAME = r"\\wsl$\Ubuntu-20.04\home\lauren\code\advent-of-code21\02\input.txt"

def main():
    input = utils.readInput(INPUT_FILE_NAME)

    resultCoordinates = calculatePosition(input)
    coordinatesMultiplied = resultCoordinates[0] * resultCoordinates[1]
    print(coordinatesMultiplied)


def calculatePosition(input):
    horizontalPos = 0
    depth = 0
    aim = 0

    for instruction in input:
        direction = instruction[0]
        value = int(instruction[1])

        if (direction == "forward"):
            horizontalPos += value
            depth += (aim * value)
        elif (direction == "up"):
            aim -= value
        elif (direction == "down"):
            aim += value

    return [horizontalPos, depth]


if __name__ == "__main__":
    main()