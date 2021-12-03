import utils

INPUT_FILE_NAME = r"\\wsl$\Ubuntu-20.04\home\lauren\code\advent-of-code21\02\input.txt"

def main():
    input = utils.readInput(INPUT_FILE_NAME)

    resultCoordinates = calculatePosition(input)
    print(resultCoordinates)

    coordinatesMultiplied = resultCoordinates[0] * resultCoordinates[1]
    print(coordinatesMultiplied)


def calculatePosition(input):
    horizontalPos = 0
    depth = 0

    for instruction in input:
        direction = instruction[0]
        value = int(instruction[1])

        if (direction == "forward"):
            horizontalPos += value
        else:
            depth += calculateDepthValue(direction, value)

    return [horizontalPos, depth]


# depth value is positive or negative depending on which direction
def calculateDepthValue(direction, value):
    if (direction == "up"):
        return (value * -1)
    elif (direction == "down"):
        return value

if __name__ == "__main__":
    main()