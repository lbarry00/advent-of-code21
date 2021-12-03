INPUT_FILE_NAME = r"\\wsl$\Ubuntu-20.04\home\lauren\code\advent-of-code21\01\input.txt"

def readInput(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines