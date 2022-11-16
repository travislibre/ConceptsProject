def main():
    array = []
    input_file = open('C:/Users/tjlib/PycharmProjects/ConceptsProject/input.dat', 'r')
    print(type(input_file))
    for line in input_file:
        array.append(line)
    print((array[-1][-1]))
    height = len(array)
    width = len(array[0])-1
    print(height,width)
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
        #print(array[up][left], array[up][j], array[up][right], '\n')
        #print(array[i][left], array[i][j], array[i][right], '\n')
        #print(array[down][left], array[down][j], array[down][right], '\n')

    # if (i-1,j-1) (i,j-1) ()


if __name__ == "__main__":
    main()
