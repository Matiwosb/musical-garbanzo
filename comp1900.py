# def find_path(data, starting_row):
#     # to return final path
#
#     result = []
#
#     # keep count so that, while checking we don't check outside of range
#
#     n_rows = len(data) - 2
#
#     columns = len(data[0])
#
#     # initialize starting position
#
#     row = starting_row
#
#     # append starting position
#
#     result.append(row)
#
#     # iterate for number columns - 1, so that we dont check outside list range
#
#     for i in range(columns - 1):
#
#         # list to store difference details
#
#         difference = []
#
#         # check if it is not upper edge
#
#         if row > 0:
#
#             # append details for north-east direction
#
#             difference.append((data[row][i] - data[row - 1][i + 1], 'NE', row - 1))
#
#             # append details for east direction
#
#             difference.append((data[row][i] - data[row][i + 1], 'E', row))
#
#             # check if it is not lower edge
#
#             if row < n_rows:
#                 # append details for south-east direction
#
#                 difference.append((data[row][i] - data[row + 1][i + 1], 'SE', row + 1))
#
#                 # get the minimum difference details based on the difference stored on 0th index
#
#                 row = min(difference, key=lambda x: abs(x[0]))[-1]
#
#                 # append row to result list
#
#                 result.append(row)
#
#         # return the result
#
#         return result
#
#
# path = [
#
#     [4, 4, 0, 9, 8],
#
#     [4, 6, 5, 5, 8],
#
#     [5, 5, 2, 3, 0],
#
#     [7, 1, 1, 0, 9]
#
# ]
#
# find_path(path, 3)

forest = [[4, 4, 0, 9, 8],
          [4, 6, 5, 5, 8],
          [5, 5, 2, 3, 0],
          [7, 1, 1, 0, 9]
          ]


# def find_path(data,starting_row):
#     row = []
#     # starting_point = len(data[starting_row][0])
#     columns = len(data[0])
#     current_row = starting_row
#     #print(starting_point)
#     # #for i in range(row):
#     # print(i) #
#     # for j in range(column):
#     num_row = len(data) - 2
#     row.append(current_row)
#     for i in range(columns - 1):
#         a = []
#         if current_row > 0:
#             a.append((data[row][i] - data[current_row - 1][i + 1], 'NE', current_row - 1))
#
#             # append details for east direction
#
#             a.append((data[current_row][i] - data[current_row][i + 1], 'E', current_row))
#
#         if row < num_row:
#                 # append details for south-east direction
#
#                 a.append((data[current_row][i] - data[current_row + 1][i + 1], 'SE', current_row + 1))
#
#                 # get the minimum difference details based on the difference stored on 0th index
#
#                 rows = min(a, key=lambda x: abs(x[0]))[-1]
#
#                 # append row to result list
#
#                 row.append(rows)
#
#         # return the result
#
#         return row

def find_path(data, starting_row):
    # to return final path
    result = []
    # keep count so that, while checking we don't check outside of range
    n_rows = len(data) - 2
    columns = len(data[0])
    # initialize starting position
    row = starting_row
    # append starting position
    result.append(row)
    # iterate for number columns - 1, so that we dont check outside list range
    for i in range(columns - 1):
        # list to store difference details
        difference = []
        # check if it is not upper edge
        if row > 0:
            # append details for north-east direction
            difference.append((data[row][i] - data[row - 1][i + 1], 'NE', row - 1))
        # append details for east direction
        difference.append((data[row][i] - data[row][i + 1], 'E', row))
        # check if it is not lower edge
        if row < n_rows:
            # append details for south-east direction
            difference.append((data[row][i] - data[row + 1][i + 1], 'SE', row + 1))
        # get the minimum difference details based on the difference stored on 0th index
        row = min(difference, key=lambda x: abs(x[0]))[-1]
        # append row to result list
        result.append(row)
    # return the result
    return result

find_path(forest, 3)
