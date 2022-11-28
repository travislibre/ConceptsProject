import argparse
from multiprocessing import Pool

def isPrime(x):
    for i in range(2, int(x / 2)):
        if (x % i) == 0:
            return False
    return True


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
    for line in input_file:
        array.append(list(line))
    height = len(array) - 1
    width = len(array[0]) - 1
    print(height, width)
    count = 100

    for rowIndex in range(height):
        subArray = list()
        subArray.append(array[(rowIndex-1)%height])
        subArray.append(array[(rowIndex)])
        subArray.append(array[(rowIndex + 1) % height])
        poolData.append(subArray)
    while count != 0:
        nextArray = processPool.map(rowCheck,poolData, width, height)
        for i in range(height):
            poolData[i][0] = nextArray[(i - 1)%height]
            poolData[i][1] = nextArray[i]
            poolData[i][2] = nextArray[(i + 1) % height]
    output_file = open(commandLineArgs.outputFile, 'w')
    for i in range(height):
        for j in range(width):
            output_file.write(nextArray[i][j])
        output_file.write('\n')



def rowCheck(array, width, length):
    i=1

    nextArray=[]
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
        # print(neighbor_sum)
        # print(array[up][left],array[up][j],array[up][right])
        # print(array[i][left]," ",array[i][right])
        # print(i,left)
        # print(array[down][left],array[down][j],array[down][right])
        if array[i][j] == '+':
            if neighbor_sum == 0 or (neighbor_sum % 2) == 1 or neighbor_sum == 8:
                # print("Killing\n")
                nextArray[i] = '-'
            else:
                nextArray[i] = '+'
        elif array[i][j] == '-' and (
                neighbor_sum == 2 or neighbor_sum == 3 or neighbor_sum == 5 or neighbor_sum == 7):
            # print("Aliving\n")
            nextArray[i] = '+'
        else:
            nextArray[i] = '-'
    return nextArray

if __name__ == "__main__":
    main()
