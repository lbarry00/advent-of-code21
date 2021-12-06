def readInput(fileName):
    with open(fileName) as file:
        lines = []

        data = file.readlines()
        for line in data:
            lines.append(line.strip())
        return lines

def binaryToDecimal(n):
    return int(n,2)