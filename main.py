import argparse
from multiprocessing import Pool
import time

def main():
    argumentParse = argparse.ArgumentParser(prog='Concepts Project', description =
    'Fulfills final project requirements via multithreading')
    argumentParse.add_argument('-i', "--inputFile", required=True)
    argumentParse.add_argument('-o', "--outputFile", required=True)
    argumentParse.add_argument('-t', "--threadCount", type=int, default=1, required=False)
    commandLineArgs = argumentParse.parse_args()
    array = []
    input_file = open(commandLineArgs.inputFile, 'r')
    threads = commandLineArgs.threadCount
    if threads < 1:
        raise Exception("Threads cannot be zero or negative")
    processPool = Pool(processes=threads)
    poolData = list()
    for (line) in input_file:
        line = line[:-1]
        array.append(list(line))
    height = len(array) - 1
    width = len(array[0])
    print(height, width)
    count = 100
    for rowIndex in range(height):
        subArray = list()
        subArray.append(array[(rowIndex-1)%height])
        subArray.append(array[(rowIndex)])
        subArray.append(array[(rowIndex + 1) % height])
        poolData.append(subArray)
    while count != 0:
        nextArray = processPool.map(rowCheck , poolData)
        for i in range(height):
            poolData[i][0] = nextArray[(i - 1)%height]
            poolData[i][1] = nextArray[i]
            poolData[i][2] = nextArray[(i + 1) % height]
        count = count-1
    output_file = open(commandLineArgs.outputFile, 'w')
    for i in range(height):
        for j in range(width):
            output_file.write(nextArray[i][j])
        output_file.write('\n')

def rowCheck(array):
    i=1
    width = len(array[0])
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
    st = time.time()
    print("Project :: R11702155")
    main()
    end = time.time()
    print(end-st)
