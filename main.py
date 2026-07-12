import random
GREEN = "\033[32m"
YELLOW = "\033[33m"
ORANGE = "\033[38;5;172m"
RED = "\033[31m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
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
    if difficulty == "easy":
        minecount=random.randint(size+2,size+5)
    if difficulty == "medium":
        minecount=random.randint(size+5,size+10)
    if difficulty == "hard":
        minecount=random.randint(size+10,size+20)
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
def open_cell(x, y, board, opened, invisible):
    if board[x-1][y-1] == "*":
        invisible[x-1][y-1] = "*"
        print("BOOOM!")
        return False
    print("Safe!")
    if board[x-1][y-1] == 0:
        fill_flood(board, x, y, invisible, opened)
    else:
        opened[x-1][y-1] = True
        invisible[x-1][y-1] = str(board[x-1][y-1])
    return True
def reveal_mines(minesplaced, invisible):
    for x in range(size):
        for y in range(size):
            if minesplaced[x][y]:
                invisible[x][y] = "*"
    return invisible
def fill_flood(board,x,y,invisible,opened):
    if x<1 or x>size or y<1 or y>size:
        return
    if opened[x-1][y-1]:
        return
    opened[x-1][y-1] = True
    invisible[x-1][y-1] = str(board[x-1][y-1])  
    if board[x-1][y-1] != 0:
        return
    for dx, dy in DIRECTIONS:
        fill_flood(board, x+dx,y+dy,invisible, opened)
def check_win(opened, board):
    return all(opened[i][j] or board[i][j] == "*" for i in range(size) for j in range(size))
def print_board(invisible):
    for row in invisible:
        line = ""

        for cell in row:
            if cell == "0":
                line += CYAN + cell
            elif cell == "1":
                line += GREEN + cell
            elif cell == "2":
                line += YELLOW + cell
            elif cell == "3":
                line += ORANGE + cell
            elif cell == "4" or cell == "5" or cell == "6" or cell == "7" or cell == "8":
                line += RED + cell
            else:
                line += WHITE + cell

            line += RESET + " "

        print(line)
def main():
    invisible, board, opened, minesplaced = create_board(size)
    board, minesplaced = place_mines(board, minesplaced)
    board = calculate_numbers(board, minesplaced)
    game_over = False
    while not game_over:
        print("Choose a cell:")
        x, y = get_coordinates(size, opened)
        if not open_cell(x, y, board, opened, invisible):
            reveal_mines(minesplaced, invisible)
            game_over = True
        print_board(invisible)
        if check_win(opened, board):
                print("Congratulations! You won!")
                game_over = True
if __name__ == "__main__":
    main()
