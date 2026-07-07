import random
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
    invisible[x-1][y-1] = "O"
    print("Safe!")
    return True
def check_win(opened, board):
    return all(opened[i][j] or board[i][j] == "*" for i in range(size) for j in range(size))

def main():
    invisible, board, opened, minesplaced = create_board(size)
    board, minesplaced = place_mines(board, minesplaced)
    game_over = False
    while not game_over:
        print("Choose a cell:")
        x, y = get_coordinates(size, opened)
        if not opencell(x, y, board, opened, invisible):
            game_over = True
        for row in invisible:
            print(" ".join(row))
        if check_win(opened, board):
                print("Congratulations! You won!")
                game_over = True
if __name__ == "__main__":
    main()