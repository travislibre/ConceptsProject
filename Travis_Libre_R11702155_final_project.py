# Project 1, for Prof. Rees's CS 3361 Fall 2022 TTU Course
# Written by Travis Libre, 11/27/2022
# Program Description:
# Takes an input file which is split into packages of data to be multiprocessed
# Outputs a .dat file consisting of the input matrix after 100 iterations of the rowCheck function
import argparse
from multiprocessing import Pool
import time

def main():
    # Parse arguments
    argumentParse = argparse.ArgumentParser(prog='Concepts Project', description =
    'Fulfills final project requirements via multithreading')
    argumentParse.add_argument('-i', "--inputFile", required=True)
    argumentParse.add_argument('-o', "--outputFile", required=True)
    argumentParse.add_argument('-t', "--threadCount", type=int, default=1, required=False)
    commandLineArgs = argumentParse.parse_args()
    array = []
    input_file = open(commandLineArgs.inputFile, 'r')
    threads = commandLineArgs.threadCount
    # Catches thread<=0 error
    if threads < 1:
        raise Exception("Threads cannot be zero or negative")
    processPool = Pool(processes=threads)
    poolData = list()
    # Removes the \n in every line and appends to array
    for (line) in input_file:
        line = line[:-1]
        array.append(list(line))
    # Accounts for empty line in test files
    height = len(array) - 1
    width = len(array[0])
    print(height, width)
    count = 100
    # Package the data into 3 lines
    # The function defined later in the program only calculates the output for the middle line!
    for rowIndex in range(height):
        subArray = list()
        subArray.append(array[(rowIndex-1)%height])
        subArray.append(array[(rowIndex)])
        subArray.append(array[(rowIndex + 1) % height])
        # Append package to poolData
        poolData.append(subArray)
    while count != 0:
        # Store rowCheck result to nextArray
        nextArray = processPool.map(rowCheck , poolData)
        for i in range(height):
            # Update poolData
            poolData[i][0] = nextArray[(i - 1)%height]
            poolData[i][1] = nextArray[i]
            poolData[i][2] = nextArray[(i + 1) % height]
        count = count-1
    # Write to output
    output_file = open(commandLineArgs.outputFile, 'w')
    for i in range(height):
        for j in range(width):
            output_file.write(nextArray[i][j])
        output_file.write('\n')

# rowCheck: takes input, a 2D array of three lines, and returns the middle line with corrected values.
# rowCheck assumes vertical wraparound has already been accounted for
def rowCheck(array):
    i=1
    width = len(array[0])
    # Array to return
    nextArray=[None]*width
    for j in range(width):
        neighbor_sum = 0
        up = (i - 1)
        down = (i + 1)
        left = (j - 1) % width
        right = (j + 1) % width
        if array[up][left] == '+':
            neighbor_sum += 1
        if array[up][j] == '+':
            neighbor_sum += 1
        if array[up][right] == '+':
            neighbor_sum += 1
        if array[i][left] == '+':
            neighbor_sum += 1
        if array[i][right] == '+':
            neighbor_sum += 1
        if array[down][left] == '+':
            neighbor_sum += 1
        if array[down][j] == '+':
            neighbor_sum += 1
        if array[down][right] == '+':
            neighbor_sum += 1
        if array[i][j] == '+':
            if neighbor_sum == 0 or (neighbor_sum % 2) == 1 or neighbor_sum == 8:
                nextArray[j] = '-'
            else:
                nextArray[j] = '+'
        elif array[i][j] == '-' and (neighbor_sum == 2 or neighbor_sum == 3 or neighbor_sum == 5 or neighbor_sum == 7):
            nextArray[j] = '+'
        else:
            nextArray[j] = '-'
    return nextArray

if __name__ == "__main__":
    print("Project :: R11702155")
    main()
