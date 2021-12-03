def readInput(fileName):
    with open(fileName) as file:
        lines = []

        data = file.readlines()
        for line in data:
            lines.append(line.split())
        return lines