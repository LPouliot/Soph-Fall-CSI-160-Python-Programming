
EMPTY = ""

board1 = [
        ["X",EMPTY,EMPTY],
        [EMPTY,"0",EMPTY],
        [EMPTY,EMPTY,EMPTY]
]

# print(board1[0][0])
# print(board1[1][1])

board2 = [
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY]
]


# Assume space is 1,1
def is_empty():
    p = input("Player: ")
    r = int(input("What Row: "))
    c = int(input("What Column: "))

    result = board2[r][c]
    if result == False:
        print("Slot Availble")
    else:
        print("Try again")

is_empty()






