def print_graph(arr, start_row=0, start_col=0):
    row = len(arr)
    col = len(arr[0])

    print()

    for i in range(start_row, row):
        for j in range(start_col, col):
            print(arr[i][j], end = ' ')
        print()

    print()