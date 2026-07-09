import random
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]
while True:
    difficulty = input("Enter difficulty (easy, medium, hard): ")
    if difficulty == "easy":
        size = 8
        break
    elif difficulty == "medium":
        size = 12
        break
    elif difficulty == "hard":
        size = 16
        break
    else:
        print("Invalid difficulty level. Please try again.")
        continue

def create_board(size):
        invisible = [["-"]*size for _ in range(size)]
        board = [[0]*size for _ in range(size)]
        opened = [[False]*size for _ in range(size)]
        minesplaced = [[False]*size for _ in range(size)]
        return invisible, board, opened, minesplaced
def place_mines(board, minesplaced):
    mines = 0
    minecount = random.randint(size,size+2)
    while mines < minecount:
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        if board[x][y] == 0:
            board[x][y] = "*"
            minesplaced[x][y] = True
            mines += 1
    return board, minesplaced
def calculate_numbers(board, minesplaced):
    for x in range(size):
        for y in range(size):
            if board[x][y] == "*":
                continue
            count = closer_mines(x, y, minesplaced)
            board[x][y] = count
    return board
def closer_mines(x, y, minesplaced):
    count = 0
    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < size and 0 <= new_y < size and minesplaced[new_x][new_y]:
            count += 1
    return count
def get_coordinates(size, opened):
    while True:
        x = int(input(f"Enter row (1-{size}): "))
        y = int(input(f"Enter column (1-{size}): "))
        if x < 1 or x > size:
            print(f"Invalid row. Please enter a value between 1 and {size}.")
            continue
        if y < 1 or y > size:
            print(f"Invalid column. Please enter a value between 1 and {size}.")
            continue
        if opened[x-1][y-1]:
            print("This area is already opened.")
            continue
        return x, y
def opencell(x, y, board, opened, invisible):
    if board[x-1][y-1] == "*":
        invisible[x-1][y-1] = "*"
        print("BOOOM!")
        return False
    opened[x-1][y-1] = True
    invisible[x-1][y-1] = str(board[x-1][y-1])
    print("Safe!")
    return True
def reveal_mines(minesplaced, invisible):
    for x in range(size):
        for y in range(size):
            if minesplaced[x][y]:
                invisible[x][y] = "*"
    return invisible
def check_win(opened, board):
    return all(opened[i][j] or board[i][j] == "*" for i in range(size) for j in range(size))
def main():
    invisible, board, opened, minesplaced = create_board(size)
    board, minesplaced = place_mines(board, minesplaced)
    board = calculate_numbers(board, minesplaced)
    game_over = False
    while not game_over:
        print("Choose a cell:")
        x, y = get_coordinates(size, opened)
        if not opencell(x, y, board, opened, invisible):
            reveal_mines(minesplaced, invisible)
        for row in invisible:
            print(" ".join(row))
        if check_win(opened, board):
                print("Congratulations! You won!")
                game_over = True
if __name__ == "__main__":
    main()
