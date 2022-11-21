def isPrime(x):
    for i in range(2, int(x / 2)):
        if (x % i) == 0:
            return False
    return True


def main():
    array = []
    input_file = open('C:/Users/tjlib/PycharmProjects/ConceptsProject/input.dat', 'r')
    print(type(input_file))
    for line in input_file:
        array.append(list(line))
    print((array[-1][-1]))
    height = len(array)
    width = len(array[0]) - 1
    print(height, width)
    count = 100
    nextArray = list(map(list, array))
    while count != 0:
        for i in range(height):
            for j in range(width):
                neighbor_sum = 0
                up = (i - 1) % height
                down = (i + 1) % height
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
                print(neighbor_sum)
                print(array[up][left],array[up][j],array[up][right])
                print(array[i][left]," ",array[i][right])
                print(i,left)
                print(array[down][left],array[down][j],array[down][right])
                if array[i][j] == '+':
                    if neighbor_sum == 0 or neighbor_sum == 8 or (neighbor_sum % 2) == 1:
                        print("Killing\n")
                        nextArray[i][j] = '-'
                        continue
                    continue
                elif array[i][j] == '-' and (neighbor_sum == 2 or neighbor_sum == 3 or neighbor_sum == 5 or neighbor_sum == 7):
                    print("Aliving\n")
                    nextArray[i][j] = '+'
        count = count - 1
        array = list(map(list, nextArray))
    output_file = open('C:/Users/tjlib/PycharmProjects/ConceptsProject/input_test1.dat', 'w')
    for i in range(height):
        for j in range(width):
            output_file.write(nextArray[i][j])
        output_file.write('\n')

    # if (i-1,j-1) (i,j-1) ()


if __name__ == "__main__":
    main()
