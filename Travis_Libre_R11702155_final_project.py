# Project 1, for Prof. Rees's CS 3361 Fall 2022 TTU Course
# Written by Travis Libre, 11/27/2022
# Program Description:
# Takes an input file which is split into packages of data to be multiprocessed
# Outputs a .dat file consisting of the input matrix after 100 iterations of the rowCheck function
import argparse
from multiprocessing import Pool

def main():
    # Process Args
    commandLineArgs = takeArgs()
    dataArray = []
    input_file = open(commandLineArgs.inputFile, 'r')
    # Read & Convert file
    readFile(input_file, dataArray)
    height = len(dataArray)
    width = len(dataArray[0])
    poolData = list()
    package(poolData, dataArray, height, width)
    threads = commandLineArgs.threadCount
    # Catches thread<=0 error
    if threads < 1:
        raise Exception("Threads cannot be zero or negative")
    processPool = Pool(processes=threads)
    iterations = 100
    # Repeat 100 times
    for count in range(iterations):
        # Store rowCheck result to nextArray
        nextArray = processPool.map(rowCheck , poolData)
        del poolData
        poolData = list()
        # Restart poolData
        package(poolData, nextArray, height, width)
    # Write to output
    output_file = open(commandLineArgs.outputFile, 'w')
    writeToOutput(output_file, height, width, nextArray)

# Takes file dimensions, output_file, and the array to be printed, prints array to output file
def writeToOutput(output_file, height, width, array):
    for i in range(height):
        for j in range(width):
            num = array[i][j]
            if(num==1):
                output_file.write('+')
            else:
                output_file.write('-')
        output_file.write('\n')

# Reads file, converts to digits
# Takes input_file and output matrix
def readFile(input_file, output):
    # Removes the \n in every line and appends to dataArray
    for line in input_file:
        line = list(line.strip('\n'))
        # Converts to ints for faster computation
        for x in range(len(line)):
            if(line[x]=='-'):
                line[x] = 0
            elif(line[x]=='+'):
                line[x] = 1
            else:
                print("Invalid Character Detected")
        # Accounts for empty line in test files
        if(len(line)!=0):
            output.append(line)
# Parse arguments
# Takes no arguments, returns argument parse object
def takeArgs():
    argumentParse = argparse.ArgumentParser(prog='Concepts Project', description=
    'Fulfills final project requirements via multithreading')
    argumentParse.add_argument('-i', "--inputFile", required=True)
    argumentParse.add_argument('-o', "--outputFile", required=True)
    argumentParse.add_argument('-t', "--threadCount", type=int, default=1, required=False)
    commandLineArgs = argumentParse.parse_args()
    return commandLineArgs

# Package the middle row, it's immediate wrapping neighbors, and width
# Function requires height in order to wrap data, but does not package height itself
def package(poolData, dataArray, h, w):
    for (rowIndex) in range(h):
        poolData.append([dataArray[(rowIndex - 1) % h], dataArray[(rowIndex)], dataArray[(rowIndex + 1) % h], w])

# rowCheck: takes input, a 2D array of three lines, and returns the middle line with corrected values.
# rowCheck assumes vertical wraparound has already been accounted for
def rowCheck(array):
    i=1
    # Array to return
    nextArray=[None]*array[3]
    for j in range(array[3]):
        up = (i - 1)
        down = (i + 1)
        left = (j - 1) % array[3]
        right = ((j + 1) % array[3])
        sum1=(array[up][left]+array[up][j]+array[up][right])
        sum2=array[i][left]+array[i][right]
        sum3=array[down][left]+array[down][j]+array[down][right]
        sums = sum1+sum2+sum3
        if array[i][j] == 1:
            if sums == 0 or (sums % 2) == 1 or sums == 8:
                nextArray[j] = 0
            else:
                nextArray[j] = 1
        elif sums == 2 or sums == 3 or sums == 5 or sums == 7:
            nextArray[j] = 1
        else:
            nextArray[j] = 0
    return nextArray

if __name__ == "__main__":
    print("Project :: R11702155")
    main()
