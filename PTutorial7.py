
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def winner(board,player):
    win_combinations=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for combo in win_combinations:
        if board[combo[0]]==board[combo[1]]==board[combo[2]]==player:
            return True
    return False

def get_input(player,board):
    position=int(input("Enter position from 1-9:"))
    if position in range(1,10):
        position-=1
        if board[position]==" ":
            return position
        else:
            print("Position is already taken")
    else:
        print("Invalid input")
    return get_input(player,board)

def play_game():
    board=[" "]*9
    current_player="X"
    for i in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn")
        pos=get_input(current_player,board)
        board[pos]=current_player
        if winner(board,current_player):
            print_board(board)
            print(f"Player {current_player} wins")
            break
        current_player="O" if current_player=="X" else "X"
    else:
        print_board(board)
        print("It's a tie")
    play_again=input("Do you want to replay?").lower()
    if play_again=="y":
        play_game()
    else:
        print("Game Over")

play_game()
#Project2
tasks = []
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!\n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.\n")
    else:
        print("Your To-Do List:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])
        print()

def delete_task():
    view_tasks()
    if len(tasks) > 0:
        index = int(input("Enter the task number to delete: "))
        if index > 0 and index <= len(tasks):
            tasks.pop(index - 1)
            print("Task deleted!\n")
        else:
            print("Invalid task number.\n")

def main():
    choice = ""
    while choice != "4":
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting program.")
        else:
            print("Invalid choice.\n")

main()
#Project3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_grid(rows, cols, obstacles):
    grid = np.zeros((rows, cols), dtype=int)
    for r, c in obstacles:
        grid[r][c] = 1
    return grid

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_list = [start]
    came_from = {}
    g_score = {tuple(start): 0}
    f_score = {tuple(start): manhattan(start, goal)}
    
    while open_list:
        open_list.sort(key=lambda x: f_score.get(tuple(x), float('inf')))
        current = open_list.pop(0)
        
        if current == goal:
            path = [tuple(current)]
            while tuple(current) in came_from:
                current = came_from[tuple(current)]
                path.append(tuple(current))
            return path[::-1]
        
        r, c = current
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                if grid[nr][nc] == 1:
                    continue
                tentative_g = g_score[tuple(current)] + 1
                if tentative_g < g_score.get((nr, nc), float('inf')):
                    came_from[(nr, nc)] = tuple(current)
                    g_score[(nr, nc)] = tentative_g
                    f_score[(nr, nc)] = tentative_g + manhattan((nr, nc), goal)
                    if [nr, nc] not in open_list:
                        open_list.append([nr, nc])
    return None

def visualize(grid, path, start, goal):
    plt.imshow(grid, cmap='gray_r')
    if path:
        pr, pc = zip(*path)
        plt.scatter(pc, pr, c='red', s=60)
    plt.scatter(start[1], start[0], c='green', s=100, label='Start')
    plt.scatter(goal[1], goal[0], c='blue', s=100, label='Goal')
    plt.legend()
    plt.show()

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    num_obs = int(input("Enter number of obstacles: "))
    obstacles = []
    for i in range(num_obs):
        r = int(input(f"Enter obstacle {i+1} row: "))
        c = int(input(f"Enter obstacle {i+1} col: "))
        obstacles.append((r, c))
    
    start = [int(input("Enter start row: ")), int(input("Enter start col: "))]
    goal = [int(input("Enter goal row: ")), int(input("Enter goal col: "))]
    
    grid = create_grid(rows, cols, obstacles)
    print("\nGrid Data:")
    print(pd.DataFrame(grid))
    
    path = astar(grid, start, goal)
    if path:
        print("\nPath Found:", path)
    else:
        print("\nNo valid path found.")
    
    visualize(grid, path, start, goal)

main()

